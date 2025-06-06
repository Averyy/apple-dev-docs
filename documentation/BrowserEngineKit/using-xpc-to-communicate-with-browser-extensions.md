# Using XPC to communicate with browser extensions

**Framework**: Browserenginekit

Build interprocess communication between your host app and extensions.

#### Overview

When `BrowserEngineKit` launches your extension processes, it provides the host app with a simple way to initiate an [`XPC`](https://developer.apple.com/documentation/XPC) connection with the extensions. Use this connection to communicate with the extensions, and to set up anonymous connections that the extensions use to communicate directly with each other.

#### Create a Connection in the Browser App

When your browser app has launched an extension, call the extension’s `makeLibXPCConnection()` method to create and initialize an [`xpc_connection_t`](https://developer.apple.com/documentation/XPC/xpc_connection_t) that represents an XPC connection between the browser app and the extension.

For example, to get an `xpc_connection_t` that represents a `libxpc` connection for IPC between your host app and its networking extension:

```swift
do {
  let networkExtensionConnection = try networkProcess.makeLibXPCConnection()
  // Use the connection.
} catch {
  // Handle the error.
}
```

Use the [`XPC`](https://developer.apple.com/documentation/XPC) framework to create objects that represent messages you send over the connection. You send all messages as dictionary objects. For example, to send a URL to the network extension:

```swift
extension URL {
    func toXPCObject() -> xpc_object_t {
		let urlString = xpc_string_create(self.absoluteString)
        let dict = xpc_dictionary_create_empty()
        xpc_dictionary_set_string(dict, "x-url-key", urlString)
        return dict
    }
}

func fetchData(from url: URL, over connection: xpc_connection_t) throws {
    xpc_connection_send_message_with_reply(connection, url.toXPCObject(), nil) { reply in
        // Handle the reply object.
    }
}
```

The [`xpc_connection_t`](https://developer.apple.com/documentation/XPC/xpc_connection_t) data type and functions that act on it are described in [`XPC connections`](https://developer.apple.com/documentation/XPC/xpc-connections). It is recommended that you use this API for browser apps and their extensions.

#### Handle Xpc Events in the Extension

When your browser app calls an extension process’s `makeLibXPCConnection()` method, `BrowserEngineKit` sets up the XPC connection and calls your extension’s `handle(xpcConnection:)` method. In your implementation of this method, install an event handler to process messages sent over this connection, and activate the connection:

```swift
class MyNetworkExtension: NetworkingExtension {

	public func handle(xpcConnection: xpc_connection_t) {
		xpc_connection_set_event_handler(xpcConnection) { event in
			// Process the event, replying if necessary.
		}
		xpc_connection_activate(xpcConnection)
	}
	
}
```

> ❗ **Important**:  Don’t call [`xpc_main(_:)`](https://developer.apple.com/documentation/XPC/xpc_main(_:)) from a browser extension. This function sets up the event loop for an XPC service, which causes problems if you call it in a process that isn’t an XPC service, for example a browser extension.

#### Pass Anonymous Connection Endpoints Between Extensions

When two extensions that are part of the same browser app need to communicate directly, send an XPC message requesting an anonymous endpoint from the browser app to the first extension. In the first extension’s connection handler, configure and activate the connection. Wrap the connection you created in an [`xpc_endpoint_t`](https://developer.apple.com/documentation/XPC/xpc_endpoint_t) and send it in a reply to the host app:

```swift
/* In the connection event handler for the connection to the browser app,
 * when you determine that a message is a request to open a connection to
 * another extension.
 */
 
// Set up the anonymous XPC connection.
let anonymousConnection = xpc_connection_create(nil, nil)
xpc_connection_set_event_handler(anonymousConnection) { event in
	// Process events from the other extension.
}
xpc_connection_activate(anonymousConnection)

// Create an endpoint and send it to the browser app in reply to the message.
let endpoint = xpc_endpoint_create(anonymousConnection)
let reply = xpc_dictionary_create_reply(originalMessage)
xpc_dictionary_set_value(reply, "x-endpoint-key", endpoint)

xpc_connection_send_message(browserConnection, reply)
```

In the browser app’s reply handler, pass the `xpc_endpoint_t` to the other extension.

```swift
/* The reply handler in the browser app. */

let endpointRequestReplyHandler = { replyWithEndpoint in
	// Check for error.
	guard xpc_get_type(replyWithEndpoint) != XPC_TYPE_DICTIONARY else {
		// Handle the error.
		return
	}
	// Send the dictionary that contains the endpoint to the other extension.
	xpc_connection_send(otherEndpointConnection, replyWithEndpoint)
}
```

Finally, in the extension that receives the `xpc_endpoint_t`, call [`xpc_connection_create_from_endpoint(_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_create_from_endpoint(_:)) to get an `xpc_connection_t` that the receiving extension uses to message the creating extension.

```swift
/* The connection event handler for the receiving extension. */

// Retrieve the endpoint from the connection event
let	endpoint = xpc_dictionary_get_value(reply, "x-endpoint-key")

guard let endpoint = endpoint else {
	// Handle an incorrectly-formed message.
	return
}

// Create a new connection from the endpoint.
let otherExtensionConnection = xpc_connection_create_from_endpoint(endpoint)

// Send messages to the other extension.
```

#### Verify the Identity of the Remote Process

To be confident that your browser app or extension is communicating with the correct component, set a lightweight code requirement on the XPC connection. The operating system tests that the executable for the process at the remote end of the connection satisfies the requirement each time the process sends a message.

> **Note**:  It’s possible for the process sending messages to your XPC connection to change at runtime, for example, if the listener creates an [`xpc_endpoint_t`](https://developer.apple.com/documentation/XPC/xpc_endpoint_t) and forwards it to a different process.

In the sending process, if you send a message over an XPC connection and the receiving process doesn’t satisfy the lightweight code requirement you set, the message isn’t delivered. If you request a reply, XPC delivers the `XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT` error.

In the receiving process, if a process that doesn’t satisfy the lightweight code requirement you set sends a message to your connection, the operating system drops the message and your event handler isn’t called.

The sending and receiving process can each set a single lightweight code requirement on an XPC connection. For information on creating complex requirements that test multiple properties of the communicating process’s executable, see [`Defining launch environment and library constraints`](https://developer.apple.com/documentation/Security/defining-launch-environment-and-library-constraints).

For each XPC connection on which you set a lightweight code requirement, call one of the functions below to define the lightweight code requirement and attach it to the connection. Each function returns `0` if it sets the lightweight code requirement, or another value if it encounters an error.

It’s an error to call multiple functions that set lightweight code requirements on the same XPC connection, or the same function more than once. If you do, the operating system terminates your process.

For example, to require that the executable’s code signature contains the browser rendering extension entitlement with a value of `com.example.browserapp`:

```swift
let expectedValue = xpc_string_create("com.example.browserapp")
xpc_connection_set_peer_entitlement_matches_value_requirement(connection,
	"com.apple.developer.web-browser-engine.rendering",
	expectedValue);

// Use the connection.
```

## See Also

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)
  Coordinate helper processes to efficiently support your browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserEngineKit/using-xpc-to-communicate-with-browser-extensions)*
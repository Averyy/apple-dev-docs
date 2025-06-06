# handle(xpcConnection:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Accept or reject an incoming XPC connection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func handle(xpcConnection: xpc_connection_t)
```

#### Overview

When your browser app calls [`makeLibXPCConnection()`](networkingprocess/makelibxpcconnection().md), `BrowserEngineKit` calls this method on your extension, passing the newly created connection as the parameter. To accept the connection, call [`xpc_connection_set_event_handler(_:_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_set_event_handler(_:_:)) to install an event handler and listen for incoming messages.

Otherwise, call [`xpc_connection_cancel(_:)`](https://developer.apple.com/documentation/XPC/xpc_connection_cancel(_:)) to reject the connection.

## Parameters

- `xpcConnection`: The inbound connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingextension/handle(xpcconnection:))*
# TN3113: Testing and debugging XPC code with an anonymous listener

**Framework**: Technotes

Use an anonymous XPC listener to simplify your XPC testing and debugging.

#### Overview

Testing and debugging XPC code is tricky because there are two processes involved.  Imagine you have an app with an embedded XPC service.  To debug this you have to run two instances of the debugger, one connected to the app and another to the service, and then switch between them.  This works, but it’s quite inconvenient.  Fortunately there is a better way, a technique that allows you to test and debug all your XPC code in a single process.

> ❗ **Important**: This technique does not help with all XPC testing and debugging scenarios.  For example, if you’re developing a `launchd` daemon that performs privileged operations on behalf of your app, you can’t use this technique to debug your privileged code because it’s not running in a privileged process.  However, even in situations like that, this technique is useful when debugging your XPC-specific code.  For example, you might use it to create a unit test for your [`NSSecureCoding`](https://developer.apple.com/documentation/foundation/nssecurecoding) implementation.

This technique involves two key concepts:

- Put your XPC listener and XPC client code in the same test program.  The specifics of this program are up to you: It might be a simple test app that you create specifically for this purpose, or it might be an Xcode unit test bundle, or it might be some other kind of program.
- Use an anonymous XPC listener to connect your XPC listener and client code.

Imagine you’re building an app with an embedded XPC service.  You have a `MyListener` class that manages your XPC listener within the XPC service, and a `MyConnection` class that manages the connection on the app side of things.  Add both of those classes, and all their support code, to your test program.  Then change `MyListener` to accept an `NSXPCListener` instance.  For example, your `MyListener` class might look like this:

```swift
class MyListener {

    init() {
        self.listener = NSXPCListener.service()
    }

    let listener: NSXPCListener
    
    … more code …
}
```

> **Note**: While this example uses the Foundation [`XPC`](https://developer.apple.com/documentation/foundation/xpc) API, the same technique works for the low-level C [`XPC`](https://developer.apple.com/documentation/xpc) API.

Change its initialiser to look like this:

```swift
init(listener: NSXPCListener = .service()) {
    self.listener = listener
}
```

This uses the XPC service’s listener by default, but allows you to override that by passing in a value to the `listener` parameter.

Now, in your test program, call [`anonymous()`](https://developer.apple.com/documentation/foundation/nsxpclistener/anonymous()) to create a anonymous listener and pass that to your listener abstraction:

```swift
let myListener = MyListener(listener: .anonymous())
```

On the client side, your `MyConnection` class might look like this:

```swift
class MyConnection {

    init() {
        self.connection = NSXPCConnection(serviceName: "com.example.MyService")
    }

    let connection: NSXPCConnection
}
```

Change the initialiser to look like this:

```swift
init(connection: NSXPCConnection = .init(serviceName: "com.example.MyService")) {
    self.connection = connection
}
```

This sets up a connection to the XPC service’s listener by default, but allows you to override that by passing in a value to the `connection` parameter.

Finally, in your test program, use [`init(listenerEndpoint:)`](https://developer.apple.com/documentation/foundation/nsxpcconnection/init(listenerendpoint:)) to create a connection to your anonymous listener:

```swift
let connection = NSXPCConnection(listenerEndpoint: myListener.listener.endpoint)
let myConnection = MyConnection(connection: connection)
```

You now have an XPC connection between your client code and your listener, with all the code running in the same test program.  This makes it much easier to debug your XPC code.  And the same technique is perfect for unit tests.

#### Revision History

- **2022-04-12** Added syntax highlighting to the code listings (r. 89366505).
- **2022-02-08** Republished as TN3113.  Expanded the introduction to clarify the overall concept.  Made other minor editorial changes.
- **2021-11-09** First published as ”Testing and Debugging XPC Code With an Anonymous Listener” on Apple Developer Forums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3113-testing-xpc-code-with-an-anonymous-listener)*
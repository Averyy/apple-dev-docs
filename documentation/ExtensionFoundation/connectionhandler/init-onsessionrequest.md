# init(onSessionRequest:)

**Framework**: ExtensionFoundation  
**Kind**: init

Initializes the connection handler with a closure that accepts an XPC session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(onSessionRequest requestHandler: @escaping (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)
```

#### Discussion

Use this initializer if your app extension communicates with the host app using types from the [`XPC`](https://developer.apple.com/documentation/XPC) framework.

## See Also

- [init(onConnection: (NSXPCConnection) -> Bool)](connectionhandler/init(onconnection:).md)
  Initializes the connection handler with a closure that accepts a Foundation XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler/init(onsessionrequest:))*
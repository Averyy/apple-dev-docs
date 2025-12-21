# init(onConnection:)

**Framework**: ExtensionFoundation  
**Kind**: init

Initializes the connection handler with a closure that accepts a Foundation XPC object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 1.1+

## Declaration

```swift
@MainActor
@preconcurrency init(onConnection connectionHandler: @escaping (NSXPCConnection) -> Bool)
```

#### Discussion

Use this initializer if your app extension communicates with the host app using [`XPC`](https://developer.apple.com/documentation/Foundation/xpc).

## See Also

- [init(onSessionRequest: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)](connectionhandler/init(onsessionrequest:).md)
  Initializes the connection handler with a closure that accepts an XPC session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler/init(onconnection:))*
# init(onSessionRequest:)

**Framework**: ExtensionFoundation  
**Kind**: init  
**Role**: Initializer

Initializes the connection handler with a closure that accepts an XPC session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(onSessionRequest requestHandler: @escaping @Sendable (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)
```

#### Discussion

Use this initializer if your app extension communicates with the host app using types from the [XPC](../../XPC/XPC.md) framework.

## See Also

### Initializing the connection handler
- [init(onConnection: (NSXPCConnection) -> Bool)](./init%28onconnection%29.md)
  Initializes the connection handler with a closure that accepts a Foundation XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler/init(onsessionrequest:))*
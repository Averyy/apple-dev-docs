# ConnectionHandler

**Framework**: ExtensionFoundation  
**Kind**: struct

ConnectionHandler handles incoming XPC connections.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 1.1+

## Declaration

```swift
@MainActor
@preconcurrency struct ConnectionHandler
```

## Topics

### Initializers
- [init(onConnection: (NSXPCConnection) -> Bool)](connectionhandler/init(onconnection:).md)
  Creates a `ConnectionHandler` with an `NSXPCConnection` request handler.
- [init(onSessionRequest: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)](connectionhandler/init(onsessionrequest:).md)
  Creates a `ConnectionHandler` with an `XPCSession` request handler.

## Relationships

### Conforms To
- [AppExtensionConfiguration](appextensionconfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler)*
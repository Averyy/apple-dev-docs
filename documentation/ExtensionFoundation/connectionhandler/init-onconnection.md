# init(onConnection:)

**Framework**: ExtensionFoundation  
**Kind**: init

Creates a `ConnectionHandler` with an `NSXPCConnection` request handler.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 1.1+

## Declaration

```swift
@MainActor
@preconcurrency init(onConnection connectionHandler: @escaping (NSXPCConnection) -> Bool)
```

#### Discussion

The `requestHandler` will be called every time the host process attempts to create an `NSXPCConnection` to the extension. The extension must respond to the request by either configuring and resuming the connection and returning `true` or rejecting by returning `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler/init(onconnection:))*
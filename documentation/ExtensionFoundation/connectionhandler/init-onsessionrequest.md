# init(onSessionRequest:)

**Framework**: ExtensionFoundation  
**Kind**: init

Creates a `ConnectionHandler` with an `XPCSession` request handler.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(onSessionRequest requestHandler: @escaping (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)
```

#### Discussion

The `requestHandler` will be called every time the host process attempts to start an `XPCSession` with the extension. The extension must respond to the request by either accepting or rejecting it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler/init(onsessionrequest:))*
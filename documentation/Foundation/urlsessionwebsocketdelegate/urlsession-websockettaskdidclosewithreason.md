# urlSession(_:webSocketTask:didCloseWith:reason:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?)
```

## Parameters

- `session`: The session of the WebSocket task that closed.
- `webSocketTask`: The WebSocket task that closed.
- `closeCode`: The close code provided by the server. If the close frame didn’t include a close code, this value is  .
- `reason`: The close reason provided by the server. If the close frame didn’t include a reason, this value is  .

## See Also

- [func urlSession(URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol: String?)](urlsessionwebsocketdelegate/urlsession(_:websockettask:didopenwithprotocol:).md)
  Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate/urlsession(_:websockettask:didclosewith:reason:))*
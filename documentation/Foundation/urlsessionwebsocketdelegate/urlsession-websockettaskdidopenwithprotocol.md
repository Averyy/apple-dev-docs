# urlSession(_:webSocketTask:didOpenWithProtocol:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.

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
optional func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol protocol: String?)
```

#### Discussion

If the handshake fails, the task doesn’t call this delegate method.

## Parameters

- `session`: The session of the WebSocket task that opened.
- `webSocketTask`: The WebSocket task that opened.
- `protocol`: The protocol picked during the handshake phase. This parameter is   if the server did not pick a protocol, or if the client did not advertise protocols when creating the task.

## See Also

- [func urlSession(URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith: URLSessionWebSocketTask.CloseCode, reason: Data?)](urlsessionwebsocketdelegate/urlsession(_:websockettask:didclosewith:reason:).md)
  Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate/urlsession(_:websockettask:didopenwithprotocol:))*
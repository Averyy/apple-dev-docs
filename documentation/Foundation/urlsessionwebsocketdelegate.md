# URLSessionWebSocketDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.

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
protocol URLSessionWebSocketDelegate : URLSessionTaskDelegate
```

## Topics

### Handling WebSocket lifecycle events
- [func urlSession(URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol: String?)](urlsessionwebsocketdelegate/urlsession(_:websockettask:didopenwithprotocol:).md)
  Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.
- [func urlSession(URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith: URLSessionWebSocketTask.CloseCode, reason: Data?)](urlsessionwebsocketdelegate/urlsession(_:websockettask:didclosewith:reason:).md)
  Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [URLSessionDelegate](urlsessiondelegate.md)
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## See Also

- [func webSocketTask(with: URL) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-87ipz.md)
  Creates a WebSocket task for the provided URL.
- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [func webSocketTask(with: URL, protocols: [String]) -> URLSessionWebSocketTask](urlsession/websockettask(with:protocols:).md)
  Creates a WebSocket task given a URL and an array of protocols.
- [class URLSessionWebSocketTask](urlsessionwebsockettask.md)
  A URL session task that communicates over the WebSockets protocol standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate)*
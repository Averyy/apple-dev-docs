# URLSessionWebSocketDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSURLSessionWebSocketDelegate <NSURLSessionTaskDelegate>
```

## Topics

### Handling WebSocket lifecycle events
- [func urlSession(URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol: String?)](./urlsessionwebsocketdelegate/urlsession%28_,websockettask,didopenwithprotocol%29.md)
  Tells the delegate that the WebSocket task successfully negotiated the handshake with the endpoint, indicating the negotiated protocol.
- [func urlSession(URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith: URLSessionWebSocketTask.CloseCode, reason: Data?)](./urlsessionwebsocketdelegate/urlsession%28_,websockettask,didclosewith,reason%29.md)
  Tells the delegate that the WebSocket task received a close frame from the server endpoint, optionally including a close code and reason from the server.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [URLSessionDelegate](./urlsessiondelegate.md)
- [URLSessionTaskDelegate](./urlsessiontaskdelegate.md)

## See Also

### Adding WebSocket tasks to a session
- [func webSocketTask(with: URL) -> URLSessionWebSocketTask](./urlsession/websockettask%28with%29-87ipz.md)
  Creates a WebSocket task for the provided URL.
- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](./urlsession/websockettask%28with%29-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [func webSocketTask(with: URL, protocols: [String]) -> URLSessionWebSocketTask](./urlsession/websockettask%28with,protocols%29.md)
  Creates a WebSocket task given a URL and an array of protocols.
- [class URLSessionWebSocketTask](./urlsessionwebsockettask.md)
  A URL session task that communicates over the WebSockets protocol standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsocketdelegate)*
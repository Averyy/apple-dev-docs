# webSocketTask(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a WebSocket task for the provided URL.

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
func webSocketTask(with url: URL) -> URLSessionWebSocketTask
```

```objc
- (NSURLSessionWebSocketTask *) webSocketTaskWithURL:(NSURL *) url;
```

#### Discussion

The provided URL must have a `ws` or `wss` scheme.

## Parameters

- `url`: The WebSocket URL with which to connect.

## See Also

### Adding WebSocket tasks to a session
- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](./websockettask%28with%29-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [func webSocketTask(with: URL, protocols: [String]) -> URLSessionWebSocketTask](./websockettask%28with,protocols%29.md)
  Creates a WebSocket task given a URL and an array of protocols.
- [class URLSessionWebSocketTask](../urlsessionwebsockettask.md)
  A URL session task that communicates over the WebSockets protocol standard.
- [protocol URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
- [NSURLSessionWebSocketMessage](../nsurlsessionwebsocketmessage.md)
- [NSURLSessionWebSocketMessageType](../nsurlsessionwebsocketmessagetype.md)
  An enumeration of the types of messages sent and received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:)-87ipz)*
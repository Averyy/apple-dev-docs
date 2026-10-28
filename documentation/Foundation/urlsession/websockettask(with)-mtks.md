# webSocketTask(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a WebSocket task for the provided URL request.

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
func webSocketTask(with request: URLRequest) -> URLSessionWebSocketTask
```

```objc
- (NSURLSessionWebSocketTask *) webSocketTaskWithRequest:(NSURLRequest *) request;
```

## Discussion

You can modify the request’s properties prior to calling [`resume()`](../urlsessiontask/resume%28%29.md) on the task. The task uses these properties during the HTTP handshake phase.

To add custom protocols, add a header with the key `Sec-WebSocket-Protocol`, and a comma-separated list of protocols you want to negotiate with the server. The custom HTTP headers provided by the client remain unchanged for the handshake with the server.

## Parameters

- `request`: A URL request that indicates a WebSockets endpoint with which to connect.

## See Also

### Adding WebSocket tasks to a session
- [func webSocketTask(with: URL) -> URLSessionWebSocketTask](./websockettask%28with%29-87ipz.md)
  Creates a WebSocket task for the provided URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:)-mtks)*
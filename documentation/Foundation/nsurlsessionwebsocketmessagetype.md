# NSURLSessionWebSocketMessageType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the types of messages sent and received.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
enum NSURLSessionWebSocketMessageType : NSInteger;
```

## Topics

### Enumeration Cases
- [NSURLSessionWebSocketMessageTypeData](./nsurlsessionwebsocketmessagetype/nsurlsessionwebsocketmessagetypedata.md)
- [NSURLSessionWebSocketMessageTypeString](./nsurlsessionwebsocketmessagetype/nsurlsessionwebsocketmessagetypestring.md)

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
- [protocol URLSessionWebSocketDelegate](./urlsessionwebsocketdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
- [NSURLSessionWebSocketMessage](./nsurlsessionwebsocketmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlsessionwebsocketmessagetype)*
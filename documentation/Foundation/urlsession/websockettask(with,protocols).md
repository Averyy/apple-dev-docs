# webSocketTask(with:protocols:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a WebSocket task given a URL and an array of protocols.

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
func webSocketTask(with url: URL, protocols: [String]) -> URLSessionWebSocketTask
```

```objc
- (NSURLSessionWebSocketTask *) webSocketTaskWithURL:(NSURL *) url protocols:(NSArray<NSString *> *) protocols;
```

#### Discussion

During the WebSocket handshake, the task uses the provided protocols to negotiate a preferred protocol with the server.

> **Note**:  The protocol doesn’t affect the WebSocket framing. More details on the protocol are available in [RFC 6455, The WebSocket Protocol](https://tools.ietf.org/html/rfc6455).

## Parameters

- `url`: The WebSocket URL with which to connect.
- `protocols`: An array of protocols to negotiate with the server.

## See Also

### Adding WebSocket tasks to a session
- [func webSocketTask(with: URL) -> URLSessionWebSocketTask](./websockettask%28with%29-87ipz.md)
  Creates a WebSocket task for the provided URL.
- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](./websockettask%28with%29-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [class URLSessionWebSocketTask](../urlsessionwebsockettask.md)
  A URL session task that communicates over the WebSockets protocol standard.
- [protocol URLSessionWebSocketDelegate](../urlsessionwebsocketdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.
- [NSURLSessionWebSocketMessage](../nsurlsessionwebsocketmessage.md)
- [NSURLSessionWebSocketMessageType](../nsurlsessionwebsocketmessagetype.md)
  An enumeration of the types of messages sent and received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:protocols:))*
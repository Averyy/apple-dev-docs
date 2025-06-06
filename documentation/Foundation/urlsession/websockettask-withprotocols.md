# webSocketTask(with:protocols:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

During the WebSocket handshake, the task uses the provided protocols to negotiate a preferred protocol with the server.

> **Note**:  The protocol doesn’t affect the WebSocket framing. More details on the protocol are available in [`RFC 6455, The WebSocket Protocol`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6455).

 The protocol doesn’t affect the WebSocket framing. More details on the protocol are available in [`RFC 6455, The WebSocket Protocol`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6455).

## Parameters

- `url`: The WebSocket URL with which to connect.
- `protocols`: An array of protocols to negotiate with the server.

## See Also

- [func webSocketTask(with: URL) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-87ipz.md)
  Creates a WebSocket task for the provided URL.
- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [class URLSessionWebSocketTask](urlsessionwebsockettask.md)
  A URL session task that communicates over the WebSockets protocol standard.
- [protocol URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:protocols:))*
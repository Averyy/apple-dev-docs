# webSocketTask(with:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

The provided URL must have a `ws` or `wss` scheme.

## Parameters

- `url`: The WebSocket URL with which to connect.

## See Also

- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [func webSocketTask(with: URL, protocols: [String]) -> URLSessionWebSocketTask](urlsession/websockettask(with:protocols:).md)
  Creates a WebSocket task given a URL and an array of protocols.
- [class URLSessionWebSocketTask](urlsessionwebsockettask.md)
  A URL session task that communicates over the WebSockets protocol standard.
- [protocol URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/websockettask(with:)-87ipz)*
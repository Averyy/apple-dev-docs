# closeReason

**Framework**: Foundation  
**Kind**: property

A block of data that provides further information about why a connection closed.

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
var closeReason: Data? { get }
```

#### Discussion

The close reason provides further information about why a connection closed, beyond that provided by the [`closeCode`](urlsessionwebsockettask/closecode-swift.property.md). The value of this property isn’t defined by [`RFC 6455`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6455); the endpoints define how it’s used.

You can retrieve the close reason at any time. When the task is not yet closed, this value is [`URLSessionWebSocketTask.CloseCode.invalid`](urlsessionwebsockettask/closecode-swift.enum/invalid.md).

## See Also

- [func cancel(with: URLSessionWebSocketTask.CloseCode, reason: Data?)](urlsessionwebsockettask/cancel(with:reason:).md)
  Sends a close frame with the given close code and optional close reason.
- [var closeCode: URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.property.md)
  A code that indicates the reason a connection closed.
- [URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.enum.md)
  A code that indicates why a WebSocket connection closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closereason)*
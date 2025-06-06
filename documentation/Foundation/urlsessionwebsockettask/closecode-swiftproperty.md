# closeCode

**Framework**: Foundation  
**Kind**: property

A code that indicates the reason a connection closed.

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
var closeCode: URLSessionWebSocketTask.CloseCode { get }
```

#### Discussion

You can retrieve the close code at any time. When the task is not yet closed, this value is [`URLSessionWebSocketTask.CloseCode.invalid`](urlsessionwebsockettask/closecode-swift.enum/invalid.md).

## See Also

- [func cancel(with: URLSessionWebSocketTask.CloseCode, reason: Data?)](urlsessionwebsockettask/cancel(with:reason:).md)
  Sends a close frame with the given close code and optional close reason.
- [URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.enum.md)
  A code that indicates why a WebSocket connection closed.
- [var closeReason: Data?](urlsessionwebsockettask/closereason.md)
  A block of data that provides further information about why a connection closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closecode-swift.property)*
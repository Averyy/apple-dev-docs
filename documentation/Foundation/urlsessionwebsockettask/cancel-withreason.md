# cancel(with:reason:)

**Framework**: Foundation  
**Kind**: method

Sends a close frame with the given close code and optional close reason.

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
func cancel(with closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?)
```

#### Discussion

If you call [`cancel()`](urlsessiontask/cancel().md) on the task instead of this method, it sends a cancellation frame with no close code or reason.

## Parameters

- `closeCode`: A   that indicates the reason for closing the connection.
- `reason`: Optional further information to explain the closing. The value of this parameter is defined by the endpoints, not by the standard.

## See Also

- [var closeCode: URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.property.md)
  A code that indicates the reason a connection closed.
- [URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.enum.md)
  A code that indicates why a WebSocket connection closed.
- [var closeReason: Data?](urlsessionwebsockettask/closereason.md)
  A block of data that provides further information about why a connection closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/cancel(with:reason:))*
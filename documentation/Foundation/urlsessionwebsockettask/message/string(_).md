# URLSessionWebSocketTask.Message.string(_:)

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A WebSocket message that contains a string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case string(String)
```

#### Discussion

The [`URLSessionWebSocketTask`](../../urlsessionwebsockettask.md) uses UTF-8 encoding to send the message’s string.

## See Also

### Message types
- [URLSessionWebSocketTask.Message.data(_:)](./data%28_%29.md)
  A WebSocket message that contains a block of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/message/string(_:))*
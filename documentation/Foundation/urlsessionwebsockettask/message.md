# URLSessionWebSocketTask.Message

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the types of messages sent and received.

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
enum Message
```

## Topics

### Message types
- [URLSessionWebSocketTask.Message.data(_:)](./message/data%28_%29.md)
  A WebSocket message that contains a block of data.
- [URLSessionWebSocketTask.Message.string(_:)](./message/string%28_%29.md)
  A WebSocket message that contains a string.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending and receiving data
- [func send(URLSessionWebSocketTask.Message, completionHandler: ((any Error)?) -> Void)](./send%28_,completionhandler%29.md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [func receive(completionHandler: (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)](./receive%28completionhandler%29.md)
  Reads a WebSocket message once all the frames of the message are available.
- [var maximumMessageSize: Int](./maximummessagesize.md)
  The maximum number of bytes to buffer before the receive call fails with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/message)*
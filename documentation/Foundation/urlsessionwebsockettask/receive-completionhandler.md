# receive(completionHandler:)

**Framework**: Foundation  
**Kind**: method

Reads a WebSocket message once all the frames of the message are available.

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
@preconcurrency
func receive(completionHandler: @escaping (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)
```

#### Discussion

If the task reaches the [`maximumMessageSize`](urlsessionwebsockettask/maximummessagesize.md) while buffering the frames, this call fails with an error.

## Parameters

- `completionHandler`: A closure that receives two parameters: the WebSocket message, and an   that indicates an error encountered while receiving the message. The error is   if no error occurred.

## See Also

- [func send(URLSessionWebSocketTask.Message, completionHandler: ((any Error)?) -> Void)](urlsessionwebsockettask/send(_:completionhandler:).md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [URLSessionWebSocketTask.Message](urlsessionwebsockettask/message.md)
  An enumeration of the types of messages sent and received.
- [var maximumMessageSize: Int](urlsessionwebsockettask/maximummessagesize.md)
  The maximum number of bytes to buffer before the receive call fails with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/receive(completionhandler:))*
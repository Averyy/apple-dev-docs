# receive(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func receive(completionHandler: @escaping @Sendable (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)
```

#### Discussion

If the task reaches the [`maximumMessageSize`](./maximummessagesize.md) while buffering the frames, this call fails with an error.

## Parameters

- `completionHandler`: A closure that receives two parameters: the WebSocket message, and an [`NSError`](../nserror.md) that indicates an error encountered while receiving the message. The error is `nil` if no error occurred.

## See Also

### Sending and receiving data
- [func send(URLSessionWebSocketTask.Message, completionHandler: ((any Error)?) -> Void)](./send%28_,completionhandler%29.md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [URLSessionWebSocketTask.Message](./message.md)
  An enumeration of the types of messages sent and received.
- [var maximumMessageSize: Int](./maximummessagesize.md)
  The maximum number of bytes to buffer before the receive call fails with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/receive(completionhandler:))*
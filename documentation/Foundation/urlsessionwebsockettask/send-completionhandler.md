# send(_:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Sends a WebSocket message, receiving the result in a completion handler.

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
func send(_ message: URLSessionWebSocketTask.Message, completionHandler: @escaping ((any Error)?) -> Void)
```

#### Discussion

If an error occurs while sending the message, any outstanding work also fails.

## Parameters

- `message`: The WebSocket message to send to the other endpoint.
- `completionHandler`: A closure that receives an   that indicates an error encountered while sending, or nil if no error occurred.

## See Also

- [URLSessionWebSocketTask.Message](urlsessionwebsockettask/message.md)
  An enumeration of the types of messages sent and received.
- [func receive(completionHandler: (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)](urlsessionwebsockettask/receive(completionhandler:).md)
  Reads a WebSocket message once all the frames of the message are available.
- [var maximumMessageSize: Int](urlsessionwebsockettask/maximummessagesize.md)
  The maximum number of bytes to buffer before the receive call fails with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/send(_:completionhandler:))*
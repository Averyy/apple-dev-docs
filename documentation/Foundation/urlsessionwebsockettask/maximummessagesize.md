# maximumMessageSize

**Framework**: Foundation  
**Kind**: property

The maximum number of bytes to buffer before the receive call fails with an error.

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
var maximumMessageSize: Int { get set }
```

#### Discussion

This value includes the sum of all bytes from continuation frames. Receive calls will fail once the task reaches this limit.

## See Also

- [func send(URLSessionWebSocketTask.Message, completionHandler: ((any Error)?) -> Void)](urlsessionwebsockettask/send(_:completionhandler:).md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [URLSessionWebSocketTask.Message](urlsessionwebsockettask/message.md)
  An enumeration of the types of messages sent and received.
- [func receive(completionHandler: (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)](urlsessionwebsockettask/receive(completionhandler:).md)
  Reads a WebSocket message once all the frames of the message are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/maximummessagesize)*
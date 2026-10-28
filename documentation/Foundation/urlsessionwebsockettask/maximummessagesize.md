# maximumMessageSize

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSInteger maximumMessageSize;
```

## Discussion

This value includes the sum of all bytes from continuation frames. Receive calls will fail once the task reaches this limit.

## See Also

### Sending and receiving data
- [func send(URLSessionWebSocketTask.Message, completionHandler: ((any Error)?) -> Void)](./send%28_,completionhandler%29.md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [URLSessionWebSocketTask.Message](./message.md)
  An enumeration of the types of messages sent and received.
- [func receive(completionHandler: (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)](./receive%28completionhandler%29.md)
  Reads a WebSocket message once all the frames of the message are available.
- [- sendMessage:completionHandler:](../nsurlsessionwebsockettask/sendmessage_completionhandler_.md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [- receiveMessageWithCompletionHandler:](../nsurlsessionwebsockettask/receivemessagewithcompletionhandler_.md)
  Reads a WebSocket message once all the frames of the message are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/maximummessagesize)*
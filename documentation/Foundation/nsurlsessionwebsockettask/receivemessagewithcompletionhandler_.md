# receiveMessageWithCompletionHandler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Reads a WebSocket message once all the frames of the message are available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (void) receiveMessageWithCompletionHandler:(void (^)(NSURLSessionWebSocketMessage *message, NSError *error)) completionHandler;
```

## Discussion

If the task reaches the [`maximumMessageSize`](../urlsessionwebsockettask/maximummessagesize.md) while buffering the frames, this call fails with an error.

## Parameters

- `completionHandler`: A closure that receives two parameters: the WebSocket message, and an [`NSError`](../nserror.md) that indicates an error encountered while receiving the message. The error is `nil` if no error occurred.

## See Also

### Sending and receiving data
- [- sendMessage:completionHandler:](./sendmessage_completionhandler_.md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [var maximumMessageSize: Int](../urlsessionwebsockettask/maximummessagesize.md)
  The maximum number of bytes to buffer before the receive call fails with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlsessionwebsockettask/receivemessagewithcompletionhandler:)*
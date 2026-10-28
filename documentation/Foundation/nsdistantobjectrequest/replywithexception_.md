# replyWithException:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sends a reply back to the remote object making the distant object request.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) replyWithException:(NSException *) exception;
```

## Discussion

If `exception` is `nil`, the return value of the receiver’s invocation is sent; otherwise, `exception` is sent and is automatically raised when it arrives at its destination.

## Parameters

- `exception`: The exception to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/replywithexception:)*
# requestTimeout

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The timeout interval for outgoing remote messages.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property NSTimeInterval requestTimeout;
```

## Discussion

If a remote message can’t be sent before the timeout, an [`portTimeoutException`](../nsexceptionname/porttimeoutexception.md) is raised. The default timeout is the maximum possible value.

## See Also

### Configuring Instances
- [replyTimeout](./replytimeout.md)
  The timeout interval for replies to outgoing remote messages.
- [independentConversationQueueing](./independentconversationqueueing.md)
  A Boolean value that indicates whether the receiver handles remote messages atomically.
- [- addRequestMode:](./addrequestmode_.md)
  Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests.
- [- removeRequestMode:](./removerequestmode_.md)
  Removes `mode` from the set of run-loop input modes the receiver uses for connection requests.
- [requestModes](./requestmodes-c.property.md)
  The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object.
- [- invalidate](./invalidate.md)
  Invalidates the receiver.
- [valid](./valid.md)
  A Boolean value that indicates whether the receiver is known to be valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/requesttimeout)*
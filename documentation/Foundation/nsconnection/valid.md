# valid

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is known to be valid.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (readonly, getter=isValid) BOOL valid;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver is known to be valid, otherwise [`false`](../../Swift/false.md).

An `NSConnection` object becomes invalid when either of its ports becomes invalid, but only notes that it has become invalid when it tries to send or receive a message. When this happens it posts an [`NSConnectionDidDieNotification`](../nsconnectiondiddienotification.md) to the default notification center.

## See Also

### Related Documentation
- [var isValid: Bool](../port/isvalid.md)
  A Boolean value that indicates whether the receiver is valid.
### Configuring Instances
- [requestTimeout](./requesttimeout.md)
  The timeout interval for outgoing remote messages.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/valid)*
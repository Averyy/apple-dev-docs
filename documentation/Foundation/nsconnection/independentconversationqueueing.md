# independentConversationQueueing

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver handles remote messages atomically.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property BOOL independentConversationQueueing;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver handles remote messages atomically, otherwise [`false`](../../Swift/false.md).

The default is [`false`](../../Swift/false.md). An `NSConnection` object normally forwards remote message to the intended recipients as they come in. See [Configuring a Connection](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/configuring.html#//apple_ref/doc/uid/20000766) for more information.

## See Also

### Configuring Instances
- [requestTimeout](./requesttimeout.md)
  The timeout interval for outgoing remote messages.
- [replyTimeout](./replytimeout.md)
  The timeout interval for replies to outgoing remote messages.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/independentconversationqueueing)*
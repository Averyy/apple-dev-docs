# invalidate

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Invalidates the receiver.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) invalidate;
```

#### Discussion

After withdrawing the ports the receiver has registered with the current run loop, `invalidate` posts an [`NSConnectionDidDieNotification`](../nsconnectiondiddienotification.md) and then invalidates all remote objects and exported local proxies.

## See Also

### Related Documentation
- [func remove(Port, forMode: RunLoop.Mode)](../runloop/remove%28_,formode%29.md)
  Removes a port from the specified input mode of the run loop.
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
- [valid](./valid.md)
  A Boolean value that indicates whether the receiver is known to be valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/invalidate)*
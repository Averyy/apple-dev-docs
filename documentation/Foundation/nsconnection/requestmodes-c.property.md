# requestModes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (copy, readonly) NSArray<NSString *> * requestModes;
```

## Discussion

An array of `NSString` objects that represents the set of request modes the receiver’s receive port is registered for with its [`RunLoop`](../runloop.md) object.

## See Also

### Related Documentation
- [func add(Port, forMode: RunLoop.Mode)](../runloop/add%28_,formode%29-6z982.md)
  Adds a port as an input source to the specified mode of the run loop.
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
- [- invalidate](./invalidate.md)
  Invalidates the receiver.
- [valid](./valid.md)
  A Boolean value that indicates whether the receiver is known to be valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/requestmodes-c.property)*
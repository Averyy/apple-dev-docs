# invalidate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Invalidates the connection.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

#### Discussion

When you call this method, all outstanding reply blocks, error handling blocks, and invalidation blocks are called on the message handling queue. The connection must be invalidated before it is deallocated. After a connection is invalidated, no more messages may be sent or received.

## See Also

### Managing connection state
- [func activate()](./activate%28%29.md)
  Activates the connection.
- [func resume()](./resume%28%29.md)
  Starts or resumes handling of messages on a connection.
- [func suspend()](./suspend%28%29.md)
  Suspends the connection.
- [var interruptionHandler: (() -> Void)?](./interruptionhandler.md)
  An interruption handler that is called if the remote process exits or crashes.
- [var invalidationHandler: (() -> Void)?](./invalidationhandler.md)
  An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [class func current() -> NSXPCConnection?](./current%28%29.md)
  Returns the current connection, in the context of a call to a method on your exported object.
- [func scheduleSendBarrierBlock(() -> Void)](./schedulesendbarrierblock%28_%29.md)
  Add a barrier block to execute on the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/invalidate())*
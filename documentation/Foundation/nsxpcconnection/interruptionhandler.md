# interruptionHandler

**Framework**: Foundation  
**Kind**: property

An interruption handler that is called if the remote process exits or crashes.

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
var interruptionHandler: (() -> Void)? { get set }
```

#### Discussion

It may be possible to re-establish the connection by simply sending another message. The handler is invoked on the same queue as reply messages and other handlers, and it is always executed after any other messages or reply block handlers (except for the invalidation handler).

## See Also

- [func activate()](nsxpcconnection/activate.md)
  Activates the connection.
- [func resume()](nsxpcconnection/resume.md)
  Starts or resumes handling of messages on a connection.
- [func invalidate()](nsxpcconnection/invalidate.md)
  Invalidates the connection.
- [func suspend()](nsxpcconnection/suspend.md)
  Suspends the connection.
- [var invalidationHandler: (() -> Void)?](nsxpcconnection/invalidationhandler.md)
  An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [class func current() -> NSXPCConnection?](nsxpcconnection/current.md)
  Returns the current connection, in the context of a call to a method on your exported object.
- [func scheduleSendBarrierBlock(() -> Void)](nsxpcconnection/schedulesendbarrierblock(_:).md)
  Add a barrier block to execute on the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/interruptionhandler)*
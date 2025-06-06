# activate()

**Framework**: Foundation  
**Kind**: method

Activates the connection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func activate()
```

#### Discussion

Connections start in an inactive state. You must call [`activate()`](nsxpcconnection/activate().md) on a connection before it can send or receive any messages.

Calling [`activate()`](nsxpcconnection/activate().md) on an active connection has no effect.

For backward compatibility reasons, calling [`resume()`](nsxpcconnection/resume().md) on an inactive and otherwise not suspended [`NSXPCConnection`](nsxpcconnection.md) has the same effect as calling [`activate()`](nsxpcconnection/activate().md). For new code, prefer [`activate()`](nsxpcconnection/activate().md).

## See Also

- [func resume()](nsxpcconnection/resume.md)
  Starts or resumes handling of messages on a connection.
- [func invalidate()](nsxpcconnection/invalidate.md)
  Invalidates the connection.
- [func suspend()](nsxpcconnection/suspend.md)
  Suspends the connection.
- [var interruptionHandler: (() -> Void)?](nsxpcconnection/interruptionhandler.md)
  An interruption handler that is called if the remote process exits or crashes.
- [var invalidationHandler: (() -> Void)?](nsxpcconnection/invalidationhandler.md)
  An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [class func current() -> NSXPCConnection?](nsxpcconnection/current.md)
  Returns the current connection, in the context of a call to a method on your exported object.
- [func scheduleSendBarrierBlock(() -> Void)](nsxpcconnection/schedulesendbarrierblock(_:).md)
  Add a barrier block to execute on the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/activate())*
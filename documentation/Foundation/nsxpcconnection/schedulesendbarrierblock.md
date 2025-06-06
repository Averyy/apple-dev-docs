# scheduleSendBarrierBlock(_:)

**Framework**: Foundation  
**Kind**: method

Add a barrier block to execute on the connection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func scheduleSendBarrierBlock(_ block: @escaping () -> Void)
```

#### Discussion

This barrier block runs after any outstanding send commands complete. However, the remote process isn’t guaranteed to receive the sent messages by the time the block executes. If you need to ensure the remote process received a message, wait for a reply from the process.

## Parameters

- `block`: A block or closure to execute. This block takes no parameters and returns no value.

## See Also

- [func activate()](nsxpcconnection/activate.md)
  Activates the connection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/schedulesendbarrierblock(_:))*
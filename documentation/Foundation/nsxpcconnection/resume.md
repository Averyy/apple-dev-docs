# resume()

**Framework**: Foundation  
**Kind**: method

Starts or resumes handling of messages on a connection.

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
func resume()
```

#### Discussion

All connections start suspended. You must resume them before they start processing received messages or sending messages through the [`remoteObjectProxy()`](nsxpcproxycreating/remoteobjectproxy().md) object.

## See Also

- [func activate()](nsxpcconnection/activate.md)
  Activates the connection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/resume())*
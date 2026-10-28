# resume()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) resume;
```

## Discussion

All connections start suspended. You must resume them before they start processing received messages or sending messages through the [`remoteObjectProxy()`](../nsxpcproxycreating/remoteobjectproxy%28%29.md) object.

## See Also

### Managing connection state
- [func activate()](./activate%28%29.md)
  Activates the connection.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates the connection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/resume())*
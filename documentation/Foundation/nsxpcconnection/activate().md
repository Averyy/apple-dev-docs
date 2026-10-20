# activate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) activate;
```

#### Discussion

Connections start in an inactive state. You must call [`activate()`](./activate%28%29.md) on a connection before it can send or receive any messages.

Calling [`activate()`](./activate%28%29.md) on an active connection has no effect.

For backward compatibility reasons, calling [`resume()`](./resume%28%29.md) on an inactive and otherwise not suspended [`NSXPCConnection`](../nsxpcconnection.md) has the same effect as calling [`activate()`](./activate%28%29.md). For new code, prefer [`activate()`](./activate%28%29.md).

## See Also

### Managing connection state
- [func resume()](./resume%28%29.md)
  Starts or resumes handling of messages on a connection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/activate())*
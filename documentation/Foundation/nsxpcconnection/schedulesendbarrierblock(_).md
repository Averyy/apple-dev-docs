# scheduleSendBarrierBlock(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) scheduleSendBarrierBlock:(void (^)()) block;
```

#### Discussion

This barrier block runs after any outstanding send commands complete. However, the remote process isn’t guaranteed to receive the sent messages by the time the block executes. If you need to ensure the remote process received a message, wait for a reply from the process.

## Parameters

- `block`: A block or closure to execute. This block takes no parameters and returns no value.

## See Also

### Managing connection state
- [func activate()](./activate%28%29.md)
  Activates the connection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/schedulesendbarrierblock(_:))*
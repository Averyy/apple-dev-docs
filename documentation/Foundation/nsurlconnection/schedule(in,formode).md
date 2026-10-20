# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Determines the run loop and mode that the connection uses to call methods on its delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) scheduleInRunLoop:(NSRunLoop *) aRunLoop forMode:(NSRunLoopMode) mode;
```

#### Discussion

By default, a connection is scheduled on the current thread in the default mode when it is created. If you create a connection with the [`init(request:delegate:startImmediately:)`](./init%28request,delegate,startimmediately%29.md) method and provide [`false`](../../Swift/false.md) for the `startImmediately` parameter, you can schedule the connection on a different run loop or mode before starting it with the [`start()`](./start%28%29.md) method. You can schedule a connection on multiple run loops and modes, or on the same run loop in multiple modes.

You cannot reschedule a connection after it has started.

It is an error to schedule delegate method calls with both this method and the [`setDelegateQueue(_:)`](./setdelegatequeue%28_%29.md) method.

## Parameters

- `aRunLoop`: The [`RunLoop`](../runloop.md) instance to use when calling delegate methods.
- `mode`: The mode in which to call delegate methods.

## See Also

### Scheduling Delegate Method Calls
- [func setDelegateQueue(OperationQueue?)](./setdelegatequeue%28_%29.md)
  Determines the operation queue that is used to call methods on the connection’s delegate.
- [func unschedule(from: RunLoop, forMode: RunLoop.Mode)](./unschedule%28from,formode%29.md)
  Causes the connection to stop calling delegate methods in the specified run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/schedule(in:formode:))*
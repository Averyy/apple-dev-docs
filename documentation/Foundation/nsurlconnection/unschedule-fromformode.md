# unschedule(from:forMode:)

**Framework**: Foundation  
**Kind**: method

Causes the connection to stop calling delegate methods in the specified run loop and mode.

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
func unschedule(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

#### Discussion

By default, a connection is scheduled on the current thread in the default mode when it is created. If you create a connection with the [`init(request:delegate:startImmediately:)`](nsurlconnection/init(request:delegate:startimmediately:).md) method and provide [`false`](https://developer.apple.com/documentation/Swift/false) for the `startImmediately` parameter, you can instead schedule connection on a different run loop or mode before starting it with the [`start()`](nsurlconnection/start().md) method. You can schedule a connection on multiple run loops and modes, or on the same run loop in multiple modes. Use this method to unschedule the connection from an undesired run loop and mode before starting the connection.

You cannot reschedule a connection after it has started. It is not necessary to unschedule a connection after it has finished.

## Parameters

- `aRunLoop`: The run loop instance to unschedule.
- `mode`: The mode to unschedule.

## See Also

- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](nsurlconnection/schedule(in:formode:).md)
  Determines the run loop and mode that the connection uses to call methods on its delegate.
- [func setDelegateQueue(OperationQueue?)](nsurlconnection/setdelegatequeue(_:).md)
  Determines the operation queue that is used to call methods on the connection’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/unschedule(from:formode:))*
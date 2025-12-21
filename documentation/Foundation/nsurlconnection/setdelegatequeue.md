# setDelegateQueue(_:)

**Framework**: Foundation  
**Kind**: method

Determines the operation queue that is used to call methods on the connection’s delegate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setDelegateQueue(_ queue: OperationQueue?)
```

#### Discussion

By default, a connection is scheduled on the current thread in the default mode when it is created. If you create a connection with the [`init(request:delegate:startImmediately:)`](nsurlconnection/init(request:delegate:startimmediately:).md) method and provide [`false`](https://developer.apple.com/documentation/Swift/false) for the `startImmediately` parameter, you can instead schedule the connection on an operation queue before starting it with the [`start()`](nsurlconnection/start().md) method.

You cannot reschedule a connection after it has started.

It is an error to schedule delegate method calls with both this method and the [`schedule(in:forMode:)`](nsurlconnection/schedule(in:formode:).md) method.

## Parameters

- `queue`: The operation queue to use when calling delegate methods.

## See Also

- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](nsurlconnection/schedule(in:formode:).md)
  Determines the run loop and mode that the connection uses to call methods on its delegate.
- [func unschedule(from: RunLoop, forMode: RunLoop.Mode)](nsurlconnection/unschedule(from:formode:).md)
  Causes the connection to stop calling delegate methods in the specified run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/setdelegatequeue(_:))*
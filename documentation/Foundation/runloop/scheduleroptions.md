# RunLoop.SchedulerOptions

**Framework**: Foundation  
**Kind**: struct

A set of options that affect the operation of the run loop scheduler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct SchedulerOptions
```

#### Overview

The run loop doesn’t support any scheduler options.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func schedule(options: RunLoop.SchedulerOptions?, () -> Void)](runloop/schedule(options:_:).md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void)](runloop/schedule(after:tolerance:options:_:).md)
  Performs the action at some time after the specified date, using the specified tolerance and options.
- [func schedule(after: RunLoop.SchedulerTimeType, interval: RunLoop.SchedulerTimeType.Stride, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void) -> any Cancellable](runloop/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [var minimumTolerance: RunLoop.SchedulerTimeType.Stride](runloop/minimumtolerance.md)
  The minimum tolerance the run loop scheduler allows.
- [var now: RunLoop.SchedulerTimeType](runloop/now.md)
  The run loop scheduler’s definition of the current moment in time.
- [RunLoop.SchedulerTimeType](runloop/schedulertimetype.md)
  The scheduler time type that the run loop uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/scheduleroptions)*
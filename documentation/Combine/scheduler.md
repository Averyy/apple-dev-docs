# Scheduler

**Framework**: Combine  
**Kind**: protocol

A protocol that defines when and how to execute a closure.

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
protocol Scheduler<SchedulerTimeType>
```

## Mentions

- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)

#### Overview

You can use a scheduler to execute code as soon as possible, or after a future date. Individual scheduler implementations use whatever time-keeping system makes sense for them. Schedulers express this as their `SchedulerTimeType`. Since this type conforms to [`SchedulerTimeIntervalConvertible`](schedulertimeintervalconvertible.md), you can always express these times with the convenience functions like `.milliseconds(500)`. Schedulers can accept options to control how they execute the actions passed to them. These options may control factors like which threads or dispatch queues execute the actions.

## Topics

### Declaring scheduler timekeeping and options
- [associatedtype SchedulerTimeType : Strideable](scheduler/schedulertimetype.md)
  Describes an instant in time for this scheduler.
- [associatedtype SchedulerOptions](scheduler/scheduleroptions.md)
  A type that defines options accepted by the scheduler.
### Accessing scheduler time properties
- [var minimumTolerance: Self.SchedulerTimeType.Stride](scheduler/minimumtolerance.md)
  The minimum tolerance allowed by the scheduler.
- [var now: Self.SchedulerTimeType](scheduler/now.md)
  This scheduler’s definition of the current moment in time.
### Scheduling actions
- [func schedule(() -> Void)](scheduler/schedule(_:).md)
  Performs the action at the next possible opportunity, without options.
- [func schedule(after: Self.SchedulerTimeType, () -> Void)](scheduler/schedule(after:_:).md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](scheduler/schedule(after:interval:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, using minimum tolerance possible for this Scheduler.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, () -> Void) -> any Cancellable](scheduler/schedule(after:interval:tolerance:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, interval: Self.SchedulerTimeType.Stride, tolerance: Self.SchedulerTimeType.Stride, options: Self.SchedulerOptions?, () -> Void) -> any Cancellable](scheduler/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, () -> Void)](scheduler/schedule(after:tolerance:_:).md)
  Performs the action at some time after the specified date.
- [func schedule(after: Self.SchedulerTimeType, tolerance: Self.SchedulerTimeType.Stride, options: Self.SchedulerOptions?, () -> Void)](scheduler/schedule(after:tolerance:options:_:).md)
  Performs the action at some time after the specified date.
- [func schedule(options: Self.SchedulerOptions?, () -> Void)](scheduler/schedule(options:_:).md)
  Performs the action at the next possible opportunity.

## Relationships

### Conforming Types
- [ImmediateScheduler](immediatescheduler.md)

## See Also

- [struct ImmediateScheduler](immediatescheduler.md)
  A scheduler for performing synchronous actions.
- [protocol SchedulerTimeIntervalConvertible](schedulertimeintervalconvertible.md)
  A protocol that provides a scheduler with an expression for relative time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/scheduler)*
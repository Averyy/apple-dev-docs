# ImmediateScheduler

**Framework**: Combine  
**Kind**: struct

A scheduler for performing synchronous actions.

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
struct ImmediateScheduler
```

#### Overview

You can only use this scheduler for immediate actions. If you attempt to schedule actions after a specific date, this scheduler ignores the date and performs them immediately.

## Topics

### Declaring scheduler timekeeping and options
- [ImmediateScheduler.SchedulerTimeType](immediatescheduler/schedulertimetype.md)
  The time type used by the immediate scheduler.
- [ImmediateScheduler.SchedulerOptions](immediatescheduler/scheduleroptions.md)
  A type that defines options accepted by the immediate scheduler.
### Accessing scheduler time properties
- [var minimumTolerance: ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/minimumtolerance.md)
  The minimum tolerance allowed by the immediate scheduler.
- [var now: ImmediateScheduler.SchedulerTimeType](immediatescheduler/now.md)
  The immediate scheduler’s definition of the current moment in time.
### Using the shared scheduler
- [static let shared: ImmediateScheduler](immediatescheduler/shared.md)
  The shared instance of the immediate scheduler.
### Scheduling actions
- [func schedule(after: ImmediateScheduler.SchedulerTimeType, interval: ImmediateScheduler.SchedulerTimeType.Stride, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, () -> Void) -> any Cancellable](immediatescheduler/schedule(after:interval:tolerance:options:_:).md)
  Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [func schedule(after: ImmediateScheduler.SchedulerTimeType, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, () -> Void)](immediatescheduler/schedule(after:tolerance:options:_:).md)
  Performs the action at some time after the specified date.
- [func schedule(options: ImmediateScheduler.SchedulerOptions?, () -> Void)](immediatescheduler/schedule(options:_:).md)
  Performs the action at the next possible opportunity.

## Relationships

### Conforms To
- [Scheduler](scheduler.md)

## See Also

- [protocol Scheduler](scheduler.md)
  A protocol that defines when and how to execute a closure.
- [protocol SchedulerTimeIntervalConvertible](schedulertimeintervalconvertible.md)
  A protocol that provides a scheduler with an expression for relative time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler)*
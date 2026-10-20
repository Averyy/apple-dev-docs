# RunLoop.SchedulerTimeType

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The scheduler time type that the run loop uses.

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
struct SchedulerTimeType
```

## Topics

### Creating Scheduler Times
- [init(Date)](./schedulertimetype/init%28_%29.md)
  Initializes a run loop scheduler time with the given date.
### Working with Scheduler Time Intervals
- [RunLoop.SchedulerTimeType.Stride](./schedulertimetype/stride.md)
  The interval by which run loop times advance.
- [func advanced(by: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType](./schedulertimetype/advanced%28by%29.md)
  Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [func distance(to: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride](./schedulertimetype/distance%28to%29.md)
  Returns the distance to another run loop scheduler time.
### Inspecting Properties
- [var date: Date](./schedulertimetype/date.md)
  The date this type represents.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Strideable](../../Swift/strideable.md)

## See Also

### Scheduling Combine Publishers
- [func schedule(options: RunLoop.SchedulerOptions?, () -> Void)](./schedule%28options,_%29.md)
  Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [func schedule(after: RunLoop.SchedulerTimeType, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void)](./schedule%28after,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, using the specified tolerance and options.
- [func schedule(after: RunLoop.SchedulerTimeType, interval: RunLoop.SchedulerTimeType.Stride, tolerance: RunLoop.SchedulerTimeType.Stride, options: RunLoop.SchedulerOptions?, () -> Void) -> any Cancellable](./schedule%28after,interval,tolerance,options,_%29.md)
  Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [var minimumTolerance: RunLoop.SchedulerTimeType.Stride](./minimumtolerance.md)
  The minimum tolerance the run loop scheduler allows.
- [var now: RunLoop.SchedulerTimeType](./now.md)
  The run loop scheduler’s definition of the current moment in time.
- [RunLoop.SchedulerOptions](./scheduleroptions.md)
  A set of options that affect the operation of the run loop scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype)*
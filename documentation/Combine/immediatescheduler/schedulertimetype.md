# ImmediateScheduler.SchedulerTimeType

**Framework**: Combine  
**Kind**: struct

The time type used by the immediate scheduler.

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

### Declaring a Scheduler Timekeeping System
- [ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride.md)
  The increment by which the immediate scheduler counts time.
### Calculating Time Offsets
- [func advanced(by: ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType](immediatescheduler/schedulertimetype/advanced(by:).md)
  Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.
- [func distance(to: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/distance(to:).md)
  Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.
### Comparing Scheduler Times
- [static func != (Self, Self) -> Bool](immediatescheduler/schedulertimetype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func ... (Self) -> PartialRangeFrom<Self>](immediatescheduler/schedulertimetype/'...(_:)-6wy1j.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](immediatescheduler/schedulertimetype/'...(_:)-5ai2g.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](immediatescheduler/schedulertimetype/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func == (Self, Self) -> Bool](immediatescheduler/schedulertimetype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Comparable Implementations](immediatescheduler/schedulertimetype/comparable-implementations.md)
- [Equatable Implementations](immediatescheduler/schedulertimetype/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Strideable](../Swift/Strideable.md)

## See Also

- [ImmediateScheduler.SchedulerOptions](immediatescheduler/scheduleroptions.md)
  A type that defines options accepted by the immediate scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype)*
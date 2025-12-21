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

### Declaring a scheduler timekeeping system
- [ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride.md)
  The increment by which the immediate scheduler counts time.
### Calculating time offsets
- [func advanced(by: ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType](immediatescheduler/schedulertimetype/advanced(by:).md)
  Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.
- [func distance(to: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/distance(to:).md)
  Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.

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
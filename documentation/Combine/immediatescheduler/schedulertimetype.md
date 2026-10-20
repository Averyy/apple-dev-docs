# ImmediateScheduler.SchedulerTimeType

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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
- [ImmediateScheduler.SchedulerTimeType.Stride](./schedulertimetype/stride.md)
  The increment by which the immediate scheduler counts time.
### Calculating time offsets
- [func advanced(by: ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType](./schedulertimetype/advanced%28by%29.md)
  Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.
- [func distance(to: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride](./schedulertimetype/distance%28to%29.md)
  Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Equatable](../../Swift/equatable.md)
- [Strideable](../../Swift/strideable.md)

## See Also

### Declaring scheduler timekeeping and options
- [ImmediateScheduler.SchedulerOptions](./scheduleroptions.md)
  A type that defines options accepted by the immediate scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype)*
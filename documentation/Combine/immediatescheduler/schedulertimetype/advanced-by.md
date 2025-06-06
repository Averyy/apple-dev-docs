# advanced(by:)

**Framework**: Combine  
**Kind**: method

Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.

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
func advanced(by n: ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType
```

#### Return Value

An empty `SchedulerTimeType`.

## Parameters

- `n`: The amount to advance by. The   ignores this value.

## See Also

- [func distance(to: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/distance(to:).md)
  Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/advanced(by:))*
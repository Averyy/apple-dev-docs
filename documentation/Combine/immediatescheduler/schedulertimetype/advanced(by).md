# advanced(by:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

An empty `SchedulerTimeType`.

## Parameters

- `n`: The amount to advance by. The `ImmediateScheduler` ignores this value.

## See Also

### Calculating time offsets
- [func distance(to: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride](./distance%28to%29.md)
  Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/advanced(by:))*
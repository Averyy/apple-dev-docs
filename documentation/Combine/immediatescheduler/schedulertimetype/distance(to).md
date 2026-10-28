# distance(to:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.

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
func distance(to other: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride
```

## Return Value

`0`, as a `Stride`.

## Parameters

- `other`: The other scheduler time.

## See Also

### Calculating time offsets
- [func advanced(by: ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType](./advanced%28by%29.md)
  Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/distance(to:))*
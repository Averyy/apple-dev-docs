# DispatchQueue.SchedulerTimeType

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

The scheduler time type used by the dispatch queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
struct SchedulerTimeType
```

## Topics

### Creating Scheduler Times
- [init(DispatchTime)](./schedulertimetype/init%28_%29.md)
  Creates a dispatch queue time type instance.
### Working with Scheduler Time Intervals
- [func advanced(by: DispatchQueue.SchedulerTimeType.Stride) -> DispatchQueue.SchedulerTimeType](./schedulertimetype/advanced%28by%29.md)
- [func distance(to: DispatchQueue.SchedulerTimeType) -> DispatchQueue.SchedulerTimeType.Stride](./schedulertimetype/distance%28to%29.md)
### Inspecting Scheduler Time Properties
- [var dispatchTime: DispatchTime](./schedulertimetype/dispatchtime.md)
  The dispatch time represented by this type.

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
- [DispatchQueue.SchedulerOptions](./scheduleroptions.md)
  A set of options that affect the operation of the dispatch queue scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/schedulertimetype)*
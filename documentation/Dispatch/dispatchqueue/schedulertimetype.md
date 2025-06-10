# DispatchQueue.SchedulerTimeType

**Framework**: Dispatch  
**Kind**: struct

The scheduler time type used by the dispatch queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
struct SchedulerTimeType
```

## Topics

### Creating Scheduler Times
- [init(DispatchTime)](dispatchqueue/schedulertimetype/init(_:).md)
  Creates a dispatch queue time type instance.
### Working with Scheduler Time Intervals
- [func advanced(by: DispatchQueue.SchedulerTimeType.Stride) -> DispatchQueue.SchedulerTimeType](dispatchqueue/schedulertimetype/advanced(by:).md)
- [func distance(to: DispatchQueue.SchedulerTimeType) -> DispatchQueue.SchedulerTimeType.Stride](dispatchqueue/schedulertimetype/distance(to:).md)
### Inspecting Scheduler Time Properties
- [var dispatchTime: DispatchTime](dispatchqueue/schedulertimetype/dispatchtime.md)
  The dispatch time represented by this type.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Strideable](../Swift/Strideable.md)

## See Also

- [DispatchQueue.SchedulerOptions](dispatchqueue/scheduleroptions.md)
  A set of options that affect the operation of the dispatch queue scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/schedulertimetype)*
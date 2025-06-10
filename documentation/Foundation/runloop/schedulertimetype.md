# RunLoop.SchedulerTimeType

**Framework**: Foundation  
**Kind**: struct

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
- [init(Date)](runloop/schedulertimetype/init(_:).md)
  Initializes a run loop scheduler time with the given date.
### Working with Scheduler Time Intervals
- [RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/stride.md)
  The interval by which run loop times advance.
- [func advanced(by: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType](runloop/schedulertimetype/advanced(by:).md)
  Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [func distance(to: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/distance(to:).md)
  Returns the distance to another run loop scheduler time.
### Inspecting Properties
- [var date: Date](runloop/schedulertimetype/date.md)
  The date this type represents.

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

- [RunLoop.SchedulerOptions](runloop/scheduleroptions.md)
  A set of options that affect the operation of the run loop scheduler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype)*
# RunLoop.SchedulerTimeType.Stride

**Framework**: Foundation  
**Kind**: struct

The interval by which run loop times advance.

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
struct Stride
```

## Topics

### Creating Scheduler Time Strides
- [init(TimeInterval)](runloop/schedulertimetype/stride/init(_:).md)
  Creates a run loop scheduler time interval from the given time interval.
### Inspecting Stride Properties
- [var magnitude: TimeInterval](runloop/schedulertimetype/stride/magnitude.md)
  The value of this time interval in seconds.
- [var timeInterval: TimeInterval](runloop/schedulertimetype/stride/timeinterval.md)
  The value of this time interval in seconds.

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Numeric](../Swift/Numeric.md)
- [SchedulerTimeIntervalConvertible](../Combine/SchedulerTimeIntervalConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SignedNumeric](../Swift/SignedNumeric.md)

## See Also

- [func advanced(by: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType](runloop/schedulertimetype/advanced(by:).md)
  Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
- [func distance(to: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride](runloop/schedulertimetype/distance(to:).md)
  Returns the distance to another run loop scheduler time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/stride)*
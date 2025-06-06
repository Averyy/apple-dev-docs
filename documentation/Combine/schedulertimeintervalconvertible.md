# SchedulerTimeIntervalConvertible

**Framework**: Combine  
**Kind**: protocol

A protocol that provides a scheduler with an expression for relative time.

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
protocol SchedulerTimeIntervalConvertible
```

## Topics

### Converting Seconds to Scheduler Time Intervals
- [static func microseconds(Int) -> Self](schedulertimeintervalconvertible/microseconds(_:).md)
  Converts the specified number of microseconds into an instance of this scheduler time type.
- [static func milliseconds(Int) -> Self](schedulertimeintervalconvertible/milliseconds(_:).md)
  Converts the specified number of milliseconds into an instance of this scheduler time type.
- [static func nanoseconds(Int) -> Self](schedulertimeintervalconvertible/nanoseconds(_:).md)
  Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [static func seconds(Double) -> Self](schedulertimeintervalconvertible/seconds(_:)-2cv8t.md)
  Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [static func seconds(Int) -> Self](schedulertimeintervalconvertible/seconds(_:)-3g8ay.md)
  Converts the specified number of seconds into an instance of this scheduler time type.

## Relationships

### Conforming Types
- [ImmediateScheduler.SchedulerTimeType.Stride](immediatescheduler/schedulertimetype/stride.md)

## See Also

- [protocol Scheduler](scheduler.md)
  A protocol that defines when and how to execute a closure.
- [struct ImmediateScheduler](immediatescheduler.md)
  A scheduler for performing synchronous actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/schedulertimeintervalconvertible)*
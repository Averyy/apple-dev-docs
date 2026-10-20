# DateInterval

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The span of time between a specific start date and end date.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct DateInterval
```

#### Overview

DateInterval represents a closed date interval in the form of [startDate, endDate].  It is possible for the start and end dates to be the same with a duration of 0.  DateInterval does not support reverse intervals i.e. intervals where the duration is less than 0 and the end date occurs earlier in time than the start date.

## Topics

### Creating a Date Interval
- [init()](./dateinterval/init%28%29.md)
  Initializes an interval with start and end dates set to the current date and the duration set to `0`.
- [init(start: Date, duration: TimeInterval)](./dateinterval/init%28start,duration%29.md)
  Initializes an interval with the specified start date and duration.
- [init(start: Date, end: Date)](./dateinterval/init%28start,end%29.md)
  Initializes an interval with the specified start and end date.
### Accessing Start Date, End Date, and Duration
- [var start: Date](./dateinterval/start.md)
  The start date.
- [var end: Date](./dateinterval/end.md)
  The end date.
- [var duration: TimeInterval](./dateinterval/duration.md)
  The duration.
### Determining Intersections
- [func intersection(with: DateInterval) -> DateInterval?](./dateinterval/intersection%28with%29.md)
  Returns an interval that represents the interval where the given date interval and the current instance intersect.
- [func intersects(DateInterval) -> Bool](./dateinterval/intersects%28_%29.md)
  Indicates whether this interval intersects the specified interval.
### Determining Whether a Date Occurs Within a Date Interval
- [func contains(Date) -> Bool](./dateinterval/contains%28_%29.md)
  Indicates whether this interval contains the given date.
### Using Reference Types
- [class NSDateInterval](./nsdateinterval.md)
  An object representing the span of time between a specific start date and end date.
### Instance Methods
- [func compare(DateInterval) -> ComparisonResult](./dateinterval/compare%28_%29.md)
  Compares two intervals.

## Relationships

### Conforms To
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [ReferenceConvertible](./referenceconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Date Representations
- [struct Date](./date.md)
  A specific point in time, independent of any calendar or time zone.
- [typealias TimeInterval](./timeinterval.md)
  A number of seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateinterval)*
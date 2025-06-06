# timeIntervalSinceNow

**Framework**: Foundation  
**Kind**: property

The time interval between the date value and the current date and time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeIntervalSinceNow: TimeInterval { get }
```

#### Discussion

If the date is earlier than the current date and time, this property’s value is negative.

## See Also

- [func timeIntervalSince(Date) -> TimeInterval](date/timeintervalsince(_:).md)
  Returns the interval between this date and another given date.
- [var timeIntervalSinceReferenceDate: TimeInterval](date/timeintervalsincereferencedate-swift.property.md)
  The interval between the date value and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](date/timeintervalsince1970.md)
  The interval between the date value and 00:00:00 UTC on 1 January 1970.
- [static var timeIntervalSinceReferenceDate: TimeInterval](date/timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [static let timeIntervalBetween1970AndReferenceDate: Double](date/timeintervalbetween1970andreferencedate.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/timeintervalsincenow)*
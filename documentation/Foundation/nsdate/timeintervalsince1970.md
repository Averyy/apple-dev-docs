# timeIntervalSince1970

**Framework**: Foundation  
**Kind**: property

The interval between the date object and 00:00:00 UTC on 1 January 1970.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeIntervalSince1970: TimeInterval { get }
```

#### Discussion

This property’s value is negative if the date object is earlier than 00:00:00 UTC on 1 January 1970.

## See Also

- [func timeIntervalSince(Date) -> TimeInterval](nsdate/timeintervalsince(_:).md)
  Returns the interval between the receiver and another given date.
- [var timeIntervalSinceNow: TimeInterval](nsdate/timeintervalsincenow.md)
  The interval between the date object and the current date and time.
- [var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.property.md)
  The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [class var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [var NSTimeIntervalSince1970: Double](nstimeintervalsince1970.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/timeintervalsince1970)*
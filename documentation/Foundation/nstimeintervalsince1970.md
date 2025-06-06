# NSTimeIntervalSince1970

**Framework**: Foundation  
**Kind**: var

The number of seconds from 1 January 1970 to the reference date, 1 January 2001.

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
var NSTimeIntervalSince1970: Double { get }
```

#### Discussion

1 January 1970 is the epoch (or starting point) for Unix time.

## See Also

- [func timeIntervalSince(Date) -> TimeInterval](nsdate/timeintervalsince(_:).md)
  Returns the interval between the receiver and another given date.
- [var timeIntervalSinceNow: TimeInterval](nsdate/timeintervalsincenow.md)
  The interval between the date object and the current date and time.
- [var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.property.md)
  The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](nsdate/timeintervalsince1970.md)
  The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [class var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimeintervalsince1970)*
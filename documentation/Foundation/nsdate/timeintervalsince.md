# timeIntervalSince(_:)

**Framework**: Foundation  
**Kind**: method

Returns the interval between the receiver and another given date.

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
func timeIntervalSince(_ anotherDate: Date) -> TimeInterval
```

#### Return Value

The interval between the receiver and the `anotherDate` parameter. If the receiver is earlier than `anotherDate`, the return value is negative. If `anotherDate` is `nil`, the results are undefined.

## Parameters

- `anotherDate`: The date with which to compare the receiver. You must pass a non-  date object.

## See Also

- [var timeIntervalSinceNow: TimeInterval](nsdate/timeintervalsincenow.md)
  The interval between the date object and the current date and time.
- [var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.property.md)
  The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](nsdate/timeintervalsince1970.md)
  The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [class var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [var NSTimeIntervalSince1970: Double](nstimeintervalsince1970.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/timeintervalsince(_:))*
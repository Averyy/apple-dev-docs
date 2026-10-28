# timeIntervalSinceNow

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The interval between the date object and the current date and time.

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
var timeIntervalSinceNow: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval timeIntervalSinceNow;
```

## Discussion

If the date object is earlier than the current date and time, this property’s value is negative.

## See Also

### Getting Time Intervals
- [func timeIntervalSince(Date) -> TimeInterval](./timeintervalsince%28_%29.md)
  Returns the interval between the receiver and another given date.
- [var timeIntervalSinceReferenceDate: TimeInterval](./timeintervalsincereferencedate-swift.property.md)
  The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](./timeintervalsince1970.md)
  The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [class var timeIntervalSinceReferenceDate: TimeInterval](./timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [var NSTimeIntervalSince1970: Double](../nstimeintervalsince1970.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/timeintervalsincenow)*
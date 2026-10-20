# timeIntervalSinceReferenceDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.

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
class var timeIntervalSinceReferenceDate: TimeInterval { get }
```

```objc
@property (class, readonly) NSTimeInterval timeIntervalSinceReferenceDate;
```

#### Return Value

The interval between the system’s absolute reference date (00:00:00 UTC on 1 January 2001) and the current date and time.

#### Discussion

This method is the primitive method for [`NSDate`](../nsdate.md). If you subclass [`NSDate`](../nsdate.md), you must override this method with your own implementation for it.

## See Also

### Getting Time Intervals
- [func timeIntervalSince(Date) -> TimeInterval](./timeintervalsince%28_%29.md)
  Returns the interval between the receiver and another given date.
- [var timeIntervalSinceNow: TimeInterval](./timeintervalsincenow.md)
  The interval between the date object and the current date and time.
- [var timeIntervalSinceReferenceDate: TimeInterval](./timeintervalsincereferencedate-swift.property.md)
  The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](./timeintervalsince1970.md)
  The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [var NSTimeIntervalSince1970: Double](../nstimeintervalsince1970.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/timeintervalsincereferencedate-swift.type.property)*
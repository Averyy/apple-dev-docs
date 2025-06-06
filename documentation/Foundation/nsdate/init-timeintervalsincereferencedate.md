# init(timeIntervalSinceReferenceDate:)

**Framework**: Foundation  
**Kind**: init

Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.

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
init(timeIntervalSinceReferenceDate ti: TimeInterval)
```

#### Return Value

An `NSDate` object initialized relative to the absolute reference date by `ti` seconds.

#### Discussion

This method is a designated initializer for the `NSDate` class and is declared primarily for the use of subclasses of `NSDate`. When you subclass `NSDate` to create a concrete date class, you must override this method.

## Parameters

- `ti`: The number of seconds to add to the reference date (00:00:00 UTC on 1 January 2001). A negative value means the receiver will be earlier than the reference date.

## See Also

- [init()](nsdate/init.md)
  Returns a date object initialized to the current date and time.
- [convenience init(timeIntervalSinceNow: TimeInterval)](nsdate/init(timeintervalsincenow:).md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
- [convenience init(timeInterval: TimeInterval, sinceDate: Date)](nsdate/init(timeinterval:sincedate:)-71m1f.md)
  Returns a date object initialized relative to another given date by a given number of seconds.
- [convenience init(timeIntervalSince1970: TimeInterval)](nsdate/init(timeintervalsince1970:).md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [init?(coder: NSCoder)](nsdate/init(coder:).md)
  Returns a date object initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(timeintervalsincereferencedate:))*
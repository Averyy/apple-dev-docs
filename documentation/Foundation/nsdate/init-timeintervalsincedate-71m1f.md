# init(timeInterval:sinceDate:)

**Framework**: Foundation  
**Kind**: init

Returns a date object initialized relative to another given date by a given number of seconds.

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
convenience init(timeInterval secsToBeAdded: TimeInterval, since date: Date)
```

#### Return Value

An `NSDate` object initialized relative to `date` by `secsToBeAdded` seconds.

## Parameters

- `secsToBeAdded`: The number of seconds to add to  . A negative value means the receiver will be earlier than  .
- `date`: The reference date.

## See Also

- [init()](nsdate/init.md)
  Returns a date object initialized to the current date and time.
- [convenience init(timeIntervalSinceNow: TimeInterval)](nsdate/init(timeintervalsincenow:).md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](nsdate/init(timeintervalsincereferencedate:).md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [convenience init(timeIntervalSince1970: TimeInterval)](nsdate/init(timeintervalsince1970:).md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [init?(coder: NSCoder)](nsdate/init(coder:).md)
  Returns a date object initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(timeinterval:sincedate:)-71m1f)*
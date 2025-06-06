# init(timeIntervalSince1970:)

**Framework**: Foundation  
**Kind**: init

Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.

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
convenience init(timeIntervalSince1970 secs: TimeInterval)
```

#### Return Value

An `NSDate` object set to `seconds` seconds from the reference date.

#### Discussion

This method is useful for creating `NSDate` objects from time_t values returned by BSD system functions.

## Parameters

- `secs`: The number of seconds from the reference date (00:00:00 UTC on 1 January 1970) for the new date. Use a negative argument to specify a date and time before the reference date.

## See Also

- [init()](nsdate/init.md)
  Returns a date object initialized to the current date and time.
- [convenience init(timeIntervalSinceNow: TimeInterval)](nsdate/init(timeintervalsincenow:).md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
- [convenience init(timeInterval: TimeInterval, sinceDate: Date)](nsdate/init(timeinterval:sincedate:)-71m1f.md)
  Returns a date object initialized relative to another given date by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](nsdate/init(timeintervalsincereferencedate:).md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [init?(coder: NSCoder)](nsdate/init(coder:).md)
  Returns a date object initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(timeintervalsince1970:))*
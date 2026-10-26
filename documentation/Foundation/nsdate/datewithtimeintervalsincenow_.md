# dateWithTimeIntervalSinceNow:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a date object set to a given number of seconds from the current date and time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dateWithTimeIntervalSinceNow:(NSTimeInterval) secs;
```

#### Return Value

An `NSDate` object set to `secs` seconds from the current date and time.

## Parameters

- `secs`: The number of seconds from the current date and time for the new date. Use a negative value to specify a date before the current date.

## See Also

### Related Documentation
- [convenience init(timeIntervalSinceNow: TimeInterval)](./init%28timeintervalsincenow%29.md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
### Creating a Date
- [+ date](./date.md)
  Creates and returns a new date object set to the current date and time.
- [+ dateWithTimeIntervalSinceReferenceDate:](./datewithtimeintervalsincereferencedate_.md)
  Creates and returns a date object set to a given number of seconds from 00:00:00 UTC on 1 January 2001.
- [+ dateWithTimeIntervalSince1970:](./datewithtimeintervalsince1970_.md)
  Creates and returns a date object set to the given number of seconds from 00:00:00 UTC on 1 January 1970.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/datewithtimeintervalsincenow:)*
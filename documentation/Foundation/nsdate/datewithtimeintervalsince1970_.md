# dateWithTimeIntervalSince1970:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a date object set to the given number of seconds from 00:00:00 UTC on 1 January 1970.

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
+ (instancetype) dateWithTimeIntervalSince1970:(NSTimeInterval) secs;
```

#### Return Value

An `NSDate` object set to `secs` seconds from the reference date.

#### Discussion

This method is useful for creating `NSDate` objects from time_t values returned by BSD system functions.

## Parameters

- `secs`: The number of seconds from the reference date (00:00:00 UTC on 1 January 1970) for the new date. Use a negative argument to specify a date and time before the reference date.

## See Also

### Related Documentation
- [var timeIntervalSince1970: TimeInterval](./timeintervalsince1970.md)
  The interval between the date object and 00:00:00 UTC on 1 January 1970.
### Creating a Date
- [+ date](./date.md)
  Creates and returns a new date object set to the current date and time.
- [+ dateWithTimeIntervalSinceNow:](./datewithtimeintervalsincenow_.md)
  Creates and returns a date object set to a given number of seconds from the current date and time.
- [+ dateWithTimeIntervalSinceReferenceDate:](./datewithtimeintervalsincereferencedate_.md)
  Creates and returns a date object set to a given number of seconds from 00:00:00 UTC on 1 January 2001.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/datewithtimeintervalsince1970:)*
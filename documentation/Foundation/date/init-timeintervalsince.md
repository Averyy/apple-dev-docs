# init(timeInterval:since:)

**Framework**: Foundation  
**Kind**: init

Creates a date value initialized relative to another given date by a given number of seconds.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(timeInterval: TimeInterval, since date: Date)
```

## Parameters

- `timeInterval`: The number of seconds to add to  . A negative value means the receiver will be earlier than  .
- `date`: The reference date.

## See Also

- [init()](date/init.md)
  Creates a date value initialized to the current date and time.
- [init(timeIntervalSinceNow: TimeInterval)](date/init(timeintervalsincenow:).md)
  Creates a date value initialized relative to the current date and time by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](date/init(timeintervalsincereferencedate:).md)
  Creates a date value initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [init(timeIntervalSince1970: TimeInterval)](date/init(timeintervalsince1970:).md)
  Creates a date value initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/init(timeinterval:since:))*
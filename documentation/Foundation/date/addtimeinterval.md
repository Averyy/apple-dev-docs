# addTimeInterval(_:)

**Framework**: Foundation  
**Kind**: method

Adds a time interval to this date.

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
mutating func addTimeInterval(_ timeInterval: TimeInterval)
```

#### Discussion

> ⚠️ **Warning**:  This only adjusts an absolute value. If you wish to add calendrical concepts like hours, days, months then you must use a `Calendar`. That will take into account complexities like daylight saving time, months with different numbers of days, and more.

 This only adjusts an absolute value. If you wish to add calendrical concepts like hours, days, months then you must use a `Calendar`. That will take into account complexities like daylight saving time, months with different numbers of days, and more.

## Parameters

- `timeInterval`: The value to add, in seconds.

## See Also

- [func addingTimeInterval(TimeInterval) -> Date](date/addingtimeinterval(_:).md)
  Creates a new date value by adding a time interval to this date.
- [static func + (Date, TimeInterval) -> Date](date/+(_:_:).md)
  Returns a date with a specified amount of time added to it.
- [static func += (inout Date, TimeInterval)](date/+=(_:_:).md)
  Adds a time interval to a date.
- [static func - (Date, TimeInterval) -> Date](date/-(_:_:).md)
  Returns a `Date` with a specified amount of time subtracted from it.
- [static func -= (inout Date, TimeInterval)](date/-=(_:_:).md)
  Subtract a `TimeInterval` from a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/addtimeinterval(_:))*
# addTimeInterval(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

## Parameters

- `timeInterval`: The value to add, in seconds.

## See Also

### Adding or Subtracting a Time Interval
- [func addingTimeInterval(TimeInterval) -> Date](./addingtimeinterval%28_%29.md)
  Creates a new date value by adding a time interval to this date.
- [func advanced(by: TimeInterval) -> Date](./advanced%28by%29.md)
  Returns a date offset the specified time interval from this date.
- [static func + (Date, TimeInterval) -> Date](./plus%28_,_%29.md)
  Returns a date with a specified amount of time added to it.
- [static func += (inout Date, TimeInterval)](./pluseq%28_,_%29.md)
  Adds a time interval to a date.
- [static func - (Date, TimeInterval) -> Date](./minus%28_,_%29.md)
  Returns a `Date` with a specified amount of time subtracted from it.
- [static func -= (inout Date, TimeInterval)](./minuseq%28_,_%29.md)
  Subtract a `TimeInterval` from a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/addtimeinterval(_:))*
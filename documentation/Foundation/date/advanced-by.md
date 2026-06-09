# advanced(by:)

**Framework**: Foundation  
**Kind**: method

Returns a date offset the specified time interval from this date.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func advanced(by n: TimeInterval) -> Date
```

#### Return Value

A date offset the specified time interval from this date.

## Parameters

- `n`: The time interval offset.

## See Also

- [func addTimeInterval(TimeInterval)](date/addtimeinterval(_:).md)
  Adds a time interval to this date.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/advanced(by:))*
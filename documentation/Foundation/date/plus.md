# +(_:_:)

**Framework**: Foundation  
**Kind**: op

Returns a date with a specified amount of time added to it.

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
static func + (lhs: Date, rhs: TimeInterval) -> Date
```

#### Return Value

A date with a specified amount of time added to it.

## Parameters

- `lhs`: A date.
- `rhs`: A [`TimeInterval`](timeinterval.md) to add to the date.

## See Also

- [func addTimeInterval(TimeInterval)](date/addtimeinterval(_:).md)
  Adds a time interval to this date.
- [func addingTimeInterval(TimeInterval) -> Date](date/addingtimeinterval(_:).md)
  Creates a new date value by adding a time interval to this date.
- [static func += (inout Date, TimeInterval)](date/+=(_:_:).md)
  Adds a time interval to a date.
- [static func - (Date, TimeInterval) -> Date](date/-(_:_:).md)
  Returns a `Date` with a specified amount of time subtracted from it.
- [static func -= (inout Date, TimeInterval)](date/-=(_:_:).md)
  Subtract a `TimeInterval` from a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/+(_:_:))*
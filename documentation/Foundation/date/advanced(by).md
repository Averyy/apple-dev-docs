# advanced(by:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

### Adding or Subtracting a Time Interval
- [func addTimeInterval(TimeInterval)](./addtimeinterval%28_%29.md)
  Adds a time interval to this date.
- [func addingTimeInterval(TimeInterval) -> Date](./addingtimeinterval%28_%29.md)
  Creates a new date value by adding a time interval to this date.
- [static func + (Date, TimeInterval) -> Date](./plus%28_,_%29.md)
  Returns a date with a specified amount of time added to it.
- [static func += (inout Date, TimeInterval)](./pluseq%28_,_%29.md)
  Adds a time interval to a date.
- [static func - (Date, TimeInterval) -> Date](./minus%28_,_%29.md)
  Returns a `Date` with a specified amount of time subtracted from it.
- [static func -= (inout Date, TimeInterval)](./minuseq%28_,_%29.md)
  Subtract a `TimeInterval` from a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/advanced(by:))*
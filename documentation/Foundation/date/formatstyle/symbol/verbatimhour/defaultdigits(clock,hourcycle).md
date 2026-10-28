# defaultDigits(clock:hourCycle:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a custom format style portraying the minimum number of digits that represents the hour.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func defaultDigits(clock: Date.FormatStyle.Symbol.VerbatimHour.Clock, hourCycle: Date.FormatStyle.Symbol.VerbatimHour.HourCycle) -> Date.FormatStyle.Symbol.VerbatimHour
```

## Return Value

An hour format style customized according to the specified clock representation and the start of the clock representation.

## Parameters

- `clock`: The clock representation.
- `hourCycle`: The start of the clock representation.

## See Also

### Modifying a Verbatim Hour
- [static func twoDigits(clock: Date.FormatStyle.Symbol.VerbatimHour.Clock, hourCycle: Date.FormatStyle.Symbol.VerbatimHour.HourCycle) -> Date.FormatStyle.Symbol.VerbatimHour](./twodigits%28clock,hourcycle%29.md)
  Creates a custom format style portraying two digits that represent the hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/verbatimhour/defaultdigits(clock:hourcycle:))*
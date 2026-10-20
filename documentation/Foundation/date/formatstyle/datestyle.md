# Date.FormatStyle.DateStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Type that defines date styles varied in length or components included.

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
struct DateStyle
```

#### Overview

The exact format depends on the locale. Possible values of date style include [`omitted`](./datestyle/omitted.md), [`numeric`](./datestyle/numeric.md), [`abbreviated`](./datestyle/abbreviated.md), [`long`](./datestyle/long.md), and [`complete`](./datestyle/complete.md).

The following code sample shows a variety of date style format results using the `en_US` locale.

```swift
let meetingDate = Date()
meetingDate.formatted(date: .omitted, time: .standard) 
// 9:42:14 AM

meetingDate.formatted(date: .numeric, time: .omitted) 
// 10/17/2020

meetingDate.formatted(date: .abbreviated, time: .omitted)
// Oct 17, 2020

meetingDate.formatted(date: .long, time: .omitted) 
// October 17, 2020

meetingDate.formatted(date: .complete, time: .omitted) 
// Saturday, October 17, 2020

meetingDate.formatted()
// 10/17/2020, 9:42 AM
```

The default date style is `numeric`.

## Topics

### Modifying a Date Style
- [static let abbreviated: Date.FormatStyle.DateStyle](./datestyle/abbreviated.md)
  A date style with some components abbreviated for space-constrained applications.
- [static let complete: Date.FormatStyle.DateStyle](./datestyle/complete.md)
  A date style with all components represented.
- [static let long: Date.FormatStyle.DateStyle](./datestyle/long.md)
  A lengthened date style with the full month, day of month, and year components represented.
- [static let numeric: Date.FormatStyle.DateStyle](./datestyle/numeric.md)
  A date style with the month, day of month, and year components represented as numeric values.
- [static let omitted: Date.FormatStyle.DateStyle](./datestyle/omitted.md)
  A date style with no date-related components represented.
### Comparing Date Styles
- [static func == (Date, Date) -> Bool](../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Specifying the Date Format
- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle](./day%28_%29.md)
  Modifies the date format style to use the specified day format style.
- [func dayOfYear(Date.FormatStyle.Symbol.DayOfYear) -> Date.FormatStyle](./dayofyear%28_%29.md)
  Modifies the date format style to use the specified day of the year format style.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle](./era%28_%29.md)
  Modifies the date format style to use the specified era format style.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle](./month%28_%29.md)
  Modifies the date format style to use the specified month format style.
- [func quarter(Date.FormatStyle.Symbol.Quarter) -> Date.FormatStyle](./quarter%28_%29.md)
  Modifies the date format style to use the specified quarter format style.
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle](./week%28_%29.md)
  Modifies the date format style to use the specified week format style.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle](./weekday%28_%29.md)
  Modifies the date format style to use the specified weekday format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](./year%28_%29.md)
  Modifies the date format style to use the specified year format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle)*
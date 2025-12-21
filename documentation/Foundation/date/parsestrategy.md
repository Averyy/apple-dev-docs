# Date.ParseStrategy

**Framework**: Foundation  
**Kind**: struct

Options for parsing string representations of dates to create a `Date` instance.

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
struct ParseStrategy
```

## Topics

### Initializers
- [init(format: Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar, isLenient: Bool, twoDigitStartDate: Date)](date/parsestrategy/init(format:locale:timezone:calendar:islenient:twodigitstartdate:).md)
  Creates a new `ParseStrategy` with the given configurations.
### Instance Properties
- [var calendar: Calendar](date/parsestrategy/calendar.md)
  The calendar to use when parsing date strings and creating the date.
- [var format: String](date/parsestrategy/format.md)
  The string representation of the fixed format conforming to Unicode Technical Standard #35.
- [var isLenient: Bool](date/parsestrategy/islenient.md)
  Indicates whether to use heuristics when parsing the representation.
- [var locale: Locale?](date/parsestrategy/locale.md)
  The locale to use when parsing date strings with the specified format. Use system locale if unspecified.
- [var timeZone: TimeZone](date/parsestrategy/timezone.md)
  The time zone to use for creating the date.
- [var twoDigitStartDate: Date](date/parsestrategy/twodigitstartdate.md)
  The earliest date that can be denoted by a two-digit year specifier.
### Default Implementations
- [ParseStrategy Implementations](date/parsestrategy/parsestrategy-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomConsumingRegexComponent](../Swift/CustomConsumingRegexComponent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ParseStrategy](parsestrategy.md)
- [RegexComponent](../Swift/RegexComponent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/parsestrategy)*
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
- [CustomConsumingRegexComponent Implementations](date/parsestrategy/customconsumingregexcomponent-implementations.md)
- [ParseStrategy Implementations](date/parsestrategy/parsestrategy-implementations.md)
- [RegexComponent Implementations](date/parsestrategy/regexcomponent-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomConsumingRegexComponent](../swift/customconsumingregexcomponent.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [ParseStrategy](parsestrategy.md)
- [RegexComponent](../swift/regexcomponent.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func parse(String) throws -> Date](date/formatstyle/parse(_:).md)
  Parses a string into a date.
- [var parseStrategy: Date.FormatStyle](date/formatstyle/parsestrategy.md)
  The strategy used to parse a string into a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/parsestrategy)*
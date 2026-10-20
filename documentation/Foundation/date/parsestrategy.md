# Date.ParseStrategy

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(format: Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar, isLenient: Bool, twoDigitStartDate: Date)](./parsestrategy/init%28format,locale,timezone,calendar,islenient,twodigitstartdate%29.md)
  Creates a new `ParseStrategy` with the given configurations.
### Instance Properties
- [var calendar: Calendar](./parsestrategy/calendar.md)
  The calendar to use when parsing date strings and creating the date.
- [var format: String](./parsestrategy/format.md)
  The string representation of the fixed format conforming to Unicode Technical Standard #35.
- [var isLenient: Bool](./parsestrategy/islenient.md)
  Indicates whether to use heuristics when parsing the representation.
- [var locale: Locale?](./parsestrategy/locale.md)
  The locale to use when parsing date strings with the specified format. Use system locale if unspecified.
- [var timeZone: TimeZone](./parsestrategy/timezone.md)
  The time zone to use for creating the date.
- [var twoDigitStartDate: Date](./parsestrategy/twodigitstartdate.md)
  The earliest date that can be denoted by a two-digit year specifier.
### Default Implementations
- [CustomConsumingRegexComponent Implementations](./parsestrategy/customconsumingregexcomponent-implementations.md)
- [ParseStrategy Implementations](./parsestrategy/parsestrategy-implementations.md)
- [RegexComponent Implementations](./parsestrategy/regexcomponent-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomConsumingRegexComponent](../../Swift/customconsumingregexcomponent.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [ParseStrategy](../parsestrategy.md)
- [RegexComponent](../../Swift/regexcomponent.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Parsing Dates
- [func parse(String) throws -> Date](./formatstyle/parse%28_%29.md)
  Parses a string into a date.
- [var parseStrategy: Date.FormatStyle](./formatstyle/parsestrategy.md)
  The strategy used to parse a string into a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/parsestrategy)*
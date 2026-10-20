# DateComponents.ISO8601FormatStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options for generating and parsing string representations of dates following the ISO 8601 standard.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ISO8601FormatStyle
```

## Topics

### Initializers
- [init(dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator, includingFractionalSeconds: Bool, timeZone: TimeZone)](./iso8601formatstyle/init%28dateseparator,datetimeseparator,timeseparator,timezoneseparator,includingfractionalseconds,timezone%29.md)
### Instance Properties
- [var dateSeparator: Date.ISO8601FormatStyle.DateSeparator](./iso8601formatstyle/dateseparator.md)
- [var dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator](./iso8601formatstyle/datetimeseparator.md)
- [var includingFractionalSeconds: Bool](./iso8601formatstyle/includingfractionalseconds.md)
  If set, fractional seconds will be present in formatted output. Fractional seconds may be present in parsing regardless of the setting of this property.
- [var timeSeparator: Date.ISO8601FormatStyle.TimeSeparator](./iso8601formatstyle/timeseparator.md)
- [var timeZone: TimeZone](./iso8601formatstyle/timezone.md)
  The time zone to use to create and parse date representations.
- [var timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator](./iso8601formatstyle/timezoneseparator.md)
### Instance Methods
- [func dateSeparator(Date.ISO8601FormatStyle.DateSeparator) -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/dateseparator%28_%29.md)
- [func dateTimeSeparator(Date.ISO8601FormatStyle.DateTimeSeparator) -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/datetimeseparator%28_%29.md)
- [func day() -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/day%28%29.md)
- [func month() -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/month%28%29.md)
- [func time(includingFractionalSeconds: Bool) -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/time%28includingfractionalseconds%29.md)
- [func timeSeparator(Date.ISO8601FormatStyle.TimeSeparator) -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/timeseparator%28_%29.md)
- [func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/timezone%28separator%29.md)
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/timezoneseparator%28_%29.md)
- [func weekOfYear() -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/weekofyear%28%29.md)
- [func year() -> DateComponents.ISO8601FormatStyle](./iso8601formatstyle/year%28%29.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomConsumingRegexComponent](../../Swift/customconsumingregexcomponent.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [FormatStyle](../formatstyle.md)
- [Hashable](../../Swift/hashable.md)
- [ParseStrategy](../parsestrategy.md)
- [ParseableFormatStyle](../parseableformatstyle.md)
- [RegexComponent](../../Swift/regexcomponent.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/iso8601formatstyle)*
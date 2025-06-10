# DateComponents.ISO8601FormatStyle

**Framework**: Foundation  
**Kind**: struct

Options for generating and parsing string representations of dates following the ISO 8601 standard.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct ISO8601FormatStyle
```

## Topics

### Initializers
- [init(dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator, includingFractionalSeconds: Bool, timeZone: TimeZone)](datecomponents/iso8601formatstyle/init(dateseparator:datetimeseparator:timeseparator:timezoneseparator:includingfractionalseconds:timezone:).md)
### Instance Properties
- [var dateSeparator: Date.ISO8601FormatStyle.DateSeparator](datecomponents/iso8601formatstyle/dateseparator.md)
- [var dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator](datecomponents/iso8601formatstyle/datetimeseparator.md)
- [var includingFractionalSeconds: Bool](datecomponents/iso8601formatstyle/includingfractionalseconds.md)
  If set, fractional seconds will be present in formatted output. Fractional seconds may be present in parsing regardless of the setting of this property.
- [var timeSeparator: Date.ISO8601FormatStyle.TimeSeparator](datecomponents/iso8601formatstyle/timeseparator.md)
- [var timeZone: TimeZone](datecomponents/iso8601formatstyle/timezone.md)
  The time zone to use to create and parse date representations.
- [var timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator](datecomponents/iso8601formatstyle/timezoneseparator.md)
### Instance Methods
- [func dateSeparator(Date.ISO8601FormatStyle.DateSeparator) -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/dateseparator(_:).md)
- [func dateTimeSeparator(Date.ISO8601FormatStyle.DateTimeSeparator) -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/datetimeseparator(_:).md)
- [func day() -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/day.md)
- [func month() -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/month.md)
- [func time(includingFractionalSeconds: Bool) -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/time(includingfractionalseconds:).md)
- [func timeSeparator(Date.ISO8601FormatStyle.TimeSeparator) -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/timeseparator(_:).md)
- [func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/timezone(separator:).md)
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/timezoneseparator(_:).md)
- [func weekOfYear() -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/weekofyear.md)
- [func year() -> DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle/year.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomConsumingRegexComponent](../Swift/CustomConsumingRegexComponent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [ParseStrategy](parsestrategy.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [RegexComponent](../Swift/RegexComponent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/iso8601formatstyle)*
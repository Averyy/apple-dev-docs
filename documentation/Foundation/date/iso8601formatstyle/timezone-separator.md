# timeZone(separator:)

**Framework**: Foundation  
**Kind**: method

Modifies the ISO 8601 date format style to include the time zone in the formatted output.

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
func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle
```

#### Return Value

An ISO 8601 date format style modified to include the time zone.

#### Discussion

The default [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md) doesn’t include the time zone.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `separator`: Character used to separate the time and time zone in a date.

## See Also

- [func time(includingFractionalSeconds: Bool) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/time(includingfractionalseconds:).md)
  Modifies the ISO 8601 date format style to include the time in the formatted output.
- [func timeSeparator(Date.ISO8601FormatStyle.TimeSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timeseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time separator.
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezoneseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time zone separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/timezone(separator:))*
# timeZone(separator:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

The default [`Date.ISO8601FormatStyle`](../iso8601formatstyle.md) doesn’t include the time zone.

For more information about formatting dates, see the [`Date.FormatStyle`](../formatstyle.md).

## Parameters

- `separator`: Character used to separate the time and time zone in a date.

## See Also

### Modifying Times in an ISO 8601 Format Style
- [func time(includingFractionalSeconds: Bool) -> Date.ISO8601FormatStyle](./time%28includingfractionalseconds%29.md)
  Modifies the ISO 8601 date format style to include the time in the formatted output.
- [func timeSeparator(Date.ISO8601FormatStyle.TimeSeparator) -> Date.ISO8601FormatStyle](./timeseparator%28_%29.md)
  Modifies the ISO 8601 date format style to use the specified time separator.
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](./timezoneseparator%28_%29.md)
  Modifies the ISO 8601 date format style to use the specified time zone separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/timezone(separator:))*
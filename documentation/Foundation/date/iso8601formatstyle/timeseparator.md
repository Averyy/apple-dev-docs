# timeSeparator(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the ISO 8601 date format style to use the specified time separator.

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
func timeSeparator(_ separator: Date.ISO8601FormatStyle.TimeSeparator) -> Date.ISO8601FormatStyle
```

#### Return Value

An ISO 8601 date format style modified to include the specified time separator style.

#### Discussion

Possible values of [`Date.ISO8601FormatStyle.TimeSeparator`](date/iso8601formatstyle/timeseparator-swift.enum.md) are [`Date.ISO8601FormatStyle.TimeSeparator.colon`](date/iso8601formatstyle/timeseparator-swift.enum/colon.md) and [`Date.ISO8601FormatStyle.TimeSeparator.omitted`](date/iso8601formatstyle/timeseparator-swift.enum/omitted.md).

This example shows a variety of ISO 8601 time separator formats applied to an ISO 8601 date format:

```swift
let meetingDate = Date() // Jun 23, 2021 at 1:41 PM
meetingDate.formatted(.iso8601.timeSeparator(.omitted)) // 20210623T184148Z
meetingDate.formatted(.iso8601.timeSeparator(.colon)) // 20210623T18:41:48Z
meetingDate.formatted(.iso8601) // 20210623T184148Z
```

If no format is specified as a parameter, the [`Date.ISO8601FormatStyle.DateSeparator.omitted`](date/iso8601formatstyle/dateseparator-swift.enum/omitted.md) case is the default format.

For more information about ISO 8601 formatted dates, see the [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md).

## Parameters

- `separator`: Character used to separate the hour and minute in a date.

## See Also

- [func time(includingFractionalSeconds: Bool) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/time(includingfractionalseconds:).md)
  Modifies the ISO 8601 date format style to include the time in the formatted output.
- [func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezone(separator:).md)
  Modifies the ISO 8601 date format style to include the time zone in the formatted output.
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezoneseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time zone separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/timeseparator(_:))*
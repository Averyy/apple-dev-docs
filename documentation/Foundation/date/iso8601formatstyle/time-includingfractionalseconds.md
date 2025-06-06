# time(includingFractionalSeconds:)

**Framework**: Foundation  
**Kind**: method

Modifies the ISO 8601 date format style to include the time in the formatted output.

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
func time(includingFractionalSeconds: Bool) -> Date.ISO8601FormatStyle
```

#### Return Value

An ISO 8601 date format style modified to include the time.

#### Discussion

The following example shows an ISO 8601 format with, and without, a time and fractional seconds.

```swift
let meetingDate = Date() // Jun 24, 2021 at 6:52 AM
meetingDate.formatted(.iso8601
    .year()
    .month()
    .day()
    .time(includingFractionalSeconds: false)
)
// 20210624T115209

meetingDate.formatted(.iso8601
    .year()
    .time(includingFractionalSeconds: true)
)
// 2021T115209.274

meetingDate.formatted(.iso8601
    .year()
    .year()
    .month()
    .day()
    .dateSeparator(.dash)
    .time(includingFractionalSeconds: true)
    .timeSeparator(.colon)
)
// 2021-06-24T11:52:09.274

meetingDate.formatted(.iso8601
    .year()
    .year()
    .month()
    .day()
    .dateSeparator(.dash)
    .time(includingFractionalSeconds: false)
    .timeSeparator(.colon)
    .dateTimeSeparator(.space)
)
// 2021-06-24 11:52:09
```

The default [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md) includes the time but not the fractional seconds.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `includingFractionalSeconds`: Specifies whether the format style inclues the fractional component of the seconds.

## See Also

- [func timeSeparator(Date.ISO8601FormatStyle.TimeSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timeseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time separator.
- [func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezone(separator:).md)
  Modifies the ISO 8601 date format style to include the time zone in the formatted output.
- [func timeZoneSeparator(Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/timezoneseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified time zone separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/time(includingfractionalseconds:))*
# year()

**Framework**: Foundation  
**Kind**: method

Modifies the ISO 8601 date format style to include the year in the formatted output.

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
func year() -> Date.ISO8601FormatStyle
```

#### Return Value

An ISO 8601 date format style modified to include the year.

#### Discussion

This example shows an ISO 8601 format with, and without, a year.

```swift
let meetingDate = Date() // Jun 23, 2021 at 12:51 PM
meetingDate.formatted(.iso8601
    .year()
    .month()
    .day()
) 
// 20210623

meetingDate.formatted(.iso8601
    .month()
    .day()
) 
// 0623
```

The default [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md) includes the year.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## See Also

- [func dateSeparator(Date.ISO8601FormatStyle.DateSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/dateseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified date separator.
- [func month() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/month.md)
  Modifies the ISO 8601 date format style to include the month in the formatted output.
- [func weekOfYear() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/weekofyear.md)
  Modifies the ISO 8601 date format style to include the week of the year in the formatted output.
- [func day() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/day.md)
  Modifies the ISO 8601 date format style to include the day in the formatted output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/year())*
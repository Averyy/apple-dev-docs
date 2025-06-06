# weekOfYear()

**Framework**: Foundation  
**Kind**: method

Modifies the ISO 8601 date format style to include the week of the year in the formatted output.

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
func weekOfYear() -> Date.ISO8601FormatStyle
```

#### Return Value

An ISO 8601 date format style modified to include the week of the year.

#### Discussion

The following example shows an ISO 8601 format with, and without, a week of the year.

```swift
let meetingDate = Date() // Jun 23, 2021 at 12:51 PM
meetingDate.formatted(.iso8601
    .year()
    .month()
    .weekOfYear()
) // 202106W25

meetingDate.formatted(.iso8601
    .year()
    .month()
    .day()
    .weekOfYear()
) // 202106W2504

meetingDate.formatted(.iso8601
    .year()
    .day()
    .weekOfYear()
) // 2021W2504
```

When the format style includes the week of year, the output represents the day as the ordinal day of the week.

The default [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md) includes the month.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## See Also

- [func dateSeparator(Date.ISO8601FormatStyle.DateSeparator) -> Date.ISO8601FormatStyle](date/iso8601formatstyle/dateseparator(_:).md)
  Modifies the ISO 8601 date format style to use the specified date separator.
- [func year() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/year.md)
  Modifies the ISO 8601 date format style to include the year in the formatted output.
- [func month() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/month.md)
  Modifies the ISO 8601 date format style to include the month in the formatted output.
- [func day() -> Date.ISO8601FormatStyle](date/iso8601formatstyle/day.md)
  Modifies the ISO 8601 date format style to include the day in the formatted output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/weekofyear())*
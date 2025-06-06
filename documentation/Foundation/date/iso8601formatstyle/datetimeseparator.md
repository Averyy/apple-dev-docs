# dateTimeSeparator(_:)

**Framework**: Foundation  
**Kind**: method

Sets the character that specifies the date and time components.

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
func dateTimeSeparator(_ separator: Date.ISO8601FormatStyle.DateTimeSeparator) -> Date.ISO8601FormatStyle
```

#### Return Value

An ISO 8601 date format style with the provided date and time component separator.

#### Discussion

Possible values of [`Date.ISO8601FormatStyle.DateTimeSeparator`](date/iso8601formatstyle/datetimeseparator-swift.enum.md) are [`Date.ISO8601FormatStyle.DateTimeSeparator.space`](date/iso8601formatstyle/datetimeseparator-swift.enum/space.md) and [`Date.ISO8601FormatStyle.DateTimeSeparator.standard`](date/iso8601formatstyle/datetimeseparator-swift.enum/standard.md).

The following example shows a variety of [`Date.ISO8601FormatStyle.DateTimeSeparator`](date/iso8601formatstyle/datetimeseparator-swift.enum.md) formats applied to an ISO 8601 date format.

```swift
let meetingDate = Date() // Jun 23, 2021 at 10:21 AM
meetingDate.formatted(.iso8601.dateSeparator(.omitted)) // 20210623 152135Z
meetingDate.formatted(.iso8601.dateSeparator(.dash)) // 20210623T152135Z
meetingDate.formatted(.iso8601) // 20210623T152135Z
```

If no format is specified as a parameter, the [`Date.ISO8601FormatStyle.DateTimeSeparator.standard`](date/iso8601formatstyle/datetimeseparator-swift.enum/standard.md) case is the default format.

For more information about ISO 8601 formatted dates, see the [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md).

## Parameters

- `separator`: Possible values are   and  .

## See Also

- [var dateSeparator: Date.ISO8601FormatStyle.DateSeparator](date/iso8601formatstyle/dateseparator-swift.property.md)
  The character used to separate the components of a date.
- [var dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator](date/iso8601formatstyle/datetimeseparator-swift.property.md)
  The character used to separate the date and time components of an ISO 8601 string representation of a date.
- [var timeZone: TimeZone](date/iso8601formatstyle/timezone.md)
  The time zone used to create and parse date representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/datetimeseparator(_:))*
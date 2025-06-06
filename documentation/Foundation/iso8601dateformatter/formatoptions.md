# formatOptions

**Framework**: Foundation  
**Kind**: property

Options for generating and parsing ISO 8601 date representations. See [`ISO8601DateFormatter.Options`](iso8601dateformatter/options.md) for possible values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var formatOptions: ISO8601DateFormatter.Options { get set }
```

#### Discussion

The ISO 8601 specification allows for dates to be expressed in a variety of ways. You can configure the format used to parse and generate representations by specifying various combinations of format options.

| Format | Example | Options |
| --- | --- | --- |
| Date with dash separators | `2016-06-13` | [`withFullDate`](iso8601dateformatter/options/withfulldate.md), [`withDashSeparatorInDate`](iso8601dateformatter/options/withdashseparatorindate.md) |
| [`RFC 3339`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3339) Date and Time | `2016-06-13T16:00:00+00:00` | [`withInternetDateTime`](iso8601dateformatter/options/withinternetdatetime.md) |
| Date and Time with space separator between date and time | `20160613 160000` | [`withFullDate`](iso8601dateformatter/options/withfulldate.md), [`withFullTime`](iso8601dateformatter/options/withfulltime.md), [`withSpaceBetweenDateAndTime`](iso8601dateformatter/options/withspacebetweendateandtime.md) |
| Week of Year | `2016-W24` | [`withYear`](iso8601dateformatter/options/withyear.md), [`withWeekOfYear`](iso8601dateformatter/options/withweekofyear.md), [`withDashSeparatorInDate`](iso8601dateformatter/options/withdashseparatorindate.md) |
| Week of Year with Ordinal Weekday | `2016-W24-1` | [`withYear`](iso8601dateformatter/options/withyear.md), [`withWeekOfYear`](iso8601dateformatter/options/withweekofyear.md), [`withDay`](iso8601dateformatter/options/withday.md), [`withDashSeparatorInDate`](iso8601dateformatter/options/withdashseparatorindate.md) |
| Ordinal Day of Year | `2016-165` | [`withYear`](iso8601dateformatter/options/withyear.md), [`withDay`](iso8601dateformatter/options/withday.md), [`withDashSeparatorInDate`](iso8601dateformatter/options/withdashseparatorindate.md) |

> ❗ **Important**:  Resetting this property can incur a significant performance cost, as it may cause internal state to be regenerated.

 Resetting this property can incur a significant performance cost, as it may cause internal state to be regenerated.

## See Also

- [var timeZone: TimeZone!](iso8601dateformatter/timezone.md)
  The time zone used to create and parse date representations. When unspecified, GMT is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter/formatoptions)*
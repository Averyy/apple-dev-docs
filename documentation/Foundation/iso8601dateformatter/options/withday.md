# withDay

**Framework**: Foundation  
**Kind**: property

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
static var withDay: ISO8601DateFormatter.Options { get }
```

#### Discussion

The date representation includes the day. The format for day is inferred based on provided options:

- If [`withMonth`](iso8601dateformatter/options/withmonth.md) is specified, `dd` is used.
- If [`withWeekOfYear`](iso8601dateformatter/options/withweekofyear.md) is specified, `ee` is used.
- Otherwise, `DDD` is used.

## See Also

- [static var withYear: ISO8601DateFormatter.Options](iso8601dateformatter/options/withyear.md)
- [static var withMonth: ISO8601DateFormatter.Options](iso8601dateformatter/options/withmonth.md)
- [static var withWeekOfYear: ISO8601DateFormatter.Options](iso8601dateformatter/options/withweekofyear.md)
- [static var withTime: ISO8601DateFormatter.Options](iso8601dateformatter/options/withtime.md)
- [static var withTimeZone: ISO8601DateFormatter.Options](iso8601dateformatter/options/withtimezone.md)
- [static var withSpaceBetweenDateAndTime: ISO8601DateFormatter.Options](iso8601dateformatter/options/withspacebetweendateandtime.md)
- [static var withDashSeparatorInDate: ISO8601DateFormatter.Options](iso8601dateformatter/options/withdashseparatorindate.md)
- [static var withColonSeparatorInTime: ISO8601DateFormatter.Options](iso8601dateformatter/options/withcolonseparatorintime.md)
- [static var withColonSeparatorInTimeZone: ISO8601DateFormatter.Options](iso8601dateformatter/options/withcolonseparatorintimezone.md)
- [static var withFullDate: ISO8601DateFormatter.Options](iso8601dateformatter/options/withfulldate.md)
- [static var withFullTime: ISO8601DateFormatter.Options](iso8601dateformatter/options/withfulltime.md)
- [static var withInternetDateTime: ISO8601DateFormatter.Options](iso8601dateformatter/options/withinternetdatetime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter/options/withday)*
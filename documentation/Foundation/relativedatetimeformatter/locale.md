# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when formatting the date.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var locale: Locale! { get set }
```

#### Discussion

The default value is [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md).

## See Also

- [var calendar: Calendar!](relativedatetimeformatter/calendar.md)
  The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [var dateTimeStyle: RelativeDateTimeFormatter.DateTimeStyle](relativedatetimeformatter/datetimestyle-swift.property.md)
  The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [RelativeDateTimeFormatter.DateTimeStyle](relativedatetimeformatter/datetimestyle-swift.enum.md)
  A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [var unitsStyle: RelativeDateTimeFormatter.UnitsStyle](relativedatetimeformatter/unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [RelativeDateTimeFormatter.UnitsStyle](relativedatetimeformatter/unitsstyle-swift.enum.md)
  A type that represents the style to use when formatting the units of relative dates.
- [var formattingContext: Formatter.Context](relativedatetimeformatter/formattingcontext.md)
  A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/locale)*
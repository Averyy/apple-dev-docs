# formattingContext

**Framework**: Foundation  
**Kind**: property

A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.

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
var formattingContext: Formatter.Context { get set }
```

#### Discussion

The default value is [`Formatter.Context.unknown`](formatter/context/unknown.md). For additional details about specifying contexts, see [`Formatter.Context`](formatter/context.md).

## See Also

- [var calendar: Calendar!](relativedatetimeformatter/calendar.md)
  The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [var locale: Locale!](relativedatetimeformatter/locale.md)
  The locale to use when formatting the date.
- [var dateTimeStyle: RelativeDateTimeFormatter.DateTimeStyle](relativedatetimeformatter/datetimestyle-swift.property.md)
  The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [RelativeDateTimeFormatter.DateTimeStyle](relativedatetimeformatter/datetimestyle-swift.enum.md)
  A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [var unitsStyle: RelativeDateTimeFormatter.UnitsStyle](relativedatetimeformatter/unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [RelativeDateTimeFormatter.UnitsStyle](relativedatetimeformatter/unitsstyle-swift.enum.md)
  A type that represents the style to use when formatting the units of relative dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/formattingcontext)*
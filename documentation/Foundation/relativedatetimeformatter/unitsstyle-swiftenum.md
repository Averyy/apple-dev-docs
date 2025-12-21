# RelativeDateTimeFormatter.UnitsStyle

**Framework**: Foundation  
**Kind**: enum

A type that represents the style to use when formatting the units of relative dates.

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
enum UnitsStyle
```

## Topics

### Formatting Date and Time Units
- [RelativeDateTimeFormatter.UnitsStyle.abbreviated](relativedatetimeformatter/unitsstyle-swift.enum/abbreviated.md)
  A style that uses abbreviated units, such as “2 mo. ago”.
- [RelativeDateTimeFormatter.UnitsStyle.full](relativedatetimeformatter/unitsstyle-swift.enum/full.md)
  A style that uses full units, such as “2 months ago”.
- [RelativeDateTimeFormatter.UnitsStyle.short](relativedatetimeformatter/unitsstyle-swift.enum/short.md)
  A style that uses shortened units, such as “2 mo. ago”.
- [RelativeDateTimeFormatter.UnitsStyle.spellOut](relativedatetimeformatter/unitsstyle-swift.enum/spellout.md)
  A style that spells out units such as “two months ago”.
### Initializers
- [init?(rawValue: Int)](relativedatetimeformatter/unitsstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var formattingContext: Formatter.Context](relativedatetimeformatter/formattingcontext.md)
  A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/unitsstyle-swift.enum)*
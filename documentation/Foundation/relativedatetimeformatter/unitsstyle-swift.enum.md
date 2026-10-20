# RelativeDateTimeFormatter.UnitsStyle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSRelativeDateTimeFormatterUnitsStyle : NSInteger;
```

## Topics

### Formatting Date and Time Units
- [RelativeDateTimeFormatter.UnitsStyle.abbreviated](./unitsstyle-swift.enum/abbreviated.md)
  A style that uses abbreviated units, such as “2 mo. ago”.
- [RelativeDateTimeFormatter.UnitsStyle.full](./unitsstyle-swift.enum/full.md)
  A style that uses full units, such as “2 months ago”.
- [RelativeDateTimeFormatter.UnitsStyle.short](./unitsstyle-swift.enum/short.md)
  A style that uses shortened units, such as “2 mo. ago”.
- [RelativeDateTimeFormatter.UnitsStyle.spellOut](./unitsstyle-swift.enum/spellout.md)
  A style that spells out units such as “two months ago”.
### Initializers
- [init?(rawValue: Int)](./unitsstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring Formatter Options
- [var calendar: Calendar!](./calendar.md)
  The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [var locale: Locale!](./locale.md)
  The locale to use when formatting the date.
- [var dateTimeStyle: RelativeDateTimeFormatter.DateTimeStyle](./datetimestyle-swift.property.md)
  The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [RelativeDateTimeFormatter.DateTimeStyle](./datetimestyle-swift.enum.md)
  A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [var unitsStyle: RelativeDateTimeFormatter.UnitsStyle](./unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/unitsstyle-swift.enum)*
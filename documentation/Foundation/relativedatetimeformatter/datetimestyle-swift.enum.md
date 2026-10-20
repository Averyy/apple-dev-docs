# RelativeDateTimeFormatter.DateTimeStyle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.

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
enum DateTimeStyle
```

```c
enum NSRelativeDateTimeFormatterStyle : NSInteger;
```

## Topics

### Formatting Dates and Times
- [RelativeDateTimeFormatter.DateTimeStyle.named](./datetimestyle-swift.enum/named.md)
  A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.
- [RelativeDateTimeFormatter.DateTimeStyle.numeric](./datetimestyle-swift.enum/numeric.md)
  A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.
### Initializers
- [init?(rawValue: Int)](./datetimestyle-swift.enum/init%28rawvalue%29.md)

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
- [var unitsStyle: RelativeDateTimeFormatter.UnitsStyle](./unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [RelativeDateTimeFormatter.UnitsStyle](./unitsstyle-swift.enum.md)
  A type that represents the style to use when formatting the units of relative dates.
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum)*
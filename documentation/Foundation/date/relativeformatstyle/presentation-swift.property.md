# presentation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.

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
var presentation: Date.RelativeFormatStyle.Presentation
```

#### Discussion

Express relative date formats in either `numeric` or `named` styles. For example:

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    var formatStyle = Date.RelativeFormatStyle()
    
    formatStyle.presentation = .numeric
    past.formatted(formatStyle) // "1 week ago"
    
    formatStyle.presentation = .named
    past.formatted(formatStyle) // "last week"
}
```

## See Also

### Modifying a Relative Date Format Style
- [var unitsStyle: Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [var calendar: Calendar](./calendar.md)
  The calendar to use when formatting relative dates.
- [var capitalizationContext: FormatStyleCapitalizationContext](./capitalizationcontext.md)
  The capitalization context to use when formatting the relative dates.
- [var locale: Locale](./locale.md)
  The locale to use when formatting the relative date.
- [func locale(Locale) -> Date.RelativeFormatStyle](./locale%28_%29.md)
  Modifies the relative date format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.property)*
# presentation

**Framework**: Foundation  
**Kind**: property

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

- [var unitsStyle: Date.RelativeFormatStyle.UnitsStyle](date/relativeformatstyle/unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [var calendar: Calendar](date/relativeformatstyle/calendar.md)
  The calendar to use when formatting relative dates.
- [var capitalizationContext: FormatStyleCapitalizationContext](date/relativeformatstyle/capitalizationcontext.md)
  The capitalization context to use when formatting the relative dates.
- [var locale: Locale](date/relativeformatstyle/locale.md)
  The locale to use when formatting the relative date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.property)*
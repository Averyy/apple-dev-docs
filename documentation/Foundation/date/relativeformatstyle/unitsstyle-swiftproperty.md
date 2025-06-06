# unitsStyle

**Framework**: Foundation  
**Kind**: property

The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.

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
var unitsStyle: Date.RelativeFormatStyle.UnitsStyle
```

#### Discussion

Express relative date format units in either `wide`, `narrow`, `abbreviated`, or `spellOut` styles. For example:

```swift
if let past = Calendar.current.date(byAdding: .day, value: -14, to: Date()) {
    past.formatted(.relative(presentation: .named, unitsStyle: .wide)) // "2 weeks ago"
    past.formatted(.relative(presentation: .named, unitsStyle: .narrow)) // "2 wk. ago"
    past.formatted(.relative(presentation: .named, unitsStyle: .abbreviated)) // "2 wk. ago"
    past.formatted(.relative(presentation: .named, unitsStyle: .spellOut)) // "two weeks ago"
}
```

## See Also

- [var presentation: Date.RelativeFormatStyle.Presentation](date/relativeformatstyle/presentation-swift.property.md)
  Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [var calendar: Calendar](date/relativeformatstyle/calendar.md)
  The calendar to use when formatting relative dates.
- [var capitalizationContext: FormatStyleCapitalizationContext](date/relativeformatstyle/capitalizationcontext.md)
  The capitalization context to use when formatting the relative dates.
- [var locale: Locale](date/relativeformatstyle/locale.md)
  The locale to use when formatting the relative date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/unitsstyle-swift.property)*
# calendar

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The calendar to use when formatting relative dates.

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
var calendar: Calendar
```

## Discussion

Defaults to [`autoupdatingCurrent`](../../nscalendar/autoupdatingcurrent.md). If you set this property to `nil`, the format style resets to using [`autoupdatingCurrent`](../../nscalendar/autoupdatingcurrent.md).

## See Also

### Modifying a Relative Date Format Style
- [var presentation: Date.RelativeFormatStyle.Presentation](./presentation-swift.property.md)
  Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [var unitsStyle: Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [var capitalizationContext: FormatStyleCapitalizationContext](./capitalizationcontext.md)
  The capitalization context to use when formatting the relative dates.
- [var locale: Locale](./locale.md)
  The locale to use when formatting the relative date.
- [func locale(Locale) -> Date.RelativeFormatStyle](./locale%28_%29.md)
  Modifies the relative date format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/calendar)*
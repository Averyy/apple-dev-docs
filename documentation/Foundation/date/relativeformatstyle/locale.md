# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when formatting the relative date.

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
var locale: Locale
```

#### Discussion

The default value is [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the format style resets to using [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md).

## See Also

- [var presentation: Date.RelativeFormatStyle.Presentation](date/relativeformatstyle/presentation-swift.property.md)
  Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [var unitsStyle: Date.RelativeFormatStyle.UnitsStyle](date/relativeformatstyle/unitsstyle-swift.property.md)
  The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [var calendar: Calendar](date/relativeformatstyle/calendar.md)
  The calendar to use when formatting relative dates.
- [var capitalizationContext: FormatStyleCapitalizationContext](date/relativeformatstyle/capitalizationcontext.md)
  The capitalization context to use when formatting the relative dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/locale)*
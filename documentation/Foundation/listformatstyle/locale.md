# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when formatting items in the list.

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

A [`Locale`](locale.md) instance is typically used to provide, format, and interpret information about and according to the user’s customs and preferences.

Examples include ISO region and language codes, currency code, calendar, system of measurement, and decimal separator.

The default value is [`autoupdatingCurrent`](locale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using `autoupdatingCurrent`.

## See Also

- [var width: ListFormatStyle<Style, Base>.Width](listformatstyle/width-swift.property.md)
  The size of the list.
- [ListFormatStyle.Width](listformatstyle/width-swift.enum.md)
  The type representing the width of a list.
- [var listType: ListFormatStyle<Style, Base>.ListType](listformatstyle/listtype-swift.property.md)
  The type of the list.
- [ListFormatStyle.ListType](listformatstyle/listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/locale)*
# width

**Framework**: Foundation  
**Kind**: property

The size of the list.

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
var width: ListFormatStyle<Style, Base>.Width
```

#### Discussion

The `width` property controls the size of the list. The [`locale`](listformatstyle/locale.md) determines the formatting and abbreviation of the string for the given `width`.

For example, for English:

```swift
["One", "Two", "Three"].formatted(.list(type: .and, width: .standard))
// “One, Two, and Three”

["One", "Two", "Three"].formatted(.list(type: .and, width: .short))
// “One, Two, & Three” 

["One", "Two", "Three"].formatted(.list(type: .and, width: .narrow))
// “One, Two, Three” 
```

The default value is [`ListFormatStyle.Width.standard`](listformatstyle/width-swift.enum/standard.md).

## See Also

- [ListFormatStyle.Width](listformatstyle/width-swift.enum.md)
  The type representing the width of a list.
- [var listType: ListFormatStyle<Style, Base>.ListType](listformatstyle/listtype-swift.property.md)
  The type of the list.
- [ListFormatStyle.ListType](listformatstyle/listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.
- [var locale: Locale](listformatstyle/locale.md)
  The locale to use when formatting items in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/width-swift.property)*
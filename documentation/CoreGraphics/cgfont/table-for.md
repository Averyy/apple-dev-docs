# table(for:)

**Framework**: Core Graphics  
**Kind**: method

Returns the font table that corresponds to the provided tag.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func table(for tag: UInt32) -> CFData?
```

#### Return Value

The font table that corresponds to the tag, or `nil` if no such table exists.

## Parameters

- `tag`: The tag for the table you want to obtain.

## See Also

- [var tableTags: CFArray?](cgfont/tabletags.md)
  Returns an array of tags that correspond to the font tables for a font.
- [Font Table Index Values](font-table-index-values.md)
  Possible values for an index into a font table.
- [Obsolete Font Table Index Values](obsolete-font-table-index-values.md)
  Deprecated values for an index into a font table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/table(for:))*
# tableTags

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns an array of tags that correspond to the font tables for a font.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var tableTags: CFArray? { get }
```

```c
extern CFArrayRefCGFontCopyTableTags(CGFontRef font);
```

#### Discussion

Each entry in the returned array is a four-byte value that represents a single TrueType or OpenType font table tag. To obtain a tag at index `k` in a manner that is appropriate for 32-bit and 64-bit architectures, you need to use code similar to the following:

```objc
tag = (uint32_t)(uintptr_t)CFArrayGetValue(table, k);
```

## See Also

### Working with Font Tables
- [func table(for: UInt32) -> CFData?](./table%28for%29.md)
  Returns the font table that corresponds to the provided tag.
- [Font Table Index Values](../font-table-index-values.md)
  Possible values for an index into a font table.
- [Obsolete Font Table Index Values](../obsolete-font-table-index-values.md)
  Deprecated values for an index into a font table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/tabletags)*
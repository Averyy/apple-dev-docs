# pointSize

**Framework**: AppKit  
**Kind**: property

The point size of the font.

**Availability**:
- macOS ?+

## Declaration

```swift
var pointSize: CGFloat { get }
```

#### Discussion

If the font has a nonstandard matrix, the point size is the effective vertical point size.

## See Also

- [var coveredCharacterSet: CharacterSet](nsfont/coveredcharacterset.md)
  The character set containing all of the nominal characters that the font can render.
- [var fontDescriptor: NSFontDescriptor](nsfont/fontdescriptor.md)
  The font descriptor object for the font.
- [var isFixedPitch: Bool](nsfont/isfixedpitch.md)
  A Boolean value indicating whether all glyphs in the font have the same advancement.
- [var mostCompatibleStringEncoding: UInt](nsfont/mostcompatiblestringencoding.md)
  The string encoding that works best with the font.
- [Advanced Font Metrics](advanced-font-metrics.md)
  Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/pointsize)*
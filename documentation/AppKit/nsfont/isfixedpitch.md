# isFixedPitch

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether all glyphs in the font have the same advancement.

**Availability**:
- macOS ?+

## Declaration

```swift
var isFixedPitch: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when all glyphs have the same advancement or [`false`](https://developer.apple.com/documentation/swift/false) when they do not. Some Japanese fonts encoded with the scheme “EUC12-NJE-CFEncoding” return that they have the same advancement, but actually encode glyphs with one of two advancements, for historical compatibility. You may need to handle such fonts specially for some applications.

## See Also

- [func advancement(forGlyph: NSGlyph) -> NSSize](nsfont/advancement(forglyph:).md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
- [var pointSize: CGFloat](nsfont/pointsize.md)
  The point size of the font.
- [var coveredCharacterSet: CharacterSet](nsfont/coveredcharacterset.md)
  The character set containing all of the nominal characters that the font can render.
- [var fontDescriptor: NSFontDescriptor](nsfont/fontdescriptor.md)
  The font descriptor object for the font.
- [var mostCompatibleStringEncoding: UInt](nsfont/mostcompatiblestringencoding.md)
  The string encoding that works best with the font.
- [Advanced Font Metrics](advanced-font-metrics.md)
  Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/isfixedpitch)*
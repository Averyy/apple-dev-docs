# isFixedPitch

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether all glyphs in the font have the same advancement.

**Availability**:
- macOS

## Declaration

```swift
var isFixedPitch: Bool { get }
```

```objc
@property (readonly, getter=isFixedPitch) BOOL fixedPitch;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when all glyphs have the same advancement or [`false`](../../Swift/false.md) when they do not. Some Japanese fonts encoded with the scheme “EUC12-NJE-CFEncoding” return that they have the same advancement, but actually encode glyphs with one of two advancements, for historical compatibility. You may need to handle such fonts specially for some applications.

## See Also

### Related Documentation
- [func advancement(forGlyph: NSGlyph) -> NSSize](./advancement%28forglyph%29.md)
  Returns the nominal spacing for the given glyph—the distance the current point moves after showing the glyph—accounting for the receiver’s size.
### Getting Font Metrics and Information
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the font.
- [var coveredCharacterSet: CharacterSet](./coveredcharacterset.md)
  The character set containing all of the nominal characters that the font can render.
- [var fontDescriptor: NSFontDescriptor](./fontdescriptor.md)
  The font descriptor object for the font.
- [var mostCompatibleStringEncoding: UInt](./mostcompatiblestringencoding.md)
  The string encoding that works best with the font.
- [Advanced Font Metrics](../advanced-font-metrics.md)
  Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/isfixedpitch)*
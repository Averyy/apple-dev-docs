# fontDescriptor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font descriptor object for the font.

**Availability**:
- macOS

## Declaration

```swift
var fontDescriptor: NSFontDescriptor { get }
```

```objc
@property (strong, readonly) NSFontDescriptor * fontDescriptor;
```

## Discussion

The font descriptor contains a mutable dictionary of optional attributes for creating an `NSFont` object. For more information about font descriptors, see [`NSFontDescriptor`](../nsfontdescriptor.md).

## See Also

### Getting Font Metrics and Information
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the font.
- [var coveredCharacterSet: CharacterSet](./coveredcharacterset.md)
  The character set containing all of the nominal characters that the font can render.
- [var isFixedPitch: Bool](./isfixedpitch.md)
  A Boolean value indicating whether all glyphs in the font have the same advancement.
- [var mostCompatibleStringEncoding: UInt](./mostcompatiblestringencoding.md)
  The string encoding that works best with the font.
- [Advanced Font Metrics](../advanced-font-metrics.md)
  Retrieve details about ascender and descender heights, glyph bounding rectangles, glyph advancements, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/fontdescriptor)*
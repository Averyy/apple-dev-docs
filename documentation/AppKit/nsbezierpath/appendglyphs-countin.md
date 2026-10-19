# appendGlyphs(_:count:in:)

**Framework**: AppKit  
**Kind**: method

Appends the outlines of the specified glyphs to the path.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func appendGlyphs(_ glyphs: UnsafeMutablePointer<NSGlyph>, count: Int, in font: NSFont)
```

#### Discussion

If the glyphs are not encoded in the font specified by the `fontObj` parameter—that is, the font does not have an entry for one of the specified glyphs—then no path is appended to the receiver.

You must set the path’s current point (using the [`move(to:)`](nsbezierpath/move(to:).md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](https://developer.apple.com/documentation/foundation/nsexceptionname/genericexception) exception.

## Parameters

- `glyphs`: A C-style array of `NSGlyph` data types to add to the path.
- `count`: The number of glyphs in the `glyphs` parameter.
- `font`: The font in which the glyphs are encoded.

## See Also

- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
- [func appendGlyph(NSGlyph, in: NSFont)](nsbezierpath/appendglyph(_:in:).md)
  Appends an outline of the specified glyph to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendglyphs(_:count:in:))*
# appendGlyph(_:in:)

**Framework**: AppKit  
**Kind**: method

Appends an outline of the specified glyph to the path.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func appendGlyph(_ glyph: NSGlyph, in font: NSFont)
```

#### Discussion

If the glyph is not encoded in the font specified by the `fontObj` parameter—that is, the font does not have an entry for the specified glyph—then no path is appended to the receiver.

You must set the path’s current point (using the [`move(to:)`](nsbezierpath/move(to:).md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](https://developer.apple.com/documentation/foundation/nsexceptionname/genericexception) exception.

## Parameters

- `glyph`: The glyph to add to the path.
- `font`: The font in which the glyph is encoded.

## See Also

- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](nsbezierpath/appendglyphs(_:count:in:).md)
  Appends the outlines of the specified glyphs to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendglyph(_:in:))*
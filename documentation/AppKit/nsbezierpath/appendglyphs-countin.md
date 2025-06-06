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

You must set the path’s current point (using the [`move(to:)`](nsbezierpath/move(to:).md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1412113-genericexception) exception.

## Parameters

- `glyphs`: A C-style array of   data types to add to the path.
- `count`: The number of glyphs in the   parameter.
- `font`: The font in which the glyphs are encoded.

## See Also

- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
- [func append(NSBezierPath)](nsbezierpath/append(_:).md)
  Appends the contents of the specified path object to the path.
- [func appendPoints(NSPointArray, count: Int)](nsbezierpath/appendpoints(_:count:).md)
  Appends a series of line segments to the path.
- [func appendOval(in: NSRect)](nsbezierpath/appendoval(in:).md)
  Appends an oval path to the path, inscribing the oval in the specified rectangle.
- [func appendArc(from: NSPoint, to: NSPoint, radius: CGFloat)](nsbezierpath/appendarc(from:to:radius:).md)
  Appends an arc to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat)](nsbezierpath/appendarc(withcenter:radius:startangle:endangle:).md)
  Appends an arc of a circle to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](nsbezierpath/appendarc(withcenter:radius:startangle:endangle:clockwise:).md)
  Appends an arc of a circle to the path.
- [func appendRect(NSRect)](nsbezierpath/appendrect(_:).md)
  Appends a rectangular path to the path.
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/appendroundedrect(_:xradius:yradius:).md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](nsbezierpath/append(withcgglyph:in:).md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](nsbezierpath/append(withcgglyphs:count:in:).md)
  Appends the outlines of the specified glyphs to the path.
- [func appendGlyph(NSGlyph, in: NSFont)](nsbezierpath/appendglyph(_:in:).md)
  Appends an outline of the specified glyph to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendglyphs(_:count:in:))*
# append(withCGGlyph:in:)

**Framework**: AppKit  
**Kind**: method

Appends an outline of the specified glyph to the path.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func append(withCGGlyph glyph: CGGlyph, in font: NSFont)
```

## See Also

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
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](nsbezierpath/append(withcgglyphs:count:in:).md)
  Appends the outlines of the specified glyphs to the path.
- [func appendGlyph(NSGlyph, in: NSFont)](nsbezierpath/appendglyph(_:in:).md)
  Appends an outline of the specified glyph to the path.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](nsbezierpath/appendglyphs(_:count:in:).md)
  Appends the outlines of the specified glyphs to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/append(withcgglyph:in:))*
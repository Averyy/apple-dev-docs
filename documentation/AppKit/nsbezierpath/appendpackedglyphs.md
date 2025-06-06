# appendPackedGlyphs(_:)

**Framework**: AppKit  
**Kind**: method

Appends an array of packed glyphs to the path.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func appendPackedGlyphs(_ packedGlyphs: UnsafePointer<CChar>)
```

#### Discussion

You should avoid using this method directly. Instead, use the [`appendGlyph(_:in:)`](nsbezierpath/appendglyph(_:in:).md) and [`appendGlyphs(_:count:in:)`](nsbezierpath/appendglyphs(_:count:in:).md) methods to append glyphs to a path.

## Parameters

- `packedGlyphs`: A C-style array containing one or more   data types terminated by a   character.

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
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](nsbezierpath/appendglyphs(_:count:in:).md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendpackedglyphs(_:))*
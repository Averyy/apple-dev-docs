# appendArc(withCenter:radius:startAngle:endAngle:clockwise:)

**Framework**: AppKit  
**Kind**: method

Appends an arc of a circle to the path.

**Availability**:
- macOS ?+

## Declaration

```swift
func appendArc(withCenter center: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)
```

#### Discussion

The created arc lies on the perimeter of the circle, between the angles specified by the `startAngle` and `endAngle` parameters. The arc is drawn in the direction indicated by the `clockwise` parameter. If the receiver’s path is empty, this method sets the current point to the beginning of the arc before adding the arc segment. If the receiver’s path is not empty, a line is drawn from the current point to the starting point of the arc.

Depending on the length of the arc, this method may add multiple connected curve segments to the path.

## Parameters

- `center`: Specifies the center point of the circle used to define the arc.
- `radius`: Specifies the radius of the circle used to define the arc.
- `startAngle`: Specifies the starting angle of the arc, measured in degrees counterclockwise from the x-axis.
- `endAngle`: Specifies the end angle of the arc, measured in degrees counterclockwise from the x-axis.
- `clockwise`:   if you want the arc to be drawn in a clockwise direction; otherwise   to draw the arc in a counterclockwise direction.

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
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendarc(withcenter:radius:startangle:endangle:clockwise:))*
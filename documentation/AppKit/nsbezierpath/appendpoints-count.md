# appendPoints(_:count:)

**Framework**: AppKit  
**Kind**: method

Appends a series of line segments to the path.

**Availability**:
- macOS ?+

## Declaration

```swift
func appendPoints(_ points: NSPointArray, count: Int)
```

#### Discussion

This method interprets the points as a set of connected line segments.  If the current path contains an open subpath, a line is created from the last point in that subpath to the first point in the points array. If the current path is empty, the first point in the points array is used to set the starting point of the line segments. Subsequent line segments are added using the remaining points in the array.

This method does not close the path that is created. If you wish to create a closed path, you must do so by explicitly invoking the receiver’s [`close()`](nsbezierpath/close().md) method.

## Parameters

- `points`: A C-style array of   data types, each of which contains the end point of the next line segment.
- `count`: The number of points in the   parameter.

## See Also

- [func append(NSBezierPath)](nsbezierpath/append(_:).md)
  Appends the contents of the specified path object to the path.
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
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendpoints(_:count:))*
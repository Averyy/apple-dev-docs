# strokeLine(from:to:)

**Framework**: AppKit  
**Kind**: method

Strokes a line between two points using the current stroke color and the default drawing attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
class func strokeLine(from point1: NSPoint, to point2: NSPoint)
```

#### Discussion

This method strokes the specified path immediately.

## Parameters

- `point1`: The starting point of the line.
- `point2`: The ending point of the line.

## See Also

- [func move(to: NSPoint)](nsbezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](nsbezierpath/line(to:).md)
  Appends a straight line to the path.
- [func stroke()](nsbezierpath/stroke.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](nsbezierpath/fill.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](nsbezierpath/fill(_:).md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](nsbezierpath/stroke(_:).md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/strokeline(from:to:))*
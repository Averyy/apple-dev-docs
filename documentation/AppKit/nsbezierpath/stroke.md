# stroke(_:)

**Framework**: AppKit  
**Kind**: method

Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
class func stroke(_ rect: NSRect)
```

#### Discussion

The path is drawn beginning at the rectangle’s origin and proceeding in a counterclockwise direction. This method strokes the specified path immediately.

## Parameters

- `rect`: A rectangle in the current coordinate system.

## See Also

- [func set()](nscolor/set.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [init(rect: NSRect)](nsbezierpath/init(rect:).md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [func appendRect(NSRect)](nsbezierpath/appendrect(_:).md)
  Appends a rectangular path to the path.
- [func stroke()](nsbezierpath/stroke.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](nsbezierpath/fill.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](nsbezierpath/fill(_:).md)
  Fills the specified rectangular path with the current fill color.
- [class func strokeLine(from: NSPoint, to: NSPoint)](nsbezierpath/strokeline(from:to:).md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/stroke(_:))*
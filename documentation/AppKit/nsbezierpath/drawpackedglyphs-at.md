# drawPackedGlyphs(_:at:)

**Framework**: AppKit  
**Kind**: method

Draws a set of packed glyphs at the specified point in the current coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
class func drawPackedGlyphs(_ packedGlyphs: UnsafePointer<CChar>, at point: NSPoint)
```

#### Discussion

This method draws the glyphs immediately.

You should avoid using this method directly. Instead, use the [`appendGlyph(_:in:)`](nsbezierpath/appendglyph(_:in:).md) and [`appendGlyphs(_:count:in:)`](nsbezierpath/appendglyphs(_:count:in:).md) methods to create a path with one or more glyphs.

## Parameters

- `packedGlyphs`: A C-style array containing one or more   data types terminated by a   character.
- `point`: The starting point at which to draw the glyphs.

## See Also

- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.
- [func set()](nscolor/set.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [func stroke()](nsbezierpath/stroke.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](nsbezierpath/fill.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](nsbezierpath/fill(_:).md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](nsbezierpath/stroke(_:).md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func strokeLine(from: NSPoint, to: NSPoint)](nsbezierpath/strokeline(from:to:).md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/drawpackedglyphs(_:at:))*
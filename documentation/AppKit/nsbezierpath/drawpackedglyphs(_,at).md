# drawPackedGlyphs(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Draws a set of packed glyphs at the specified point in the current coordinate system.

**Availability**:
- macOS

## Declaration

```swift
class func drawPackedGlyphs(_ packedGlyphs: UnsafePointer<CChar>, at point: NSPoint)
```

```objc
+ (void) drawPackedGlyphs:(const char *) packedGlyphs atPoint:(NSPoint) point;
```

## Discussion

This method draws the glyphs immediately.

You should avoid using this method directly. Instead, use the [`appendGlyph(_:in:)`](./appendglyph%28_,in%29.md) and [`appendGlyphs(_:count:in:)`](./appendglyphs%28_,count,in%29.md) methods to create a path with one or more glyphs.

## Parameters

- `packedGlyphs`: A C-style array containing one or more `CGGlyph` data types terminated by a `NULL` character.
- `point`: The starting point at which to draw the glyphs.

## See Also

### Related Documentation
- [func appendPackedGlyphs(UnsafePointer<CChar>)](./appendpackedglyphs%28_%29.md)
  Appends an array of packed glyphs to the path.
- [func set()](../nscolor/set%28%29.md)
  Sets the color of subsequent drawing to the color that the color object represents.
### Drawing a Path
- [func stroke()](./stroke%28%29.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](./fill%28%29.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](./stroke%28_%29.md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func strokeLine(from: NSPoint, to: NSPoint)](./strokeline%28from,to%29.md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/drawpackedglyphs(_:at:))*
# stroke(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.

**Availability**:
- macOS

## Declaration

```swift
class func stroke(_ rect: NSRect)
```

```objc
+ (void) strokeRect:(NSRect) rect;
```

## Discussion

The path is drawn beginning at the rectangle’s origin and proceeding in a counterclockwise direction. This method strokes the specified path immediately.

## Parameters

- `rect`: A rectangle in the current coordinate system.

## See Also

### Related Documentation
- [func set()](../nscolor/set%28%29.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [func appendRect(NSRect)](./appendrect%28_%29.md)
  Appends a rectangular path to the path.
### Drawing a Path
- [func stroke()](./stroke%28%29.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](./fill%28%29.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func strokeLine(from: NSPoint, to: NSPoint)](./strokeline%28from,to%29.md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](./drawpackedglyphs%28_,at%29.md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/stroke(_:))*
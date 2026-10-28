# fill()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Paints the region enclosed by the path.

**Availability**:
- macOS

## Declaration

```swift
func fill()
```

```objc
- (void) fill;
```

## Discussion

This method fills the path using the current fill color and the receiver’s current winding rule. If the path contains any open subpaths, this method implicitly closes them before painting the fill region.

The painted region includes the pixels right up to, but not including, the path line itself. For paths with large line widths, this can result in overlap between the fill region and the stroked path (which is itself centered on the path line).

## See Also

### Related Documentation
- [func set()](../nscolor/set%28%29.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [var windingRule: NSBezierPath.WindingRule](./windingrule-swift.property.md)
  The winding rule used to fill the path.
### Drawing a Path
- [func stroke()](./stroke%28%29.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](./stroke%28_%29.md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func strokeLine(from: NSPoint, to: NSPoint)](./strokeline%28from,to%29.md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](./drawpackedglyphs%28_,at%29.md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/fill())*
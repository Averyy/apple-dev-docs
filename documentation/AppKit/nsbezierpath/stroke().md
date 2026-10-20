# stroke()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws a line along the path using the current stroke color and drawing attributes.

**Availability**:
- macOS

## Declaration

```swift
func stroke()
```

```objc
- (void) stroke;
```

#### Discussion

The drawn line is centered on the path with its sides parallel to the path segment. This method uses the current drawing attributes associated with the receiver. If a particular attribute is not set for the receiver, this method uses the corresponding default attribute.

## See Also

### Related Documentation
- [func set()](../nscolor/set%28%29.md)
  Sets the color of subsequent drawing to the color that the color object represents.
### Drawing a Path
- [func fill()](./fill%28%29.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](./stroke%28_%29.md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func strokeLine(from: NSPoint, to: NSPoint)](./strokeline%28from,to%29.md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](./drawpackedglyphs%28_,at%29.md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/stroke())*
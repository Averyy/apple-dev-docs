# strokeLine(from:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Strokes a line between two points using the current stroke color and the default drawing attributes.

**Availability**:
- macOS

## Declaration

```swift
class func strokeLine(from point1: NSPoint, to point2: NSPoint)
```

```objc
+ (void) strokeLineFromPoint:(NSPoint) point1 toPoint:(NSPoint) point2;
```

#### Discussion

This method strokes the specified path immediately.

## Parameters

- `point1`: The starting point of the line.
- `point2`: The ending point of the line.

## See Also

### Related Documentation
- [func move(to: NSPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](./line%28to%29.md)
  Appends a straight line to the path.
### Drawing a Path
- [func stroke()](./stroke%28%29.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](./fill%28%29.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](./stroke%28_%29.md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](./drawpackedglyphs%28_,at%29.md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/strokeline(from:to:))*
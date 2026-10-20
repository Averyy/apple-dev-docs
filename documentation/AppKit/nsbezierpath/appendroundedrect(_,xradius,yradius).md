# appendRoundedRect(_:xRadius:yRadius:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends a rounded rectangular path to the path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func appendRoundedRect(_ rect: NSRect, xRadius: CGFloat, yRadius: CGFloat)
```

```objc
- (void) appendBezierPathWithRoundedRect:(NSRect) rect xRadius:(CGFloat) xRadius yRadius:(CGFloat) yRadius;
```

#### Discussion

The path is constructed in a counter-clockwise direction, starting at the top-left corner of the rectangle. If either one of the radius parameters contains the value `0.0`, the returned path is a plain rectangle without rounded corners.

## Parameters

- `rect`: The rectangle that defines the basic shape of the path.
- `xRadius`: The radius of each corner oval along the x-axis. Values larger than half the rectangle’s width are clamped to half the width.
- `yRadius`: The radius of each corner oval along the y-axis. Values larger than half the rectangle’s height are clamped to half the height.

## See Also

### Related Documentation
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](./init%28roundedrect,xradius,yradius%29.md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
### Appending Common Shapes to a Path
- [func append(NSBezierPath)](./append%28_%29.md)
  Appends the contents of the specified path object to the path.
- [func appendPoints(NSPointArray, count: Int)](./appendpoints%28_,count%29.md)
  Appends a series of line segments to the path.
- [func appendOval(in: NSRect)](./appendoval%28in%29.md)
  Appends an oval path to the path, inscribing the oval in the specified rectangle.
- [func appendArc(from: NSPoint, to: NSPoint, radius: CGFloat)](./appendarc%28from,to,radius%29.md)
  Appends an arc to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat)](./appendarc%28withcenter,radius,startangle,endangle%29.md)
  Appends an arc of a circle to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./appendarc%28withcenter,radius,startangle,endangle,clockwise%29.md)
  Appends an arc of a circle to the path.
- [func appendRect(NSRect)](./appendrect%28_%29.md)
  Appends a rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](./append%28withcgglyph,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](./append%28withcgglyphs,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendroundedrect(_:xradius:yradius:))*
# appendRect(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends a rectangular path to the path.

**Availability**:
- macOS

## Declaration

```swift
func appendRect(_ rect: NSRect)
```

```objc
- (void) appendBezierPathWithRect:(NSRect) rect;
```

#### Discussion

Before adding the rectangle, this method moves the current point to the origin of the rectangle, which implicitly closes the current subpath (if any). The path is constructed by starting at the origin of `aRect` and adding line segments in a counterclockwise direction. The final segment is added using a [`close()`](./close%28%29.md) message.

## Parameters

- `rect`: The rectangle describing the path to create.

## See Also

### Related Documentation
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](./stroke%28_%29.md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
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
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](./appendroundedrect%28_,xradius,yradius%29.md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](./append%28withcgglyph,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](./append%28withcgglyphs,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendrect(_:))*
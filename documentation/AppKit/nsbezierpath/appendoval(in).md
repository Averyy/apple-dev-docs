# appendOval(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends an oval path to the path, inscribing the oval in the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func appendOval(in rect: NSRect)
```

```objc
- (void) appendBezierPathWithOvalInRect:(NSRect) rect;
```

#### Discussion

Before adding the oval, this method moves the current point, which implicitly closes the current subpath. If the `aRect` parameter specifies a square, the inscribed path is a circle. The path is constructed by starting in the lower-right quadrant of the rectangle and adding arc segments counterclockwise to complete the oval.

## Parameters

- `rect`: The rectangle in which to inscribe the oval.

## See Also

### Appending Common Shapes to a Path
- [func append(NSBezierPath)](./append%28_%29.md)
  Appends the contents of the specified path object to the path.
- [func appendPoints(NSPointArray, count: Int)](./appendpoints%28_,count%29.md)
  Appends a series of line segments to the path.
- [func appendArc(from: NSPoint, to: NSPoint, radius: CGFloat)](./appendarc%28from,to,radius%29.md)
  Appends an arc to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat)](./appendarc%28withcenter,radius,startangle,endangle%29.md)
  Appends an arc of a circle to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./appendarc%28withcenter,radius,startangle,endangle,clockwise%29.md)
  Appends an arc of a circle to the path.
- [func appendRect(NSRect)](./appendrect%28_%29.md)
  Appends a rectangular path to the path.
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](./appendroundedrect%28_,xradius,yradius%29.md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](./append%28withcgglyph,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](./append%28withcgglyphs,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendoval(in:))*
# appendArc(withCenter:radius:startAngle:endAngle:clockwise:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends an arc of a circle to the path.

**Availability**:
- macOS

## Declaration

```swift
func appendArc(withCenter center: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)
```

```objc
- (void) appendBezierPathWithArcWithCenter:(NSPoint) center radius:(CGFloat) radius startAngle:(CGFloat) startAngle endAngle:(CGFloat) endAngle clockwise:(BOOL) clockwise;
```

#### Discussion

The created arc lies on the perimeter of the circle, between the angles specified by the `startAngle` and `endAngle` parameters. The arc is drawn in the direction indicated by the `clockwise` parameter. If the receiver’s path is empty, this method sets the current point to the beginning of the arc before adding the arc segment. If the receiver’s path is not empty, a line is drawn from the current point to the starting point of the arc.

Depending on the length of the arc, this method may add multiple connected curve segments to the path.

## Parameters

- `center`: Specifies the center point of the circle used to define the arc.
- `radius`: Specifies the radius of the circle used to define the arc.
- `startAngle`: Specifies the starting angle of the arc, measured in degrees counterclockwise from the x-axis.
- `endAngle`: Specifies the end angle of the arc, measured in degrees counterclockwise from the x-axis.
- `clockwise`: [`true`](../../Swift/true.md) if you want the arc to be drawn in a clockwise direction; otherwise [`false`](../../Swift/false.md) to draw the arc in a counterclockwise direction.

## See Also

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
- [func appendRect(NSRect)](./appendrect%28_%29.md)
  Appends a rectangular path to the path.
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](./appendroundedrect%28_,xradius,yradius%29.md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](./append%28withcgglyph,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](./append%28withcgglyphs,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendarc(withcenter:radius:startangle:endangle:clockwise:))*
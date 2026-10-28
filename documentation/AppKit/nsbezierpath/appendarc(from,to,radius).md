# appendArc(from:to:radius:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends an arc to the path.

**Availability**:
- macOS

## Declaration

```swift
func appendArc(from point1: NSPoint, to point2: NSPoint, radius: CGFloat)
```

```objc
- (void) appendBezierPathWithArcFromPoint:(NSPoint) point1 toPoint:(NSPoint) point2 radius:(CGFloat) radius;
```

## Discussion

The created arc is defined by a circle inscribed inside the angle specified by three points: the current point, the `fromPoint` parameter, and the  `toPoint` parameter (in that order). The arc itself lies on the perimeter of the circle, whose radius is specified by the `radius` parameter. The arc is drawn between the two points of the circle that are tangent to the two legs of the angle.

The arc usually does not contain the points in the `fromPoint` and `toPoint` parameters. If the starting point of the arc does not coincide with the current point, a line is drawn between the two points. The starting point of the arc lies on the line defined by the current point and the `fromPoint` parameter.

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](../../Foundation/nsexceptionname/genericexception.md) exception.

Depending on the length of the arc, this method may add multiple connected curve segments to the path.

## Parameters

- `point1`: The middle point of the angle.
- `point2`: The end point of the angle.
- `radius`: The radius of the circle inscribed in the angle.

## See Also

### Appending Common Shapes to a Path
- [func append(NSBezierPath)](./append%28_%29.md)
  Appends the contents of the specified path object to the path.
- [func appendPoints(NSPointArray, count: Int)](./appendpoints%28_,count%29.md)
  Appends a series of line segments to the path.
- [func appendOval(in: NSRect)](./appendoval%28in%29.md)
  Appends an oval path to the path, inscribing the oval in the specified rectangle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendarc(from:to:radius:))*
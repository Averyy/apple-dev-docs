# appendPoints(_:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends a series of line segments to the path.

**Availability**:
- macOS

## Declaration

```swift
func appendPoints(_ points: NSPointArray, count: Int)
```

```objc
- (void) appendBezierPathWithPoints:(NSPointArray) points count:(NSInteger) count;
```

## Discussion

This method interprets the points as a set of connected line segments.  If the current path contains an open subpath, a line is created from the last point in that subpath to the first point in the points array. If the current path is empty, the first point in the points array is used to set the starting point of the line segments. Subsequent line segments are added using the remaining points in the array.

This method does not close the path that is created. If you wish to create a closed path, you must do so by explicitly invoking the receiver’s [`close()`](./close%28%29.md) method.

## Parameters

- `points`: A C-style array of `NSPoint` data types, each of which contains the end point of the next line segment.
- `count`: The number of points in the `points` parameter.

## See Also

### Appending Common Shapes to a Path
- [func append(NSBezierPath)](./append%28_%29.md)
  Appends the contents of the specified path object to the path.
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
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](./appendroundedrect%28_,xradius,yradius%29.md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](./append%28withcgglyph,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](./append%28withcgglyphs,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/appendpoints(_:count:))*
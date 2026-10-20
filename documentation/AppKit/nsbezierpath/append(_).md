# append(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends the contents of the specified path object to the path.

**Availability**:
- macOS

## Declaration

```swift
func append(_ path: NSBezierPath)
```

```objc
- (void) appendBezierPath:(NSBezierPath *) path;
```

#### Discussion

This method adds the commands used to create `aPath` to the end of the receiver’s path. This method does not explicitly try to connect the subpaths in the two objects, although the operations in `aPath` may still cause that effect.

## Parameters

- `path`: The path to add to the receiver.

## See Also

### Appending Common Shapes to a Path
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
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](./appendroundedrect%28_,xradius,yradius%29.md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](./append%28withcgglyph,in%29.md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](./append%28withcgglyphs,count,in%29.md)
  Appends the outlines of the specified glyphs to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/append(_:))*
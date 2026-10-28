# boundingBoxOfClipPath

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the bounding box of a clipping path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var boundingBoxOfClipPath: CGRect { get }
```

```c
extern CGRect CGContextGetClipBoundingBox(CGContextRef c);
```

## Discussion

The bounding box is the smallest rectangle completely enclosing all points in the clipping path, including control points for any Bezier curves in the path.

## See Also

### Working with the Current Clipping Path
- [func clip(using: CGPathFillRule)](./clip%28using%29.md)
  Modifies the current clipping path.
- [func clip(to: CGRect)](./clip%28to%29-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: [CGRect])](./clip%28to%29-2eg0.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [func clip(to: CGRect, mask: CGImage)](./clip%28to,mask%29.md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [CGContextClip](../cgcontextclip.md)
  Modifies the current clipping path, using the nonzero winding number rule.
- [CGContextEOClip](../cgcontexteoclip.md)
  Modifies the current clipping path, using the even-odd rule.
- [CGContextClipToRects](../cgcontextcliptorects.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/boundingboxofclippath)*
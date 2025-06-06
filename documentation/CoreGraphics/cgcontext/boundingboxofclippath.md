# boundingBoxOfClipPath

**Framework**: Core Graphics  
**Kind**: property

Returns the bounding box of a clipping path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var boundingBoxOfClipPath: CGRect { get }
```

#### Discussion

The bounding box is the smallest rectangle completely enclosing all points in the clipping path, including control points for any Bezier curves in the path.

## See Also

- [func clip(using: CGPathFillRule)](cgcontext/clip(using:).md)
  Modifies the current clipping path.
- [func clip(to: CGRect)](cgcontext/clip(to:)-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: [CGRect])](cgcontext/clip(to:)-2eg0.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [func clip(to: CGRect, mask: CGImage)](cgcontext/clip(to:mask:).md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/boundingboxofclippath)*
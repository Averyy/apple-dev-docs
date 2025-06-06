# clip(to:)

**Framework**: Core Graphics  
**Kind**: method

Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func clip(to rects: [CGRect])
```

#### Discussion

This method sets the clipping path to the intersection of the current clipping path and the region within the specified rectangles.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## Parameters

- `rects`: An array of rectangles, in user space coordinates.

## See Also

- [func clip(using: CGPathFillRule)](cgcontext/clip(using:).md)
  Modifies the current clipping path.
- [func clip(to: CGRect)](cgcontext/clip(to:)-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: CGRect, mask: CGImage)](cgcontext/clip(to:mask:).md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [var boundingBoxOfClipPath: CGRect](cgcontext/boundingboxofclippath.md)
  Returns the bounding box of a clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/clip(to:)-2eg0)*
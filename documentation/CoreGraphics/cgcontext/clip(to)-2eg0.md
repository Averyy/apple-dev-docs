# clip(to:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func clip(to rects: [CGRect])
```

## Discussion

This method sets the clipping path to the intersection of the current clipping path and the region within the specified rectangles.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## Parameters

- `rects`: An array of rectangles, in user space coordinates.

## See Also

### Working with the Current Clipping Path
- [func clip(using: CGPathFillRule)](./clip%28using%29.md)
  Modifies the current clipping path.
- [func clip(to: CGRect)](./clip%28to%29-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: CGRect, mask: CGImage)](./clip%28to,mask%29.md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [var boundingBoxOfClipPath: CGRect](./boundingboxofclippath.md)
  Returns the bounding box of a clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/clip(to:)-2eg0)*
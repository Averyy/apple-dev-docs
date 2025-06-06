# clip(using:)

**Framework**: Core Graphics  
**Kind**: method

Modifies the current clipping path.

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
func clip(using rule: CGPathFillRule = .winding)
```

#### Discussion

A clipping path restricts the paintable area: painting operations take effect only for those areas in the interior of the clipping path. This method uses the specified rule to calculate the intersection of the current path with the current clipping path. The path resulting from the intersection is used as the new current clipping path for subsequent painting operations.

If the current path contains any non-closed subpaths, this method treats each subpath as if it had been closed with the [`closePath()`](cgcontext/closepath().md) method, then applies the specified rule to determine which areas to fill.

After determining the new clipping path, this method clears the context’s current path.

Unlike the current path, the current clipping path is part of the graphics state. Therefore, to re-enlarge the paintable area by restoring the clipping path to a prior state, you must save the graphics state before you clip and restore the graphics state after you’ve completed any clipped drawing.

## Parameters

- `rule`: This parameter defaults to the   rule if unspecified.

## See Also

- [func clip(to: CGRect)](cgcontext/clip(to:)-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: [CGRect])](cgcontext/clip(to:)-2eg0.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [func clip(to: CGRect, mask: CGImage)](cgcontext/clip(to:mask:).md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [var boundingBoxOfClipPath: CGRect](cgcontext/boundingboxofclippath.md)
  Returns the bounding box of a clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/clip(using:))*
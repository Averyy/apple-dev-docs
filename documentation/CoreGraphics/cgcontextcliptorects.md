# CGContextClipToRects

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextClipToRects(CGContextRef c, const CGRect *rects, size_t count);
```

## Discussion

This function sets the clipping path to the intersection of the current clipping path and the region within the specified rectangles.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## Parameters

- `c`: The graphics context for which to set the clipping path.
- `rects`: An array of rectangles. The locations and dimensions of the rectangles are specified in the user space coordinate system.
- `count`: The total number of array entries in the `rects` parameter.

## See Also

### Working with the Current Clipping Path
- [func clip(to: CGRect)](./cgcontext/clip%28to%29-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: CGRect, mask: CGImage)](./cgcontext/clip%28to,mask%29.md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [var boundingBoxOfClipPath: CGRect](./cgcontext/boundingboxofclippath.md)
  Returns the bounding box of a clipping path.
- [CGContextClip](./cgcontextclip.md)
  Modifies the current clipping path, using the nonzero winding number rule.
- [CGContextEOClip](./cgcontexteoclip.md)
  Modifies the current clipping path, using the even-odd rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextcliptorects)*
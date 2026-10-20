# clip(to:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func clip(to rect: CGRect)
```

```c
extern void CGContextClipToRect(CGContextRef c, CGRect rect);
```

#### Discussion

This function sets the specified graphics context’s clipping region to the area which intersects both the current clipping path and the specified rectangle.

After determining the new clipping path, the function resets the context’s current path to an empty path.

## Parameters

- `rect`: The location and dimensions of the rectangle, in user space, to be used in determining the new clipping path.

## See Also

### Working with the Current Clipping Path
- [func clip(using: CGPathFillRule)](./clip%28using%29.md)
  Modifies the current clipping path.
- [func clip(to: [CGRect])](./clip%28to%29-2eg0.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [func clip(to: CGRect, mask: CGImage)](./clip%28to,mask%29.md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [var boundingBoxOfClipPath: CGRect](./boundingboxofclippath.md)
  Returns the bounding box of a clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/clip(to:)-7cbwq)*
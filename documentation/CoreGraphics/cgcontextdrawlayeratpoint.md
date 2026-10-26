# CGContextDrawLayerAtPoint

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Draws the contents of a CGLayer object at the specified point.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextDrawLayerAtPoint(CGContextRef context, CGPoint point, CGLayerRef layer);
```

#### Discussion

Calling the function `CGContextDrawLayerAtPoint` is equivalent to calling the function `CGContextDrawLayerInRect` with a rectangle that has its origin at `point` and its size equal to the size of the layer.

## Parameters

- `context`: The graphics context associated with the layer.
- `point`: The location, in current user space coordinates, to use as the origin for the drawing.
- `layer`: The layer whose contents you want to draw.

## See Also

### Drawing Core Graphics Layers
- [CGContextDrawLayerInRect](./cgcontextdrawlayerinrect.md)
  Draws the contents of a layer object into the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextdrawlayeratpoint)*
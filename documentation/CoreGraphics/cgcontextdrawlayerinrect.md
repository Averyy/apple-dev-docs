# CGContextDrawLayerInRect

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Draws the contents of a layer object into the specified rectangle.

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
extern void CGContextDrawLayerInRect(CGContextRef context, CGRect rect, CGLayerRef layer);
```

#### Discussion

The contents are scaled, if necessary, to fit into the rectangle.

## Parameters

- `context`: The graphics context associated with the layer.
- `rect`: The rectangle, in current user space coordinates, to draw to.
- `layer`: The layer whose contents you want to draw.

## See Also

### Drawing Core Graphics Layers
- [CGContextDrawLayerAtPoint](./cgcontextdrawlayeratpoint.md)
  Draws the contents of a CGLayer object at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextdrawlayerinrect)*
# CGContextFillPath

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Paints the area within the current path, using the nonzero winding number rule.

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
extern void CGContextFillPath(CGContextRef c);
```

#### Discussion

Each subpath is treated as if it were closed by calling [`closePath()`](./cgcontext/closepath%28%29.md). The nonzero winding number rule is described in [Filling a Path](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211-TPXREF106) in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066). The current path is cleared as a side effect of calling this function.

## Parameters

- `c`: A graphics context that contains a path to fill.

## See Also

### Drawing the Current Graphics Path
- [func drawPath(using: CGPathDrawingMode)](./cgcontext/drawpath%28using%29.md)
  Draws the current path using the provided drawing mode.
- [enum CGPathDrawingMode](./cgpathdrawingmode.md)
  Options for rendering a path.
- [CGContextEOFillPath](./cgcontexteofillpath.md)
  Paints the area within the current path, using the even-odd fill rule.
- [func strokePath()](./cgcontext/strokepath%28%29.md)
  Paints a line along the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextfillpath)*
# CGContextStrokeLineSegments

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Strokes a sequence of line segments.

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
extern void CGContextStrokeLineSegments(CGContextRef c, const CGPoint *points, size_t count);
```

#### Discussion

This function creates a new path, adds the individual line segments to the path, and then strokes the path. The current path is cleared as a side effect of calling this function.

## Parameters

- `c`: A graphics context.
- `points`: An array of points, organized as pairs—the starting point of a line segment followed by the ending point of a line segment. For example, the first point in the array specifies the starting position of the first line, the second point specifies the ending position of the first line, the third point specifies the starting position of the second line, and so forth.
- `count`: The number of points in the `points` array.

## See Also

### Drawing Shapes
- [func clear(CGRect)](./cgcontext/clear%28_%29.md)
  Paints a transparent rectangle.
- [func fill(CGRect)](./cgcontext/fill%28_%29-7a0rk.md)
  Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [CGContextFillRects](./cgcontextfillrects.md)
  Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [func fillEllipse(in: CGRect)](./cgcontext/fillellipse%28in%29.md)
  Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [func stroke(CGRect)](./cgcontext/stroke%28_%29.md)
  Paints a rectangular path.
- [func stroke(CGRect, width: CGFloat)](./cgcontext/stroke%28_,width%29.md)
  Paints a rectangular path, using the specified line width.
- [func strokeEllipse(in: CGRect)](./cgcontext/strokeellipse%28in%29.md)
  Strokes an ellipse that fits inside the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextstrokelinesegments)*
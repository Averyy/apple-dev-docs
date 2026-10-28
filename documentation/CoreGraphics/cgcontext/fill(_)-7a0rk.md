# fill(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Paints the area contained within the provided rectangle, using the fill color in the current graphics state.

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
func fill(_ rect: CGRect)
```

```c
extern void CGContextFillRect(CGContextRef c, CGRect rect);
```

## Discussion

The current path is cleared as a side effect of calling this function.

## Parameters

- `rect`: A rectangle, in user space coordinates.

## See Also

### Drawing Shapes
- [func clear(CGRect)](./clear%28_%29.md)
  Paints a transparent rectangle.
- [func fill([CGRect])](./fill%28_%29-6jc4y.md)
  Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [func fillEllipse(in: CGRect)](./fillellipse%28in%29.md)
  Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [func stroke(CGRect)](./stroke%28_%29.md)
  Paints a rectangular path.
- [func stroke(CGRect, width: CGFloat)](./stroke%28_,width%29.md)
  Paints a rectangular path, using the specified line width.
- [func strokeEllipse(in: CGRect)](./strokeellipse%28in%29.md)
  Strokes an ellipse that fits inside the specified rectangle.
- [func strokeLineSegments(between: [CGPoint])](./strokelinesegments%28between%29.md)
  Strokes a sequence of line segments.
- [CGContextStrokeLineSegments](../cgcontextstrokelinesegments.md)
  Strokes a sequence of line segments.
### Related Documentation
- [CGContextFillRects](../cgcontextfillrects.md)
  Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/fill(_:)-7a0rk)*
# stroke(_:width:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Paints a rectangular path, using the specified line width.

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
func stroke(_ rect: CGRect, width: CGFloat)
```

```c
extern void CGContextStrokeRectWithWidth(CGContextRef c, CGRect rect, CGFloat width);
```

#### Discussion

Aside from the line width value, Core Graphics uses the current attributes of the graphics state (such as stroke color) to paint the line. The line straddles the path, with half of the total width on either side.

The current path is cleared as a side effect of calling this function.

## Parameters

- `rect`: A rectangle, in user space coordinates.
- `width`: A value, in user space units, that is greater than zero. This value does not affect the line width values in the current graphics state.

## See Also

### Drawing Shapes
- [func clear(CGRect)](./clear%28_%29.md)
  Paints a transparent rectangle.
- [func fill(CGRect)](./fill%28_%29-7a0rk.md)
  Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [func fill([CGRect])](./fill%28_%29-6jc4y.md)
  Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [func fillEllipse(in: CGRect)](./fillellipse%28in%29.md)
  Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [func stroke(CGRect)](./stroke%28_%29.md)
  Paints a rectangular path.
- [func strokeEllipse(in: CGRect)](./strokeellipse%28in%29.md)
  Strokes an ellipse that fits inside the specified rectangle.
- [func strokeLineSegments(between: [CGPoint])](./strokelinesegments%28between%29.md)
  Strokes a sequence of line segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/stroke(_:width:))*
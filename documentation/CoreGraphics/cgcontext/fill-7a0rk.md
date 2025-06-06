# fill(_:)

**Framework**: Core Graphics  
**Kind**: method

Paints the area contained within the provided rectangle, using the fill color in the current graphics state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fill(_ rect: CGRect)
```

#### Discussion

The current path is cleared as a side effect of calling this function.

## Parameters

- `rect`: A rectangle, in user space coordinates.

## See Also

- [func clear(CGRect)](cgcontext/clear(_:).md)
  Paints a transparent rectangle.
- [func fill([CGRect])](cgcontext/fill(_:)-6jc4y.md)
  Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [func fillEllipse(in: CGRect)](cgcontext/fillellipse(in:).md)
  Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [func stroke(CGRect)](cgcontext/stroke(_:).md)
  Paints a rectangular path.
- [func stroke(CGRect, width: CGFloat)](cgcontext/stroke(_:width:).md)
  Paints a rectangular path, using the specified line width.
- [func strokeEllipse(in: CGRect)](cgcontext/strokeellipse(in:).md)
  Strokes an ellipse that fits inside the specified rectangle.
- [func strokeLineSegments(between: [CGPoint])](cgcontext/strokelinesegments(between:).md)
  Strokes a sequence of line segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/fill(_:)-7a0rk)*
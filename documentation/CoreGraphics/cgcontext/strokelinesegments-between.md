# strokeLineSegments(between:)

**Framework**: Core Graphics  
**Kind**: method

Strokes a sequence of line segments.

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
func strokeLineSegments(between points: [CGPoint])
```

#### Discussion

This function creates a new path, adds the individual line segments to the path, and then strokes the path. The current path is cleared as a side effect of calling this function.

## Parameters

- `points`: An array of points, organized as pairs—the starting point of a line segment followed by the ending point of a line segment. For example, the first point in the array specifies the starting position of the first line, the second point specifies the ending position of the first line, the third point specifies the starting position of the second line, and so forth.

## See Also

- [func clear(CGRect)](cgcontext/clear(_:).md)
  Paints a transparent rectangle.
- [func fill(CGRect)](cgcontext/fill(_:)-7a0rk.md)
  Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/strokelinesegments(between:))*
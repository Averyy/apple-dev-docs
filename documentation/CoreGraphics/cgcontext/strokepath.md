# strokePath()

**Framework**: Core Graphics  
**Kind**: method

Paints a line along the current path.

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
func strokePath()
```

#### Discussion

The line width and stroke color of the context’s graphics state are used to paint the path. The current path is cleared as a side effect of calling this function.

## See Also

- [func drawPath(using: CGPathDrawingMode)](cgcontext/drawpath(using:).md)
  Draws the current path using the provided drawing mode.
- [enum CGPathDrawingMode](cgpathdrawingmode.md)
  Options for rendering a path.
- [func fillPath(using: CGPathFillRule)](cgcontext/fillpath(using:).md)
  Paints the area within the current path, as determined by the specified fill rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/strokepath())*
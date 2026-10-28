# drawPath(using:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Draws the current path using the provided drawing mode.

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
func drawPath(using mode: CGPathDrawingMode)
```

```c
extern void CGContextDrawPath(CGContextRef c, CGPathDrawingMode mode);
```

## Discussion

The current path is cleared as a side effect of calling this function.

## Parameters

- `mode`: A path drawing mode constant—[`CGPathDrawingMode.fill`](../cgpathdrawingmode/fill.md), [`CGPathDrawingMode.eoFill`](../cgpathdrawingmode/eofill.md), [`CGPathDrawingMode.stroke`](../cgpathdrawingmode/stroke.md), [`CGPathDrawingMode.fillStroke`](../cgpathdrawingmode/fillstroke.md), or [`CGPathDrawingMode.eoFillStroke`](../cgpathdrawingmode/eofillstroke.md). For a discussion of these constants, see [`CGPath`](../cgpath.md).

## See Also

### Drawing the Current Graphics Path
- [enum CGPathDrawingMode](../cgpathdrawingmode.md)
  Options for rendering a path.
- [func fillPath(using: CGPathFillRule)](./fillpath%28using%29.md)
  Paints the area within the current path, as determined by the specified fill rule.
- [func strokePath()](./strokepath%28%29.md)
  Paints a line along the current path.
### Related Documentation
- [CGContextEOFillPath](../cgcontexteofillpath.md)
  Paints the area within the current path, using the even-odd fill rule.
- [CGContextFillPath](../cgcontextfillpath.md)
  Paints the area within the current path, using the nonzero winding number rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/drawpath(using:))*
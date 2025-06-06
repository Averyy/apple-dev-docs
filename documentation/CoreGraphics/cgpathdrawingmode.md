# CGPathDrawingMode

**Framework**: Core Graphics  
**Kind**: enum

Options for rendering a path.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGPathDrawingMode
```

#### Overview

You can pass a path drawing mode constant to the function [`drawPath(using:)`](cgcontext/drawpath(using:).md) to specify how Core Graphics should paint a graphics context’s current path.

## Topics

### Constants
- [CGPathDrawingMode.fill](cgpathdrawingmode/fill.md)
  Render the area contained within the path using the non-zero winding number rule.
- [CGPathDrawingMode.eoFill](cgpathdrawingmode/eofill.md)
  Render the area within the path using the even-odd rule.
- [CGPathDrawingMode.stroke](cgpathdrawingmode/stroke.md)
  Render a line along the path.
- [CGPathDrawingMode.fillStroke](cgpathdrawingmode/fillstroke.md)
  First fill and then stroke the path, using the nonzero winding number rule.
- [CGPathDrawingMode.eoFillStroke](cgpathdrawingmode/eofillstroke.md)
  First fill and then stroke the path, using the even-odd rule.
### Initializers
- [init?(rawValue: Int32)](cgpathdrawingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func drawPath(using: CGPathDrawingMode)](cgcontext/drawpath(using:).md)
  Draws the current path using the provided drawing mode.
- [func fillPath(using: CGPathFillRule)](cgcontext/fillpath(using:).md)
  Paints the area within the current path, as determined by the specified fill rule.
- [func strokePath()](cgcontext/strokepath.md)
  Paints a line along the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode)*
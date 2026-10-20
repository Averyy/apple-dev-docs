# CGPathDrawingMode

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Options for rendering a path.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CGPathDrawingMode
```

```c
enum CGPathDrawingMode : int32_t;
```

#### Overview

You can pass a path drawing mode constant to the function [`drawPath(using:)`](./cgcontext/drawpath%28using%29.md) to specify how Core Graphics should paint a graphics context’s current path.

## Topics

### Constants
- [CGPathDrawingMode.fill](./cgpathdrawingmode/fill.md)
  Render the area contained within the path using the non-zero winding number rule.
- [CGPathDrawingMode.eoFill](./cgpathdrawingmode/eofill.md)
  Render the area within the path using the even-odd rule.
- [CGPathDrawingMode.stroke](./cgpathdrawingmode/stroke.md)
  Render a line along the path.
- [CGPathDrawingMode.fillStroke](./cgpathdrawingmode/fillstroke.md)
  First fill and then stroke the path, using the nonzero winding number rule.
- [CGPathDrawingMode.eoFillStroke](./cgpathdrawingmode/eofillstroke.md)
  First fill and then stroke the path, using the even-odd rule.
### Initializers
- [init?(rawValue: Int32)](./cgpathdrawingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Drawing the Current Graphics Path
- [func drawPath(using: CGPathDrawingMode)](./cgcontext/drawpath%28using%29.md)
  Draws the current path using the provided drawing mode.
- [func fillPath(using: CGPathFillRule)](./cgcontext/fillpath%28using%29.md)
  Paints the area within the current path, as determined by the specified fill rule.
- [func strokePath()](./cgcontext/strokepath%28%29.md)
  Paints a line along the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode)*
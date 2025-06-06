# CGLineCap

**Framework**: Core Graphics  
**Kind**: enum

Styles for rendering the endpoint of a stroked line.

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
enum CGLineCap
```

#### Overview

A line cap specifies the method used by [`strokePath()`](cgcontext/strokepath().md) to draw the endpoint of the line. To change the line cap style in a graphics context, you use the function [`setLineCap(_:)`](cgcontext/setlinecap(_:).md).

## Topics

### Constants
- [CGLineCap.butt](cglinecap/butt.md)
  A line with a squared-off end. Core Graphics draws the line to extend only to the exact endpoint of the path. This is the default.
- [CGLineCap.round](cglinecap/round.md)
  A line with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [CGLineCap.square](cglinecap/square.md)
  A line with a squared-off end. Core Graphics extends the line beyond the endpoint of the path for a distance equal to half the line width.
### Initializers
- [init?(rawValue: Int32)](cglinecap/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinecap)*
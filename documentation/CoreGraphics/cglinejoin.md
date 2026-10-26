# CGLineJoin

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Junction types for stroked lines.

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
enum CGLineJoin
```

```c
enum CGLineJoin : int32_t;
```

#### Overview

A line join specifies how [`strokePath()`](./cgcontext/strokepath%28%29.md) draws the junction between connected line segments. To set the line join style in a graphics context, you use the function [`setLineJoin(_:)`](./cgcontext/setlinejoin%28_%29.md).

## Topics

### Constants
- [CGLineJoin.miter](./cglinejoin/miter.md)
- [CGLineJoin.round](./cglinejoin/round.md)
  A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [CGLineJoin.bevel](./cglinejoin/bevel.md)
  A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.
### Initializers
- [init?(rawValue: Int32)](./cglinejoin/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [CGPathDrawingMode](./cgpathdrawingmode.md)
  Options for rendering a path.
- [CGPathElementType](./cgpathelementtype.md)
  The type of element found in a path.
- [CGLineCap](./cglinecap.md)
  Styles for rendering the endpoint of a stroked line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinejoin)*
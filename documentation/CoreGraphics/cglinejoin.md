# CGLineJoin

**Framework**: Core Graphics  
**Kind**: enum

Junction types for stroked lines.

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
enum CGLineJoin
```

#### Overview

A line join specifies how [`strokePath()`](cgcontext/strokepath().md) draws the junction between connected line segments. To set the line join style in a graphics context, you use the function [`setLineJoin(_:)`](cgcontext/setlinejoin(_:).md).

## Topics

### Constants
- [CGLineJoin.miter](cglinejoin/miter.md)
- [CGLineJoin.round](cglinejoin/round.md)
  A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [CGLineJoin.bevel](cglinejoin/bevel.md)
  A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.
### Initializers
- [init?(rawValue: Int32)](cglinejoin/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinejoin)*
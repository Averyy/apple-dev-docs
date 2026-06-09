# Edge.Corner.Style

**Framework**: SwiftUI  
**Kind**: struct

A style that describes the corner of a rectangular shape.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Style
```

#### Overview

A corner can be square, rounded with a fixed-radius curve, or rounded with a curve that’s concentric to the container shape. For more information on how to create a shape with configurable corner styles, see [`ConcentricRectangle`](concentricrectangle.md).

> **Note**: [`ConcentricRectangle`](concentricrectangle.md), [`RoundedRectangularShape`](roundedrectangularshape.md)

## Topics

### Type Properties
- [static var concentric: Edge.Corner.Style](edge/corner/style/concentric.md)
  A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius.
### Type Methods
- [static func concentric(minimum: Edge.Corner.Style?) -> Edge.Corner.Style](edge/corner/style/concentric(minimum:).md)
  A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius, with an optional minimum radius.
- [static func fixed(CGFloat) -> Edge.Corner.Style](edge/corner/style/fixed(_:).md)
  A rounded corner style where the corner’s radius is the value you provide.
### Default Implementations
- [ExpressibleByFloatLiteral Implementations](edge/corner/style/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](edge/corner/style/expressiblebyintegerliteral-implementations.md)

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/style)*
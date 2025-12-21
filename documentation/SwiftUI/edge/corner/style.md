# Edge.Corner.Style

**Framework**: SwiftUI  
**Kind**: struct

The per-corner style of a rectangular shape. A corner can be of fixed corner radius, or be concentric to the container shape. To create such a shape with configurable corner styles, call one of the initializers of [`ConcentricRectangle`](concentricrectangle.md) and pass in the style.

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

> **Note**: [`ConcentricRectangle`](concentricrectangle.md), [`RoundedRectangularShape`](roundedrectangularshape.md)

## Topics

### Type Properties
- [static var concentric: Edge.Corner.Style](edge/corner/style/concentric.md)
  The concentric corner style. When a corner is concentric to its container, it will adjust the current corner radius to ensure that the container corner radius equals to current corner radius plus the distance between corners.
### Type Methods
- [static func concentric(minimum: Edge.Corner.Style?) -> Edge.Corner.Style](edge/corner/style/concentric(minimum:).md)
  The concentric corner style with an optional minimum corner style. When a corner is concentric to its container, it will adjust the current corner radius to ensure that the container corner radius equals to current corner radius plus the distance between corners. If the current corner is too far away from the container corner, the radius will be resolved as zero unless a minimum corner style is provided.
- [static func fixed(CGFloat) -> Edge.Corner.Style](edge/corner/style/fixed(_:).md)
  The fixed radius corner style.
### Default Implementations
- [ExpressibleByFloatLiteral Implementations](edge/corner/style/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](edge/corner/style/expressiblebyintegerliteral-implementations.md)

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/style)*
# Edge.Corner.Style

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

A corner can be square, rounded with a fixed-radius curve, or rounded with a curve that’s concentric to the container shape. For more information on how to create a shape with configurable corner styles, see [`ConcentricRectangle`](../../concentricrectangle.md).

> **See Also**: [`ConcentricRectangle`](../../concentricrectangle.md), [`RoundedRectangularShape`](../../roundedrectangularshape.md)

## Topics

### Type Properties
- [static var concentric: Edge.Corner.Style](./style/concentric.md)
  A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius.
### Type Methods
- [static func concentric(minimum: Edge.Corner.Style?) -> Edge.Corner.Style](./style/concentric%28minimum%29.md)
  A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius, with an optional minimum radius.
- [static func fixed(CGFloat) -> Edge.Corner.Style](./style/fixed%28_%29.md)
  A rounded corner style where the corner’s radius is the value you provide.
### Default Implementations
- [ExpressibleByFloatLiteral Implementations](./style/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./style/expressiblebyintegerliteral-implementations.md)

## Relationships

### Conforms To
- [Animatable](../../animatable.md)
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [ExpressibleByFloatLiteral](../../../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../../../Swift/expressiblebyintegerliteral.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/style)*
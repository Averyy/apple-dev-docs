# GraphicsContext.FilterOptions

**Framework**: SwiftUI  
**Kind**: struct

Options that configure a filter that you add to a graphics context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
struct FilterOptions
```

#### Overview

You can use filter options to configure a [`GraphicsContext.Filter`](graphicscontext/filter.md) that you apply to a [`GraphicsContext`](graphicscontext.md) with the [`addFilter(_:options:)`](graphicscontext/addfilter(_:options:).md) method.

## Topics

### Getting filter options
- [static var linearColor: GraphicsContext.FilterOptions](graphicscontext/filteroptions/linearcolor.md)
  An option that causes the filter to perform calculations in a linear color space.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func addFilter(GraphicsContext.Filter, options: GraphicsContext.FilterOptions)](graphicscontext/addfilter(_:options:).md)
  Adds a filter that applies to subsequent drawing operations.
- [GraphicsContext.Filter](graphicscontext/filter.md)
  A type that applies image processing operations to rendered content.
- [GraphicsContext.BlurOptions](graphicscontext/bluroptions.md)
  Options that configure the graphics context filter that creates blur.
- [GraphicsContext.ShadowOptions](graphicscontext/shadowoptions.md)
  Options that configure the graphics context filter that creates shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filteroptions)*
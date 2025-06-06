# GraphicsContext.BlurOptions

**Framework**: SwiftUI  
**Kind**: struct

Options that configure the graphics context filter that creates blur.

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
struct BlurOptions
```

#### Overview

You can use a set of these options when you call [`blur(radius:options:)`](graphicscontext/filter/blur(radius:options:).md) to create a [`GraphicsContext.Filter`](graphicscontext/filter.md) that adds blur to an object that you draw into a [`GraphicsContext`](graphicscontext.md).

## Topics

### Getting blur options
- [static var dithersResult: GraphicsContext.BlurOptions](graphicscontext/bluroptions/dithersresult.md)
  An option that causes the filter to dither the result, to reduce banding.
- [static var opaque: GraphicsContext.BlurOptions](graphicscontext/bluroptions/opaque.md)
  An option that causes the filter to ensure the result is completely opaque.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func addFilter(GraphicsContext.Filter, options: GraphicsContext.FilterOptions)](graphicscontext/addfilter(_:options:).md)
  Adds a filter that applies to subsequent drawing operations.
- [GraphicsContext.Filter](graphicscontext/filter.md)
  A type that applies image processing operations to rendered content.
- [GraphicsContext.FilterOptions](graphicscontext/filteroptions.md)
  Options that configure a filter that you add to a graphics context.
- [GraphicsContext.ShadowOptions](graphicscontext/shadowoptions.md)
  Options that configure the graphics context filter that creates shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/bluroptions)*
# GraphicsContext.ShadowOptions

**Framework**: SwiftUI  
**Kind**: struct

Options that configure the graphics context filter that creates shadows.

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
struct ShadowOptions
```

#### Overview

You can use a set of these options when you call [`shadow(color:radius:x:y:blendMode:options:)`](graphicscontext/filter/shadow(color:radius:x:y:blendmode:options:).md) to create a [`GraphicsContext.Filter`](graphicscontext/filter.md) that adds a drop shadow to an object that you draw into a [`GraphicsContext`](graphicscontext.md).

## Topics

### Getting shadow options
- [static var disablesGroup: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/disablesgroup.md)
  An option that causes the filter to composite the object and its shadow separately in the current layer.
- [static var invertsAlpha: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/invertsalpha.md)
  An option that causes the filter to invert the alpha of the shadow.
- [static var shadowAbove: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/shadowabove.md)
  An option that causes the filter to draw the shadow above the object, rather than below it.
- [static var shadowOnly: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/shadowonly.md)
  An option that causes the filter to draw only the shadow, and omit the source object.

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
- [GraphicsContext.BlurOptions](graphicscontext/bluroptions.md)
  Options that configure the graphics context filter that creates blur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shadowoptions)*
# GraphicsContext.BlurOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

You can use a set of these options when you call [`blur(radius:options:)`](./filter/blur%28radius,options%29.md) to create a [`GraphicsContext.Filter`](./filter.md) that adds blur to an object that you draw into a [`GraphicsContext`](../graphicscontext.md).

## Topics

### Getting blur options
- [static var dithersResult: GraphicsContext.BlurOptions](./bluroptions/dithersresult.md)
  An option that causes the filter to dither the result, to reduce banding.
- [static var opaque: GraphicsContext.BlurOptions](./bluroptions/opaque.md)
  An option that causes the filter to ensure the result is completely opaque.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Filtering
- [func addFilter(GraphicsContext.Filter, options: GraphicsContext.FilterOptions)](./addfilter%28_,options%29.md)
  Adds a filter that applies to subsequent drawing operations.
- [GraphicsContext.Filter](./filter.md)
  A type that applies image processing operations to rendered content.
- [GraphicsContext.FilterOptions](./filteroptions.md)
  Options that configure a filter that you add to a graphics context.
- [GraphicsContext.ShadowOptions](./shadowoptions.md)
  Options that configure the graphics context filter that creates shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/bluroptions)*
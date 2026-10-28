# GraphicsContext.FilterOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

You can use filter options to configure a [`GraphicsContext.Filter`](./filter.md) that you apply to a [`GraphicsContext`](../graphicscontext.md) with the [`addFilter(_:options:)`](./addfilter%28_,options%29.md) method.

## Topics

### Getting filter options
- [static var linearColor: GraphicsContext.FilterOptions](./filteroptions/linearcolor.md)
  An option that causes the filter to perform calculations in a linear color space.

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
- [GraphicsContext.BlurOptions](./bluroptions.md)
  Options that configure the graphics context filter that creates blur.
- [GraphicsContext.ShadowOptions](./shadowoptions.md)
  Options that configure the graphics context filter that creates shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filteroptions)*
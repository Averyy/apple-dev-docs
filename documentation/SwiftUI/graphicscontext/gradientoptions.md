# GraphicsContext.GradientOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Options that affect the rendering of color gradients.

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
struct GradientOptions
```

## Overview

Use these options to affect how SwiftUI manages a gradient that you create for a [`GraphicsContext.Shading`](./shading.md) instance for use in a [`GraphicsContext`](../graphicscontext.md).

## Topics

### Getting gradient options
- [static var linearColor: GraphicsContext.GradientOptions](./gradientoptions/linearcolor.md)
  An option that interpolates between colors in a linear color space.
- [static var mirror: GraphicsContext.GradientOptions](./gradientoptions/mirror.md)
  An option that repeats the gradient outside its nominal range, reflecting every other instance.
- [static var `repeat`: GraphicsContext.GradientOptions](./gradientoptions/repeat.md)
  An option that repeats the gradient outside its nominal range.

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

### Drawing a path
- [func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)](./stroke%28_,with,linewidth%29.md)
  Draws a path into the context with a specified line width.
- [func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)](./stroke%28_,with,style%29.md)
  Draws a path into the context with a specified stroke style.
- [func fill(Path, with: GraphicsContext.Shading, style: FillStyle)](./fill%28_,with,style%29.md)
  Draws a path into the context and fills the outlined region.
- [GraphicsContext.Shading](./shading.md)
  A color or pattern that you can use to outline or fill a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/gradientoptions)*
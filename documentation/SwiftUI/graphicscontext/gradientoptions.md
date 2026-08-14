# GraphicsContext.GradientOptions

**Framework**: SwiftUI  
**Kind**: struct

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

#### Overview

Use these options to affect how SwiftUI manages a gradient that you create for a [`GraphicsContext.Shading`](graphicscontext/shading.md) instance for use in a [`GraphicsContext`](graphicscontext.md).

## Topics

### Getting gradient options
- [static var linearColor: GraphicsContext.GradientOptions](graphicscontext/gradientoptions/linearcolor.md)
  An option that interpolates between colors in a linear color space.
- [static var mirror: GraphicsContext.GradientOptions](graphicscontext/gradientoptions/mirror.md)
  An option that repeats the gradient outside its nominal range, reflecting every other instance.
- [static var `repeat`: GraphicsContext.GradientOptions](graphicscontext/gradientoptions/repeat.md)
  An option that repeats the gradient outside its nominal range.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)](graphicscontext/stroke(_:with:linewidth:).md)
  Draws a path into the context with a specified line width.
- [func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)](graphicscontext/stroke(_:with:style:).md)
  Draws a path into the context with a specified stroke style.
- [func fill(Path, with: GraphicsContext.Shading, style: FillStyle)](graphicscontext/fill(_:with:style:).md)
  Draws a path into the context and fills the outlined region.
- [GraphicsContext.Shading](graphicscontext/shading.md)
  A color or pattern that you can use to outline or fill a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/gradientoptions)*
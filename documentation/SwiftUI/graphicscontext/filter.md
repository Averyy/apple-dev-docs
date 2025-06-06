# GraphicsContext.Filter

**Framework**: SwiftUI  
**Kind**: struct

A type that applies image processing operations to rendered content.

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
struct Filter
```

#### Overview

Create and configure a filter that produces an image processing effect, like adding a drop shadow or a blur effect, by calling one of the factory methods defined by the `Filter` structure. Call the [`addFilter(_:options:)`](graphicscontext/addfilter(_:options:).md) method to add the filter to a [`GraphicsContext`](graphicscontext.md). The filter only affects content that you draw into the context after adding the filter.

## Topics

### Changing brightness and contrast
- [static func brightness(Double) -> GraphicsContext.Filter](graphicscontext/filter/brightness(_:).md)
  Returns a filter that applies a brightness adjustment.
- [static func contrast(Double) -> GraphicsContext.Filter](graphicscontext/filter/contrast(_:).md)
  Returns a filter that applies a contrast adjustment.
### Manipulating color
- [static func saturation(Double) -> GraphicsContext.Filter](graphicscontext/filter/saturation(_:).md)
  Returns a filter that applies a saturation adjustment.
- [static func colorInvert(Double) -> GraphicsContext.Filter](graphicscontext/filter/colorinvert(_:).md)
  Returns a filter that inverts the color of their results.
- [static func colorMultiply(Color) -> GraphicsContext.Filter](graphicscontext/filter/colormultiply(_:).md)
  Returns a filter that multiplies each color component by the matching component of a given color.
- [static func hueRotation(Angle) -> GraphicsContext.Filter](graphicscontext/filter/huerotation(_:).md)
  Returns a filter that applies a hue rotation adjustment.
- [static func grayscale(Double) -> GraphicsContext.Filter](graphicscontext/filter/grayscale(_:).md)
  Returns a filter that applies a grayscale adjustment.
- [static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter](graphicscontext/filter/colormatrix(_:).md)
  Returns a filter that multiplies by a given color matrix.
### Adding blur
- [static func blur(radius: CGFloat, options: GraphicsContext.BlurOptions) -> GraphicsContext.Filter](graphicscontext/filter/blur(radius:options:).md)
  Returns a filter that applies a Gaussian blur.
### Adding a shadow
- [static func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat, blendMode: GraphicsContext.BlendMode, options: GraphicsContext.ShadowOptions) -> GraphicsContext.Filter](graphicscontext/filter/shadow(color:radius:x:y:blendmode:options:).md)
  Returns a filter that adds a shadow.
### Adjusting opacity
- [static var luminanceToAlpha: GraphicsContext.Filter](graphicscontext/filter/luminancetoalpha.md)
  Returns a filter that sets the opacity of each pixel based on its luminance.
- [static func alphaThreshold(min: Double, max: Double, color: Color) -> GraphicsContext.Filter](graphicscontext/filter/alphathreshold(min:max:color:).md)
  Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.
### Adding a transformation
- [static func projectionTransform(ProjectionTransform) -> GraphicsContext.Filter](graphicscontext/filter/projectiontransform(_:).md)
  Returns a filter that that transforms the rasterized form of subsequent graphics primitives.
### Using a custom Metal shader
- [static func colorShader(Shader) -> GraphicsContext.Filter](graphicscontext/filter/colorshader(_:).md)
  Returns a filter that applies `shader` to the color of each source pixel.
- [static func distortionShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](graphicscontext/filter/distortionshader(_:maxsampleoffset:).md)
  Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.
- [static func layerShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](graphicscontext/filter/layershader(_:maxsampleoffset:).md)
  Returns a filter that applies `shader` to the contents of the source layer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func addFilter(GraphicsContext.Filter, options: GraphicsContext.FilterOptions)](graphicscontext/addfilter(_:options:).md)
  Adds a filter that applies to subsequent drawing operations.
- [GraphicsContext.FilterOptions](graphicscontext/filteroptions.md)
  Options that configure a filter that you add to a graphics context.
- [GraphicsContext.BlurOptions](graphicscontext/bluroptions.md)
  Options that configure the graphics context filter that creates blur.
- [GraphicsContext.ShadowOptions](graphicscontext/shadowoptions.md)
  Options that configure the graphics context filter that creates shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter)*
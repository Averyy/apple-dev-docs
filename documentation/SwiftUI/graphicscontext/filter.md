# GraphicsContext.Filter

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

Create and configure a filter that produces an image processing effect, like adding a drop shadow or a blur effect, by calling one of the factory methods defined by the `Filter` structure. Call the [`addFilter(_:options:)`](./addfilter%28_,options%29.md) method to add the filter to a [`GraphicsContext`](../graphicscontext.md). The filter only affects content that you draw into the context after adding the filter.

## Topics

### Changing brightness and contrast
- [static func brightness(Double) -> GraphicsContext.Filter](./filter/brightness%28_%29.md)
  Returns a filter that applies a brightness adjustment.
- [static func contrast(Double) -> GraphicsContext.Filter](./filter/contrast%28_%29.md)
  Returns a filter that applies a contrast adjustment.
### Manipulating color
- [static func saturation(Double) -> GraphicsContext.Filter](./filter/saturation%28_%29.md)
  Returns a filter that applies a saturation adjustment.
- [static func colorInvert(Double) -> GraphicsContext.Filter](./filter/colorinvert%28_%29.md)
  Returns a filter that inverts the color of their results.
- [static func colorMultiply(Color) -> GraphicsContext.Filter](./filter/colormultiply%28_%29.md)
  Returns a filter that multiplies each color component by the matching component of a given color.
- [static func hueRotation(Angle) -> GraphicsContext.Filter](./filter/huerotation%28_%29.md)
  Returns a filter that applies a hue rotation adjustment.
- [static func grayscale(Double) -> GraphicsContext.Filter](./filter/grayscale%28_%29.md)
  Returns a filter that applies a grayscale adjustment.
- [static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter](./filter/colormatrix%28_%29.md)
  Returns a filter that multiplies by a given color matrix.
### Adding blur
- [static func blur(radius: CGFloat, options: GraphicsContext.BlurOptions) -> GraphicsContext.Filter](./filter/blur%28radius,options%29.md)
  Returns a filter that applies a Gaussian blur.
### Adding a shadow
- [static func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat, blendMode: GraphicsContext.BlendMode, options: GraphicsContext.ShadowOptions) -> GraphicsContext.Filter](./filter/shadow%28color,radius,x,y,blendmode,options%29.md)
  Returns a filter that adds a shadow.
### Adjusting opacity
- [static var luminanceToAlpha: GraphicsContext.Filter](./filter/luminancetoalpha.md)
  Returns a filter that sets the opacity of each pixel based on its luminance.
- [static func alphaThreshold(min: Double, max: Double, color: Color) -> GraphicsContext.Filter](./filter/alphathreshold%28min,max,color%29.md)
  Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.
### Adding a transformation
- [static func projectionTransform(ProjectionTransform) -> GraphicsContext.Filter](./filter/projectiontransform%28_%29.md)
  Returns a filter that transforms the rasterized form of subsequent graphics primitives.
### Using a custom Metal shader
- [static func colorShader(Shader) -> GraphicsContext.Filter](./filter/colorshader%28_%29.md)
  Returns a filter that applies `shader` to the color of each source pixel.
- [static func distortionShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](./filter/distortionshader%28_,maxsampleoffset%29.md)
  Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.
- [static func layerShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](./filter/layershader%28_,maxsampleoffset%29.md)
  Returns a filter that applies `shader` to the contents of the source layer.
### Type Methods
- [static func alphaMultiply(Color) -> GraphicsContext.Filter](./filter/alphamultiply%28_%29.md)
  Returns a filter that multiplies the alpha component by a given color.
- [static func colorMatrix(ColorMatrix, isPremultiplied: Bool) -> GraphicsContext.Filter](./filter/colormatrix%28_,ispremultiplied%29.md)
  Returns a filter that multiplies by a given color matrix.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Filtering
- [func addFilter(GraphicsContext.Filter, options: GraphicsContext.FilterOptions)](./addfilter%28_,options%29.md)
  Adds a filter that applies to subsequent drawing operations.
- [GraphicsContext.FilterOptions](./filteroptions.md)
  Options that configure a filter that you add to a graphics context.
- [GraphicsContext.BlurOptions](./bluroptions.md)
  Options that configure the graphics context filter that creates blur.
- [GraphicsContext.ShadowOptions](./shadowoptions.md)
  Options that configure the graphics context filter that creates shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter)*
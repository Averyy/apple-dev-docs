# GraphicsContext.Shading

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A color or pattern that you can use to outline or fill a path.

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
struct Shading
```

## Overview

Use a shading instance to describe the color or pattern of a path that you outline with a method like [`stroke(_:with:style:)`](./stroke%28_,with,style%29.md), or of the interior of a region that you fill with the [`fill(_:with:style:)`](./fill%28_,with,style%29.md) method. Get a shading instance by calling one of the `Shading` structure’s factory methods. You can base shading on:

- A [`Color`](../color.md).
- A [`Gradient`](../gradient.md).
- Any type that conforms to [`ShapeStyle`](../shapestyle.md).
- An [`Image`](../image.md).
- What you’ve already drawn into the context.
- A collection of other shading instances.

## Topics

### Colors
- [static func color(Color) -> GraphicsContext.Shading](./shading/color%28_%29.md)
  Returns a shading instance that fills with a color.
- [static func color(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double) -> GraphicsContext.Shading](./shading/color%28_,red,green,blue,opacity%29.md)
  Returns a shading instance that fills with a color in the given color space.
- [static func color(Color.RGBColorSpace, white: Double, opacity: Double) -> GraphicsContext.Shading](./shading/color%28_,white,opacity%29.md)
  Returns a shading instance that fills with a monochrome color in the given color space.
### Gradients
- [static linearGradient(_:startPoint:endPoint:options:)](./shading/lineargradient%28_,startpoint,endpoint,options%29.md)
  Returns a shading instance that fills a linear (axial) gradient.
- [static radialGradient(_:center:startRadius:endRadius:options:)](./shading/radialgradient%28_,center,startradius,endradius,options%29.md)
  Returns a shading instance that fills a radial gradient.
- [static conicGradient(_:center:angle:options:)](./shading/conicgradient%28_,center,angle,options%29.md)
  Returns a shading instance that fills a conic (angular) gradient.
### Other shape styles
- [static func style<S>(S) -> GraphicsContext.Shading](./shading/style%28_%29.md)
  Returns a shading instance that fills with the given shape style.
- [static var foreground: GraphicsContext.Shading](./shading/foreground.md)
  A shading instance that fills with the foreground style from the graphics context’s environment.
### Images
- [static func tiledImage(Image, origin: CGPoint, sourceRect: CGRect, scale: CGFloat) -> GraphicsContext.Shading](./shading/tiledimage%28_,origin,sourcerect,scale%29.md)
  Returns a shading instance that tiles an image across the infinite plane.
### Composite shading types
- [static func palette([GraphicsContext.Shading]) -> GraphicsContext.Shading](./shading/palette%28_%29.md)
  Returns a multilevel shading instance constructed from an array of shading instances.
- [static var backdrop: GraphicsContext.Shading](./shading/backdrop.md)
  A shading instance that draws a copy of the current background.
### Using a custom Metal shader
- [static func shader(Shader, bounds: CGRect) -> GraphicsContext.Shading](./shading/shader%28_,bounds%29.md)
  Returns a shading instance that fills with the results of querying a shader for each pixel.
### Type Methods
- [static func meshGradient(MeshGradient) -> GraphicsContext.Shading](./shading/meshgradient%28_%29.md)
  Returns a shading instance that fills with a mesh gradient.
- [static radialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)](./shading/radialgradient%28_,startcenter,startradius,endcenter,endradius,options%29.md)
  Returns a shading that fills a two-point radial gradient.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Drawing a path
- [func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)](./stroke%28_,with,linewidth%29.md)
  Draws a path into the context with a specified line width.
- [func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)](./stroke%28_,with,style%29.md)
  Draws a path into the context with a specified stroke style.
- [func fill(Path, with: GraphicsContext.Shading, style: FillStyle)](./fill%28_,with,style%29.md)
  Draws a path into the context and fills the outlined region.
- [GraphicsContext.GradientOptions](./gradientoptions.md)
  Options that affect the rendering of color gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading)*
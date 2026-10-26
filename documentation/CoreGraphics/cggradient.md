# CGGradient

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A definition for a smooth transition between colors for drawing radial and axial gradient fills.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CGGradient
```

```c
typedef struct CGGradient * CGGradientRef;
```

#### Overview

A gradient defines a smooth transition between colors across an area. A `CGGradient` has a color space, two or more colors, and a location for each color. The color space cannot be a pattern or indexed color space, otherwise it can be any Core Graphics color space ([`CGColorSpace`](./cgcolorspace.md)).

Colors can be provided as component values (such as red, green, blue) or as Core Graphics color objects ([`CGColor`](./cgcolor.md)). Component values can vary from 0.0 to 1.0, designating the proportion of the component present in the color.

A location is a normalized value. When it comes time to paint the gradient, Core Graphics maps the normalized location values to the points in coordinate space that you provide.

For more precise control over gradients, see [`CGShading`](./cgshading.md).

## Topics

### Creating Gradient Instances
- [init?(colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](./cggradient/init%28colorspace,colorcomponents,locations,count%29.md)
  Creates a CGGradient object from a color space and the provided color components and locations.
- [init?(colorsSpace: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)](./cggradient/init%28colorsspace,colors,locations%29.md)
  Creates a gradient object from a color space and the provided color objects and locations.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cggradient/typeid.md)
  Returns the Core Foundation type identifier for CGGradient objects.
### Initializers
- [init?(headroom: Float, colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](./cggradient/init%28headroom,colorspace,colorcomponents,locations,count%29.md)
### Instance Properties
- [var contentHeadroom: Float](./cggradient/contentheadroom.md)
### Retaining and Releasing a Gradient
- [CGGradientRelease](./cggradientrelease.md)
  Decrements the retain count of a CGGradient object.
- [CGGradientRetain](./cggradientretain.md)
  Increments the retain count of a CGGradient object.
### Constants
- [CGGradientDrawingOptions](./cggradientdrawingoptions.md)
  Drawing locations for gradients.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Utility and Support Classes
- [class CGDataConsumer](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGDataProvider](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](./cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGFunction](./cgfunction.md)
  A general facility for defining and using callback functions.
- [class CGPattern](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
### Opaque Types
- [CGContextRef](./cgcontext.md)
  A Quartz 2D drawing environment.
- [CGColorRef](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfoRef](./cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpaceRef](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [CGFontRef](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
- [CGImageRef](./cgimage.md)
  A bitmap image or image mask.
- [CGLayerRef](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
- [CGPathRef](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradient)*
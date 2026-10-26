# CGShading

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.

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
class CGShading
```

```c
typedef struct CGShading * CGShadingRef;
```

#### Overview

Shading means to fill using a smooth transition between colors across an area. You create a shading using a custom function with a [`CGFunction`](./cgfunction.md) instance. To paint with a Core Graphics shading, you call [`drawShading(_:)`](./cgcontext/drawshading%28_%29.md). This function fills the current clipping path using the specified color gradient, calling your parametric function repeatedly as it draws.

An alternative to using a `CGShading` instance is to use the [`CGGradient`](./cggradient.md) type. For applications that run in macOS 10.5 and later, `CGGradient` objects are much simpler to use.

## Topics

### Creating Shading Objects
- [init?(axialSpace: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)](./cgshading/init%28axialspace,start,end,function,extendstart,extendend%29.md)
  Creates a shading object to use for axial shading.
- [init?(radialSpace: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)](./cgshading/init%28radialspace,start,startradius,end,endradius,function,extendstart,extendend%29.md)
  Creates a shading object to use for radial shading.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgshading/typeid.md)
  Returns the Core Foundation type identifier for Core Graphics shading objects.
### Initializers
- [init?(axialHeadroom: Float, space: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)](./cgshading/init%28axialheadroom,space,start,end,function,extendstart,extendend%29.md)
- [init?(radialHeadroom: Float, space: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)](./cgshading/init%28radialheadroom,space,start,startradius,end,endradius,function,extendstart,extendend%29.md)
### Instance Properties
- [var contentHeadroom: Float](./cgshading/contentheadroom.md)
### Retaining and Releasing Shading Objects
- [CGShadingRetain](./cgshadingretain.md)
  Increments the retain count of a shading object.
- [CGShadingRelease](./cgshadingrelease.md)
  Decrements the retain count of a shading object.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### Utility and Support Classes
- [class CGDataConsumer](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGDataProvider](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGGradient](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgshading)*
# CGLayer

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

An offscreen context for reusing content drawn with Core Graphics.

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
class CGLayer
```

```c
typedef struct CGLayer * CGLayerRef;
```

## Topics

### Creating Layer Objects
- [init?(CGContext, size: CGSize, auxiliaryInfo: CFDictionary?)](./cglayer/init%28_,size,auxiliaryinfo%29.md)
  Creates a layer object that is associated with a graphics context.
### Examining a Layer
- [var context: CGContext?](./cglayer/context.md)
  Returns the graphics context associated with a layer object.
- [var size: CGSize](./cglayer/size.md)
  Returns the width and height of a layer object.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cglayer/typeid.md)
  Returns the unique type identifier used for [`CGLayer`](./cglayer.md) objects.
### Retaining and Releasing Color Objects
- [CGLayerRetain](./cglayerretain.md)
  Increments the retain count of a layer object.
- [CGLayerRelease](./cglayerrelease.md)
  Decrements the retain count of a layer object.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### 2D Drawing
- [class CGContext](./cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](./cgimage.md)
  A bitmap image or image mask.
- [class CGPath](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGMutablePath](./cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
### Opaque Types
- [CGColorRef](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfoRef](./cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpaceRef](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [CGDataConsumerRef](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProviderRef](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGFontRef](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
- [CGFunctionRef](./cgfunction.md)
  A general facility for defining and using callback functions.
- [CGGradientRef](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGPatternRef](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayer)*
# CGPattern

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A 2D pattern to be used for drawing graphics paths.

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
class CGPattern
```

```c
typedef struct CGPattern * CGPatternRef;
```

#### Overview

Core Graphics tiles the pattern cell for you, based on parameters you specify when you call [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](./cgpattern/init%28info,bounds,matrix,xstep,ystep,tiling,iscolored,callbacks%29.md).

To create a dashed line, see [`CGContextSetLineDash`](./cgcontextsetlinedash.md).

## Topics

### Creating a Pattern
- [init?(info: UnsafeMutableRawPointer?, bounds: CGRect, matrix: CGAffineTransform, xStep: CGFloat, yStep: CGFloat, tiling: CGPatternTiling, isColored: Bool, callbacks: UnsafePointer<CGPatternCallbacks>)](./cgpattern/init%28info,bounds,matrix,xstep,ystep,tiling,iscolored,callbacks%29.md)
  Creates a pattern object.
### Callbacks
- [struct CGPatternCallbacks](./cgpatterncallbacks.md)
  A structure that holds a version and two callback functions for drawing a custom pattern.
- [typealias CGPatternDrawPatternCallback](./cgpatterndrawpatterncallback.md)
  Draws a pattern cell.
- [typealias CGPatternReleaseInfoCallback](./cgpatternreleaseinfocallback.md)
  Release private data or resources associated with the pattern.
### Constants
- [enum CGPatternTiling](./cgpatterntiling.md)
  Different methods for rendering a tiled pattern.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgpattern/typeid.md)
  Returns the type identifier for Core Graphics patterns.
### Retaining and Releasing a Pattern
- [CGPatternRetain](./cgpatternretain.md)
  Increments the retain count of a Core Graphics pattern.
- [CGPatternRelease](./cgpatternrelease.md)
  Decrements the retain count of a Core Graphics pattern.

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
- [class CGShading](./cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGGradient](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGFunction](./cgfunction.md)
  A general facility for defining and using callback functions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpattern)*
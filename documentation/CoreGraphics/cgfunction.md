# CGFunction

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A general facility for defining and using callback functions.

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
class CGFunction
```

```c
typedef struct CGFunction * CGFunctionRef;
```

#### Overview

These functions can take an arbitrary number of floating-point input values and pass back an arbitrary number of floating-point output values.

Core Graphics uses function objects to implement shadings. [`CGShading`](./cgshading.md) describes the parameters and semantics required for the callbacks used by function objects.

## Topics

### Creating Function Objects
- [init?(info: UnsafeMutableRawPointer?, domainDimension: Int, domain: UnsafePointer<CGFloat>?, rangeDimension: Int, range: UnsafePointer<CGFloat>?, callbacks: UnsafePointer<CGFunctionCallbacks>)](./cgfunction/init%28info,domaindimension,domain,rangedimension,range,callbacks%29.md)
  Creates a Core Graphics function.
### Callbacks
- [struct CGFunctionCallbacks](./cgfunctioncallbacks.md)
  A structure that contains callbacks needed by a `CGFunctionRef` object.
- [typealias CGFunctionEvaluateCallback](./cgfunctionevaluatecallback.md)
  Performs custom operations on the supplied input data to produce output data.
- [typealias CGFunctionReleaseInfoCallback](./cgfunctionreleaseinfocallback.md)
  Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgfunction/typeid.md)
  Returns the type identifier for Core Graphics function objects.
### Retaining and Releasing CGFunction Objects
- [CGFunctionRelease](./cgfunctionrelease.md)
  Decrements the retain count of a function object.
- [CGFunctionRetain](./cgfunctionretain.md)
  Increments the retain count of a function object.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunction)*
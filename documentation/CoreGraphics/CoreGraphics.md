# Core Graphics

**Framework**: Core Graphics  
**Kind**: module

Harness the power of Quartz technology to perform lightweight 2D rendering with high-fidelity output. Handle path-based drawing, antialiased rendering, gradients, images, color management, PDF documents, and more.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

The Core Graphics framework is based on the Quartz advanced drawing engine. It provides low-level, lightweight 2D rendering with unmatched output fidelity. You use this framework to handle path-based drawing, transformations, color management, offscreen rendering, patterns, gradients and shadings, image data management, image creation, and image masking, as well as PDF document creation, display, and parsing.

In macOS, Core Graphics also includes services for working with display hardware, low-level user input events, and the windowing system.

## Topics

### Geometric Data Types
- [@frozen struct CGFloat](../CoreFoundation/CGFloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](../CoreFoundation/CGPoint.md)
- [struct CGSize](../CoreFoundation/CGSize.md)
  A structure that contains width and height values.
- [struct CGRect](../CoreFoundation/CGRect.md)
- [struct CGVector](../CoreFoundation/CGVector.md)
  A structure that contains a two-dimensional vector.
- [struct CGAffineTransform](../CoreFoundation/CGAffineTransform.md)
### 2D Drawing
- [class CGContext](cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](cgimage.md)
  A bitmap image or image mask.
- [class CGPath](cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGMutablePath](cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
### Colors and Fonts
- [class CGColor](cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [class CGColorConversionInfo](cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [class CGColorSpace](cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [class CGFont](cgfont.md)
  A set of character glyphs and layout information for drawing text.
### Working with PDF Documents
- [class CGPDFDocument](cgpdfdocument.md)
  A document that contains PDF (Portable Document Format) drawing information.
### Utility and Support Classes
- [class CGDataConsumer](cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGDataProvider](cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGGradient](cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGFunction](cgfunction.md)
  A general facility for defining and using callback functions.
- [class CGPattern](cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
### Services
- [Quartz Display Services](quartz-display-services.md)
  Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- [Quartz Event Services](quartz-event-services.md)
  Provides features for managing —filters for observing and altering the stream of low-level user input events in macOS.
- [Quartz Window Services](quartz-window-services.md)
  Provides information about the windows managed by the macOS window server.
### Reference
- [Core Graphics Structures](core-graphics-structures.md)
- [Core Graphics Enumerations](core-graphics-enumerations.md)
- [Core Graphics Constants](core-graphics-constants.md)
- [Core Graphics Functions](core-graphics-functions.md)
- [Core Graphics Data Types](core-graphics-data-types.md)
### Classes
- [class CGPDFWrappedObject](cgpdfwrappedobject.md)
  CGPDFWrappedObject is used to add a PDF object to a CGPDFArray or CGPDFDictionary.
- [class CGRenderingBufferProvider](cgrenderingbufferprovider.md)
### Protocols
- [protocol PDFObjectType](pdfobjecttype.md)
### Structures
- [struct CGBitmapParameters](cgbitmapparameters-4v8wo.md)
- [struct CGColorModel](cgcolormodel.md)
- [struct CGContentInfo](cgcontentinfo.md)
### Functions
- [func CGGradientCreateWithContentHeadroom(Float, CGColorSpace, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>?, Int) -> CGGradient?](cggradientcreatewithcontentheadroom(_:_:_:_:_:).md)
- [func CGGradientGetContentHeadroom(CGGradient) -> Float](cggradientgetcontentheadroom(_:).md)
- [func CGPDFWrappedObjectCreateWithArray(CGPDFArrayRef) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewitharray(_:).md)
- [func CGPDFWrappedObjectCreateWithBoolean(CGPDFBoolean) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithboolean(_:).md)
- [func CGPDFWrappedObjectCreateWithDictionary(CGPDFDictionaryRef) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithdictionary(_:).md)
- [func CGPDFWrappedObjectCreateWithInteger(CGPDFInteger) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithinteger(_:).md)
- [func CGPDFWrappedObjectCreateWithName(UnsafePointer<CChar>) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithname(_:).md)
- [func CGPDFWrappedObjectCreateWithReal(CGPDFReal) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithreal(_:).md)
- [func CGPDFWrappedObjectCreateWithStream(CGPDFStreamRef) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithstream(_:).md)
- [func CGPDFWrappedObjectCreateWithString(CGPDFStringRef) -> CGPDFWrappedObject](cgpdfwrappedobjectcreatewithstring(_:).md)
- [func CGShadingCreateAxialWithContentHeadroom(Float, CGColorSpace, CGPoint, CGPoint, CGFunction, Bool, Bool) -> CGShading?](cgshadingcreateaxialwithcontentheadroom(_:_:_:_:_:_:_:).md)
- [func CGShadingCreateRadialWithContentHeadroom(Float, CGColorSpace, CGPoint, CGFloat, CGPoint, CGFloat, CGFunction, Bool, Bool) -> CGShading?](cgshadingcreateradialwithcontentheadroom(_:_:_:_:_:_:_:_:_:).md)
- [func CGShadingGetContentHeadroom(CGShading) -> Float](cgshadinggetcontentheadroom(_:).md)
### Enumerations
- [enum CGBitmapLayout](cgbitmaplayout.md)
- [enum CGComponent](cgcomponent.md)
- [enum CGContentToneMappingInfo](cgcontenttonemappinginfo-swift.enum.md)
- [enum CGImageComponentInfo](cgimagecomponentinfo.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreGraphics)*
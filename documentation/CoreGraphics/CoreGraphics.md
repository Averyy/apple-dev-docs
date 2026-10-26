# Core Graphics

**Framework**: Core Graphics  
**Kind**: module  
**Role**: Framework

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
- [struct CGFloat](../CoreFoundation/cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](../CoreFoundation/cgpoint.md)
- [struct CGSize](../CoreFoundation/cgsize.md)
  A structure that contains width and height values.
- [struct CGRect](../CoreFoundation/cgrect.md)
- [struct CGVector](../CoreFoundation/cgvector.md)
  A structure that contains a two-dimensional vector.
- [struct CGAffineTransform](../CoreFoundation/cgaffinetransform.md)
### 2D Drawing
- [class CGContext](./cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](./cgimage.md)
  A bitmap image or image mask.
- [class CGPath](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGMutablePath](./cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
### Colors and Fonts
- [class CGColor](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [class CGColorConversionInfo](./cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [class CGColorSpace](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [class CGFont](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
### Working with PDF Documents
- [class CGPDFDocument](./cgpdfdocument.md)
  A document that contains PDF (Portable Document Format) drawing information.
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
- [class CGPattern](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
### Services
- [Quartz Display Services](./quartz-display-services.md)
  Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- [Quartz Event Services](./quartz-event-services.md)
  Provides features for managing *event taps*—filters for observing and altering the stream of low-level user input events in macOS.
- [Quartz Window Services](./quartz-window-services.md)
  Provides information about the windows managed by the macOS window server.
### Reference
- [Core Graphics Structures](./core-graphics-structures.md)
- [Core Graphics Enumerations](./core-graphics-enumerations.md)
- [Core Graphics Constants](./core-graphics-constants.md)
- [Core Graphics Functions](./core-graphics-functions.md)
- [Core Graphics Data Types](./core-graphics-data-types.md)
- [CGAffineTransform](./cgaffinetransform.md)
  An affine transformation matrix for use in drawing 2D graphics.
- [CGGeometry](./cggeometry.md)
  Various structures and associated functions for 2D geometric primitives.
- [Core Graphics Macros](./core-graphics-macros.md)
### Classes
- [class CGPDFMarkedContentItem](./cgpdfmarkedcontentitem.md)
- [class CGPDFStructureElement](./cgpdfstructureelement.md)
- [class CGRenderingBufferProvider](./cgrenderingbufferprovider.md)
### Structures
- [struct CGBitmapParameters](./cgbitmapparameters-4v8wo.md)
- [struct CGColorModel](./cgcolormodel.md)
- [struct CGContentInfo](./cgcontentinfo.md)
- [CGBitmapParameters](./cgbitmapparameters-1cm7j.md)
- [CGContentToneMappingInfo](./cgcontenttonemappinginfo-c.struct.md)
### Enumerations
- [enum CGBitmapLayout](./cgbitmaplayout.md)
- [enum CGComponent](./cgcomponent.md)
- [enum CGContentToneMappingInfo](./cgcontenttonemappinginfo-swift.enum.md)
- [enum CGImageComponentInfo](./cgimagecomponentinfo.md)
### Opaque Types
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.
- [CGPDFObject](./cgpdfobject.md)
  An object representing content within a PDF document.
- [CGPDFOperatorTable](./cgpdfoperatortable.md)
  A set of callback functions for operators used when scanning content in a PDF document.
- [CGPDFPageRef](./cgpdfpage.md)
  A type that represents a page in a PDF document.
- [CGPDFScanner](./cgpdfscanner.md)
  A parser object for handling content and operators in a PDF content stream.
- [CGPDFStream](./cgpdfstream.md)
  A stream or sequence of data bytes in a PDF document.
- [CGPDFString](./cgpdfstring.md)
  A text string in a PDF document.
- [CGPSConverterRef](./cgpsconverter.md)
  An opaque data type used to convert PostScript data to PDF data.
### Variables
- [kCGAdaptiveMaximumBitDepth](./kcgadaptivemaximumbitdepth.md)
- [kCGContentAverageLightLevel](./kcgcontentaveragelightlevel.md)
- [kCGContentAverageLightLevelNits](./kcgcontentaveragelightlevelnits.md)
- [kCGDisplayStreamColorSpace](./kcgdisplaystreamcolorspace.md)
- [kCGDisplayStreamDestinationRect](./kcgdisplaystreamdestinationrect.md)
- [kCGDisplayStreamMinimumFrameTime](./kcgdisplaystreamminimumframetime.md)
- [kCGDisplayStreamPreserveAspectRatio](./kcgdisplaystreampreserveaspectratio.md)
- [kCGDisplayStreamQueueDepth](./kcgdisplaystreamqueuedepth.md)
- [kCGDisplayStreamShowCursor](./kcgdisplaystreamshowcursor.md)
- [kCGDisplayStreamSourceRect](./kcgdisplaystreamsourcerect.md)
- [kCGDisplayStreamYCbCrMatrix](./kcgdisplaystreamycbcrmatrix.md)
- [kCGDynamicRangeConstrained](./kcgdynamicrangeconstrained.md)
- [kCGDynamicRangeHigh](./kcgdynamicrangehigh.md)
- [kCGDynamicRangeStandard](./kcgdynamicrangestandard.md)
- [kCGPreferredDynamicRange](./kcgpreferreddynamicrange.md)
### Functions
- [CGBitmapContextCreateAdaptive](./cgbitmapcontextcreateadaptive.md)
- [CGBitmapInfoMake](./cgbitmapinfomake.md)
- [CGColorGetContentHeadroom](./cgcolor/contentheadroom.md)
- [CGColorCreateWithContentHeadroom](./cgcolor/init%28headroom,colorspace,red,green,blue,alpha%29.md)
- [CGColorConversionInfoCreateForToneMapping](./cgcolorconversioninfo/init%28src,srcheadroom,dst,dstheadroom,tonemapping,options,_%29.md)
- [CGPDFContextAddStructureTreeRootChild](./cgcontext/addstructuretreerootchild%28_%29.md)
- [CGPDFContextBeginMarkedContentSequence](./cgcontext/beginmarkedcontentsequence%28_%29.md)
- [CGPDFContextBeginNonStructuralMarkedContentSequence](./cgcontext/beginnonstructuralmarkedcontentsequence%28_%29.md)
- [CGPDFContextBeginObjectReference](./cgcontext/beginobjectreference%28%29.md)
- [CGPDFContextEndMarkedContentSequence](./cgcontext/endmarkedcontentsequence%28%29.md)
- [CGPDFContextEndObjectReference](./cgcontext/endobjectreference%28%29.md)
- [CGBitmapContextCreate](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo%29-10b3i.md)
- [CGBitmapContextCreateWithData](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo,releasecallback,releaseinfo%29-4yzt5.md)
- [CGContextSynchronizeAttributes](./cgcontext/synchronizeattributes%28%29.md)
- [CGContextGetContentToneMappingInfo](./cgcontextgetcontenttonemappinginfo.md)
- [CGContextSetContentToneMappingInfo](./cgcontextsetcontenttonemappinginfo.md)
- [CGDisplayCreateImage](./cgdisplaycreateimage.md)
- [CGDisplayCreateImageForRect](./cgdisplaycreateimageforrect.md)
- [CGDisplayStreamCreate](./cgdisplaystreamcreate.md)
- [CGDisplayStreamCreateWithDispatchQueue](./cgdisplaystreamcreatewithdispatchqueue.md)
- [CGDisplayStreamGetRunLoopSource](./cgdisplaystreamgetrunloopsource.md)
- [CGDisplayStreamGetTypeID](./cgdisplaystreamgettypeid.md)
- [CGDisplayStreamStart](./cgdisplaystreamstart.md)
- [CGDisplayStreamStop](./cgdisplaystreamstop.md)
- [CGDisplayStreamUpdateCreateMergedUpdate](./cgdisplaystreamupdatecreatemergedupdate.md)
- [CGDisplayStreamUpdateGetDropCount](./cgdisplaystreamupdategetdropcount.md)
- [CGDisplayStreamUpdateGetMovedRectsDelta](./cgdisplaystreamupdategetmovedrectsdelta.md)
- [CGDisplayStreamUpdateGetRects](./cgdisplaystreamupdategetrects.md)
- [CGDisplayStreamUpdateGetTypeID](./cgdisplaystreamupdategettypeid.md)
- [CGEXRToneMappingGammaGetDefaultOptions](./cgexrtonemappinggammagetdefaultoptions.md)
- [CGGradientGetContentHeadroom](./cggradient/contentheadroom.md)
- [CGGradientCreateWithContentHeadroom](./cggradient/init%28headroom,colorspace,colorcomponents,locations,count%29.md)
- [CGPDFMarkedContentItemRelease](./cgpdfmarkedcontentitemrelease.md)
- [CGPDFMarkedContentItemRetain](./cgpdfmarkedcontentitemretain.md)
- [CGPDFStructureElementAddStructureElement](./cgpdfstructureelement/addchild%28_%29.md)
- [CGPDFStructureElementAddMarkedContentItem](./cgpdfstructureelement/addmarkedcontentitem%28_%29.md)
- [CGPDFStructureElementCreate](./cgpdfstructureelement/init%28tagtype%29.md)
- [CGPDFStructureElementRelease](./cgpdfstructureelementrelease.md)
- [CGPDFStructureElementRetain](./cgpdfstructureelementretain.md)
- [CGPDFStructureElementSetActualText](./cgpdfstructureelementsetactualtext.md)
- [CGPDFStructureElementSetAlternativeText](./cgpdfstructureelementsetalternativetext.md)
- [CGPDFStructureElementSetExpansionText](./cgpdfstructureelementsetexpansiontext.md)
- [CGPDFStructureElementSetLanguageIdentifier](./cgpdfstructureelementsetlanguageidentifier.md)
- [CGPDFStructureElementSetTitle](./cgpdfstructureelementsettitle.md)
- [CGRenderingBufferLockBytePtr](./cgrenderingbufferlockbyteptr.md)
- [CGRenderingBufferProviderCreate](./cgrenderingbufferprovidercreate.md)
- [CGRenderingBufferProviderCreateWithCFData](./cgrenderingbufferprovidercreatewithcfdata.md)
- [CGRenderingBufferProviderGetSize](./cgrenderingbufferprovidergetsize.md)
- [CGRenderingBufferProviderGetTypeID](./cgrenderingbufferprovidergettypeid.md)
- [CGRenderingBufferUnlockBytePtr](./cgrenderingbufferunlockbyteptr.md)
- [CGShadingGetContentHeadroom](./cgshading/contentheadroom.md)
- [CGShadingCreateAxialWithContentHeadroom](./cgshading/init%28axialheadroom,space,start,end,function,extendstart,extendend%29.md)
- [CGShadingCreateRadialWithContentHeadroom](./cgshading/init%28radialheadroom,space,start,startradius,end,endradius,function,extendstart,extendend%29.md)
- [CGWindowListCreateImage](./cgwindowlistcreateimage.md)
- [CGWindowListCreateImageFromArray](./cgwindowlistcreateimagefromarray.md)
### Macros
- [CG_ENUM_SOFT_DEPRECATED_WITH_REPLACEMENT](./cg_enum_soft_deprecated_with_replacement.md)
- [CG_SOFT_DEPRECATED_WITH_REPLACEMENT](./cg_soft_deprecated_with_replacement.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreGraphics)*
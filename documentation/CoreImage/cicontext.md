# CIContext

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class CIContext
```

```objc
@interface CIContext : NSObject
```

## Mentions

- [Processing an Image Using Built-in Filters](./processing-an-image-using-built-in-filters.md)

#### Overview

You use a `CIContext` instance to render a [`CIImage`](./ciimage.md) instance which represents a graph of image processing operations which are built using other Core Image classes, such as [`CIFilter`](./cifilter-swift.class.md), [`CIKernel`](./cikernel.md), [`CIColor`](./cicolor.md) and [`CIImage`](./ciimage.md). You can also use a `CIContext` with the [`CIDetector`](./cidetector.md) class to analyze images — for example, to detect faces or barcodes.

Contexts support automatic color management by performing all processing operations in a working color space. This means that unless told otherwise:

- All input images are color matched from the input’s color space to the working space.
- All renders are color matched from the working space to the destination space. (For more information on `CGColorSpace` see [`CGColorSpace`](../CoreGraphics/cgcolorspace.md))

`CIContext` and [`CIImage`](./ciimage.md) instances are immutable, so multiple threads can use the same [`CIContext`](./cicontext.md) instance to render [`CIImage`](./ciimage.md) instances. However, [`CIFilter`](./cifilter-swift.class.md) instances are mutable and thus cannot be shared safely among threads. Each thread must take case not to access or modify a [`CIFilter`](./cifilter-swift.class.md) instance while it is being used by another thread.

The `CIContext` manages various internal state such as `MTLCommandQueue` and caches for compiled kernels and intermediate buffers.  For this reason it is not recommended to create many `CIContext` instances.  As a rule, it recommended that you create one `CIContext` instance for each view that renders [`CIImage`](./ciimage.md) or each background task.

## Topics

### Creating a Context Without Specifying a Destination
- [init()](./cicontext/init%28%29.md)
  Initializes a context without a specific rendering destination, using default options.
- [+ context](./cicontext/context.md)
  Creates a context without a specific rendering destination, using default options.
- [+ contextWithOptions:](./cicontext/contextwithoptions_.md)
  Initializes a context without a specific rendering destination, using the specified options.
### Creating a Context for CPU-Based Rendering
- [init(cgContext: CGContext, options: [CIContextOption : Any]?)](./cicontext/init%28cgcontext,options%29-6p78w.md)
  Creates a Core Image context from a Quartz context, using the specified options.
### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](./cicontext/init%28mtldevice%29-swey.md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](./cicontext/init%28mtldevice,options%29-26usb.md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue)](./cicontext/init%28mtlcommandqueue%29-7dtqk.md)
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](./cicontext/init%28mtlcommandqueue,options%29-6i3me.md)
### Rendering Images
- [func createCGImage(CIImage, from: CGRect) -> CGImage?](./cicontext/createcgimage%28_,from%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?](./cicontext/createcgimage%28_,from,format,colorspace%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](./cicontext/createcgimage%28_,from,format,colorspace,deferred%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](./cicontext/render%28_,tobitmap,rowbytes,bounds,format,colorspace%29.md)
  Renders to the given bitmap.
- [func render(CIImage, to: CVPixelBuffer)](./cicontext/render%28_,to%29.md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](./cicontext/render%28_,to,bounds,colorspace%29-2k8l2.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](./cicontext/render%28_,to,bounds,colorspace%29-54b9l.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](./cicontext/render%28_,to,commandbuffer,bounds,colorspace%29.md)
  Renders a region of an image to a Metal texture.
### Drawing Images
- [func draw(CIImage, in: CGRect, from: CGRect)](./cicontext/draw%28_,in,from%29.md)
  Renders a region of an image to a rectangle in the context destination.
### Determining the Allowed Extents for Images Used by a Context
- [func inputImageMaximumSize() -> CGSize](./cicontext/inputimagemaximumsize%28%29.md)
  Returns the maximum size allowed for any image rendered into the context.
- [func outputImageMaximumSize() -> CGSize](./cicontext/outputimagemaximumsize%28%29.md)
  Returns the maximum size allowed for any image created by the context.
### Managing Resources
- [func clearCaches()](./cicontext/clearcaches%28%29.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](./cicontext/reclaimresources%28%29.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](./cicontext/offlinegpucount%28%29.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](./cicontext/workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](./cicontext/workingformat.md)
  The working pixel format of the Core Image context.
### Rendering Images for Data or File Export
- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./cicontext/tiffrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./cicontext/jpegrepresentation%28of,colorspace,options%29.md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./cicontext/pngrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./cicontext/heifrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in HEIF format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws -> Data](./cicontext/heif10representation%28of,colorspace,options%29.md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) throws -> Data](./cicontext/openexrrepresentation%28of,options%29.md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./cicontext/writetiffrepresentation%28of,to,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./cicontext/writejpegrepresentation%28of,to,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./cicontext/writepngrepresentation%28of,to,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./cicontext/writeheifrepresentation%28of,to,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./cicontext/writeheif10representation%28of,to,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any]) throws](./cicontext/writeopenexrrepresentation%28of,to,options%29.md)
  Renders the image and exports the resulting image data as a file in open EXR format.
- [struct CIImageRepresentationOption](./ciimagerepresentationoption.md)
### Creating Depth Blur Filters
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, glassesMatte: CIImage?, gainMap: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](./cicontext/depthblureffectfilter%28for,disparityimage,portraiteffectsmatte,hairsemanticsegmentation,glassesmatte,gainmap,orientation,options%29.md)
  Create a [`CIFilter`](./cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](./cicontext/depthblureffectfilter%28for,disparityimage,portraiteffectsmatte,hairsemanticsegmentation,orientation,options%29.md)
  Create a [`CIFilter`](./cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](./cicontext/depthblureffectfilter%28for,disparityimage,portraiteffectsmatte,orientation,options%29.md)
  Create a [`CIFilter`](./cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(forImageData: Data, options: [AnyHashable : Any]?) -> CIFilter?](./cicontext/depthblureffectfilter%28forimagedata,options%29.md)
  Create a [`CIFilter`](./cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.
- [func depthBlurEffectFilter(forImageURL: URL, options: [AnyHashable : Any]?) -> CIFilter?](./cicontext/depthblureffectfilter%28forimageurl,options%29.md)
  Create a [`CIFilter`](./cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.
### Constants
- [struct CIContextOption](./cicontextoption.md)
  An enum string type that your code can use to select different options when creating a Core Image context.
### Customizing Render Destination
- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws](./cicontext/preparerender%28_,from,to,at%29.md)
  An optional call to warm up a [`CIContext`](./cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) throws -> CIRenderTask](./cicontext/starttask%28toclear%29.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](./cirenderdestination/alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](./cicontext/starttask%28torender,from,to,at%29.md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) throws -> CIRenderTask](./cicontext/starttask%28torender,to%29.md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.
### Deprecated
- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](./cicontext/init%28cglcontext,pixelformat,colorspace,options%29-6rp6d.md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](./cicontext/init%28eaglcontext%29-8ajef.md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](./cicontext/init%28eaglcontext,options%29-6uyqj.md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAtIndex: UInt32)](./cicontext/init%28forofflinegpuatindex%29.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](./cicontext/init%28forofflinegpuatindex,colorspace,options,sharedcontext%29.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](./cicontext/createcglayer%28with,info%29.md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](./cicontext/draw%28_,at,from%29.md)
  Renders a region of an image to a point in the context destination.
- [+ contextWithCGLContext:pixelFormat:options:](./cicontext/contextwithcglcontext_pixelformat_options_.md)
  Creates a Core Image context from a CGL context, using the specified options and pixel format object.
### Initializers
- [init(CGContext: CGContext, options: [CIContextOption : Any]?)](./cicontext/init%28cgcontext,options%29-1yzwi.md)
- [init(CGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](./cicontext/init%28cglcontext,pixelformat,colorspace,options%29-3t25h.md)
- [init(EAGLContext: EAGLContext)](./cicontext/init%28eaglcontext%29-293h1.md)
- [init(EAGLContext: EAGLContext, options: [CIContextOption : Any]?)](./cicontext/init%28eaglcontext,options%29-2853a.md)
- [init(MTLCommandQueue: any MTLCommandQueue)](./cicontext/init%28mtlcommandqueue%29-2pgxu.md)
- [init(MTLCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](./cicontext/init%28mtlcommandqueue,options%29-q929.md)
- [init(MTLDevice: any MTLDevice)](./cicontext/init%28mtldevice%29-8ksdj.md)
- [init(MTLDevice: any MTLDevice, options: [CIContextOption : Any]?)](./cicontext/init%28mtldevice,options%29-15xqo.md)
- [init?(forOfflineGPUAt: UInt32)](./cicontext/init%28forofflinegpuat%29.md)
- [init?(forOfflineGPUAt: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](./cicontext/init%28forofflinegpuat,colorspace,options,sharedcontext%29.md)
- [init(options: [CIContextOption : Any]?)](./cicontext/init%28options%29.md)
  Initializes a context without a specific rendering destination, using the specified options.
### Instance Methods
- [func calculateHDRStats(for: CGImage) -> CGImage](./cicontext/calculatehdrstats%28for%29-3ia7r.md)
  Given a Core Graphics image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Graphics image that has the calculated values.
- [func calculateHDRStats(for: IOSurfaceRef)](./cicontext/calculatehdrstats%28for%29-6lwmz.md)
  Given an IOSurface, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the surface’s attachments to store the values.
- [func calculateHDRStats(for: CVPixelBuffer)](./cicontext/calculatehdrstats%28for%29-7bcki.md)
  Given a CVPixelBuffer, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the buffer’s attachments to store the values.
- [func calculateHDRStats(for: CIImage) -> CIImage?](./cicontext/calculatehdrstats%28for%29-l1rj.md)
  Given a Core Image image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Image image that has the calculated values.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool, calculateHDRStats: Bool) -> CGImage?](./cicontext/createcgimage%28_,from,format,colorspace,deferred,calculatehdrstats%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for calculating HDR statistics.
- [func estimateRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](./cicontext/estimaterender%28_,from,to,at%29.md)
  Returns a task with estimated resource statistics for a render, without executing the render.
### Default Implementations
- [CIContext Implementations](./cicontext/cicontext-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [Processing an Image Using Built-in Filters](./processing-an-image-using-built-in-filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIImage](./ciimage.md)
  A representation of an image to be processed or produced by Core Image filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext)*
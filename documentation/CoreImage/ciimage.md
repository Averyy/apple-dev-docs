# CIImage

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A representation of an image to be processed or produced by Core Image filters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class CIImage
```

```objc
@interface CIImage : NSObject
```

## Mentions

- [Processing an Image Using Built-in Filters](./processing-an-image-using-built-in-filters.md)
- [Selectively Focusing on an Image](./selectively-focusing-on-an-image.md)
- [Customizing Image Transitions](./customizing-image-transitions.md)

#### Overview

You use `CIImage` objects in conjunction with other Core Image classes—such as [`CIFilter`](./cifilter-swift.class.md), [`CIContext`](./cicontext.md), [`CIVector`](./civector.md), and [`CIColor`](./cicolor.md)—to take advantage of the built-in Core Image filters when processing images. You can create `CIImage` objects with data supplied from a variety of sources, including Quartz 2D images, Core Video image buffers ([`CVImageBuffer`](../CoreVideo/cvimagebuffer.md)), URL-based objects, and `NSData` objects.

Although a `CIImage` object has image data associated with it, it is not an image. You can think of a `CIImage` object as an image “recipe.” A `CIImage` object has all the information necessary to produce an image, but Core Image doesn’t actually render an image until it is told to do so. This lazy evaluation allows Core Image to operate as efficiently as possible. To show a `CIImage` object as an on-screen image, you can display it as a [`UIImage`](../UIKit/uiimage.md) in [`UIImageView`](../UIKit/uiimageview.md):

**Swift**:

```swift
guard let imageURL = Bundle.main.url(forResource: "YourJPEGName", withExtension: "JPG") else {
    print("Could not find image")
    return
}
guard let let ciImage = CIImage(contentsOf: imageURL) else {
    print("Could not create CIImage")
    return
}
let uiImage = UIImage(ciImage: ciImage)
let imageView = UIImageView(image: uiImage)    
self.view.addSubview(imageView)
```

**Objective-C**:

```objc
NSURL* imageURL = [[NSBundle mainBundle] URLForResource:@"YourJPEGName" withExtension:@"JPG"];
CIImage* ciImage = [CIImage imageWithContentsOfURL:imageURL];
UIImage* uiImage = [UIImage imageWithCIImage:ciImage];
UIImageView* imageView = [[UIImageView alloc] initWithImage:uiImage];
[self.view addSubview:imageView];
```

`CIContext`  and `CIImage` objects are immutable, which means each can be shared safely among threads. Multiple threads can use the same GPU or CPU `CIContext` object to render `CIImage` objects.  However, this is not the case for `CIFilter` objects, which are mutable. A `CIFilter` object cannot be shared safely among threads.  If you app is multithreaded, each thread must create its own `CIFilter` objects. Otherwise, your app could behave unexpectedly.

Core Image also provides auto-adjustment methods. These methods analyze an image for common deficiencies and return a set of filters to correct those deficiencies. The filters are preset with values for improving image quality by altering values for skin tones, saturation, contrast, and shadows and for removing red-eye or other artifacts caused by flash. (See Getting Autoadjustment Filters.)

For a discussion of all the methods you can use to create `CIImage` objects on iOS and macOS, see [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Topics

### Creating an Image
- [class func empty() -> CIImage](./ciimage/empty%28%29.md)
  Creates and returns an empty image object.
- [init?(image: UIImage)](./ciimage/init%28image%29.md)
  Initializes an image object with the specified UIKit image object.
- [init?(image: UIImage, options: [CIImageOption : Any]?)](./ciimage/init%28image,options%29.md)
  Initializes an image object with the specified UIKit image object, using the specified options.
- [init?(contentsOf: URL)](./ciimage/init%28contentsof%29.md)
  Initializes an image object by reading an image from a URL.
- [init?(contentsOf: URL, options: [CIImageOption : Any]?)](./ciimage/init%28contentsof,options%29.md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [init(cgImage: CGImage)](./ciimage/init%28cgimage%29-2kvvb.md)
  Initializes an image object with a Quartz 2D image.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](./ciimage/init%28cgimage,options%29-8663h.md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](./ciimage/init%28cgimagesource,index,options%29-e2bz.md)
- [init?(data: Data)](./ciimage/init%28data%29.md)
  Initializes an image object with the supplied image data.
- [init?(data: Data, options: [CIImageOption : Any]?)](./ciimage/init%28data,options%29.md)
  Initializes an image object with the supplied image data, using the specified options.
- [init(bitmapData: Data, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](./ciimage/init%28bitmapdata,bytesperrow,size,format,colorspace%29.md)
  Initializes an image object with bitmap data.
- [init?(bitmapImageRep: NSBitmapImageRep)](./ciimage/init%28bitmapimagerep%29.md)
  Initializes an image object with the specified bitmap image representation.
- [init(imageProvider: Any, size: Int, Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]?)](./ciimage/init%28imageprovider,size,_,format,colorspace,options%29.md)
  Initializes an image object based on pixels from an image provider object.
- [init?(depthData: AVDepthData)](./ciimage/init%28depthdata%29.md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](./ciimage/init%28depthdata,options%29.md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte)](./ciimage/init%28portaiteffectsmatte%29.md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte, options: [CIImageOption : Any]?)](./ciimage/init%28portaiteffectsmatte,options%29.md)
- [init?(semanticSegmentationMatte: AVSemanticSegmentationMatte)](./ciimage/init%28semanticsegmentationmatte%29.md)
- [init?(semanticSegmentationMatte: AVSemanticSegmentationMatte, options: [CIImageOption : Any]?)](./ciimage/init%28semanticsegmentationmatte,options%29.md)
- [init(cvImageBuffer: CVImageBuffer)](./ciimage/init%28cvimagebuffer%29-7wmzq.md)
  Initializes an image object from the contents of a Core Video image buffer.
- [init(cvImageBuffer: CVImageBuffer, options: [CIImageOption : Any]?)](./ciimage/init%28cvimagebuffer,options%29-8upim.md)
  Initializes an image object from the contents of a Core Video image buffer, using the specified options.
- [init(cvPixelBuffer: CVPixelBuffer)](./ciimage/init%28cvpixelbuffer%29-3wng7.md)
  Initializes an image object from the contents of a Core Video pixel buffer.
- [init(cvPixelBuffer: CVPixelBuffer, options: [CIImageOption : Any]?)](./ciimage/init%28cvpixelbuffer,options%29-9x2pz.md)
  Initializes an image object from the contents of a Core Video pixel buffer using the specified options.
- [init?(mtlTexture: any MTLTexture, options: [CIImageOption : Any]?)](./ciimage/init%28mtltexture,options%29-67uvj.md)
  Initializes an image object with data supplied by a Metal texture.
- [init(ioSurface: IOSurfaceRef)](./ciimage/init%28iosurface%29-5e9yc.md)
  Initializes an image with the contents of an IOSurface.
- [init(ioSurface: IOSurfaceRef, options: [CIImageOption : Any]?)](./ciimage/init%28iosurface,options%29-48cta.md)
  Initializes, using the specified options, an image with the contents of an IOSurface.
### Creating an Image by Modifying an Existing Image
- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](./ciimage/applyingfilter%28_,parameters%29.md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](./ciimage/applyingfilter%28_%29.md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](./ciimage/transformed%28by%29.md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](./ciimage/transformed%28by,highqualitydownsample%29.md)
- [func cropped(to: CGRect) -> CIImage](./ciimage/cropped%28to%29.md)
  Returns a new image with a cropped portion of the original image.
- [func oriented(forExifOrientation: Int32) -> CIImage](./ciimage/oriented%28forexiforientation%29.md)
  Returns a new image created by transforming the original image to the specified EXIF orientation.
- [func clampedToExtent() -> CIImage](./ciimage/clampedtoextent%28%29.md)
  Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [func clamped(to: CGRect) -> CIImage](./ciimage/clamped%28to%29.md)
  Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [func composited(over: CIImage) -> CIImage](./ciimage/composited%28over%29.md)
  Returns a new image created by compositing the original image over the specified destination image.
- [func convertingWorkingSpaceToLab() -> CIImage](./ciimage/convertingworkingspacetolab%28%29.md)
- [func convertingLabToWorkingSpace() -> CIImage](./ciimage/convertinglabtoworkingspace%28%29.md)
- [func matchedToWorkingSpace(from: CGColorSpace) -> CIImage?](./ciimage/matchedtoworkingspace%28from%29.md)
  Returns a new image created by color matching from the specified color space to the context’s working color space.
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](./ciimage/matchedfromworkingspace%28to%29.md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](./ciimage/premultiplyingalpha%28%29.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](./ciimage/unpremultiplyingalpha%28%29.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](./ciimage/settingalphaone%28in%29.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
- [func applyingGaussianBlur(sigma: Double) -> CIImage](./ciimage/applyinggaussianblur%28sigma%29.md)
  Create an image by applying a gaussian blur to the receiver.
- [func settingProperties([AnyHashable : Any]) -> CIImage](./ciimage/settingproperties%28_%29.md)
  Return a new image by changing the receiver’s metadata properties.
- [func insertingIntermediate() -> CIImage](./ciimage/insertingintermediate%28%29.md)
  Create an image that inserts a intermediate that is cacheable
- [func insertingIntermediate(cache: Bool) -> CIImage](./ciimage/insertingintermediate%28cache%29.md)
  Create an image that inserts a intermediate that is cacheable.
### Creating Solid Colors
- [init(color: CIColor)](./ciimage/init%28color%29.md)
  Initializes an image of infinite extent whose entire content is the specified color.
- [class var black: CIImage](./ciimage/black.md)
- [class var blue: CIImage](./ciimage/blue.md)
- [class var clear: CIImage](./ciimage/clear.md)
- [class var cyan: CIImage](./ciimage/cyan.md)
- [class var gray: CIImage](./ciimage/gray.md)
- [class var green: CIImage](./ciimage/green.md)
- [class var magenta: CIImage](./ciimage/magenta.md)
- [class var red: CIImage](./ciimage/red.md)
- [class var white: CIImage](./ciimage/white.md)
- [class var yellow: CIImage](./ciimage/yellow.md)
### Getting Image Information
- [var definition: CIFilterShape](./ciimage/definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](./ciimage/extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](./ciimage/properties.md)
  Returns the metadata properties dictionary of the image.
- [var url: URL?](./ciimage/url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](./ciimage/colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](./ciimage/orientationtransform%28forexiforientation%29.md)
  Returns the transformation needed to reorient the image to the specified orientation.
### Drawing Images
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./ciimage/draw%28at,from,operation,fraction%29.md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./ciimage/draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system
### Getting Autoadjustment Filters
- [func autoAdjustmentFilters() -> [CIFilter]](./ciimage/autoadjustmentfilters%28%29.md)
  Returns all possible automatically selected and configured filters for adjusting the image.
- [func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]?) -> [CIFilter]](./ciimage/autoadjustmentfilters%28options%29.md)
  Returns a subset of automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](./autoadjustment-keys.md)
  Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](./ciimage/autoadjustmentfilters%28options%29.md) method.
### Working with Filter Regions of Interest
- [func regionOfInterest(for: CIImage, in: CGRect) -> CGRect](./ciimage/regionofinterest%28for,in%29.md)
  Returns the region of interest for the filter chain that generates the image.
### Working with Orientation
- [func oriented(CGImagePropertyOrientation) -> CIImage](./ciimage/oriented%28_%29.md)
  Transforms the original image by a given orientation.
- [func orientationTransform(for: CGImagePropertyOrientation) -> CGAffineTransform](./ciimage/orientationtransform%28for%29.md)
  The affine transform for changing the image to the given orientation.
### Sampling the Image
- [func samplingNearest() -> CIImage](./ciimage/samplingnearest%28%29.md)
  Create an image by changing the receiver’s sample mode to nearest neighbor.
- [func samplingLinear() -> CIImage](./ciimage/samplinglinear%28%29.md)
  Create an image by changing the receiver’s sample mode to bilinear interpolation.
### Accessing Original Image Content
- [var cgImage: CGImage?](./ciimage/cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](./ciimage/pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](./ciimage/depthdata.md)
  Depth data associated with the image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](./ciimage/portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](./ciimage/semanticsegmentationmatte.md)
### Image Dictionary Keys
- [struct CIImageOption](./ciimageoption.md)
### AutoAdjustment Keys
- [struct CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption.md)
### Deprecated
- [init(cgLayer: CGLayer)](./ciimage/init%28cglayer%29-2lgo6.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](./ciimage/init%28cglayer,options%29-3p3l3.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](./ciimage/init%28texture,size,flipped,colorspace%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](./ciimage/init%28texture,size,flipped,options%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](./ciimage/init%28iosurface,plane,format,options%29-93isn.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](./ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](./ciimageoption/textureformat.md)
  The key for an OpenGL texture format.
### Instance Properties
- [var contentHeadroom: Float](./ciimage/contentheadroom.md)
  Returns the content headroom of the image.
- [var isOpaque: Bool](./ciimage/isopaque.md)
  Returns YES if the image is known to have and alpha value of `1.0` over the entire image extent.
- [var metalTexture: (any MTLTexture)?](./ciimage/metaltexture.md)
- [var contentAverageLightLevel: Float](./ciimage/contentaveragelightlevel.md)
  Returns the content average light level of the image.
### Instance Methods
- [func applyingGainMap(CIImage) -> CIImage](./ciimage/applyinggainmap%28_%29.md)
  Create an image that applies a gain map Core Image image to the received Core Image image.
- [func applyingGainMap(CIImage, headroom: Float) -> CIImage](./ciimage/applyinggainmap%28_,headroom%29.md)
  Create an image that applies a gain map Core Image image with a specified headroom to the received Core Image image.
- [func insertingTiledIntermediate() -> CIImage](./ciimage/insertingtiledintermediate%28%29.md)
  Create an image that inserts a intermediate that is cached in tiles
- [func settingContentAverageLightLevel(Float) -> CIImage](./ciimage/settingcontentaveragelightlevel%28_%29.md)
  Create an image by changing the receiver’s contentAverageLightLevel property.
- [func settingContentHeadroom(Float) -> CIImage](./ciimage/settingcontentheadroom%28_%29.md)
  Create an image by changing the receiver’s contentHeadroom property.
### Initializers
- [init(CGImage: CGImage)](./ciimage/init%28cgimage%29-5vlch.md)
- [init(CGImage: CGImage)](./ciimage/init%28cgimage%29-8cm8a.md)
- [init(CGImage: CGImage, options: [CIImageOption : Any]?)](./ciimage/init%28cgimage,options%29-1ksqh.md)
- [init(CGImage: CGImage, options: [CIImageOption : Any]?)](./ciimage/init%28cgimage,options%29-28wtj.md)
- [init(CGImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](./ciimage/init%28cgimagesource,index,options%29-2dium.md)
- [init(CGImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](./ciimage/init%28cgimagesource,index,options%29-4b3fz.md)
- [init(CGLayer: CGLayer)](./ciimage/init%28cglayer%29-3wseb.md)
- [init(CGLayer: CGLayer)](./ciimage/init%28cglayer%29-8o853.md)
- [init(CGLayer: CGLayer, options: [CIImageOption : Any]?)](./ciimage/init%28cglayer,options%29-34jjk.md)
- [init(CGLayer: CGLayer, options: [CIImageOption : Any]?)](./ciimage/init%28cglayer,options%29-8su8t.md)
- [init(CVImageBuffer: CVImageBuffer)](./ciimage/init%28cvimagebuffer%29-6k44w.md)
- [init(CVImageBuffer: CVImageBuffer)](./ciimage/init%28cvimagebuffer%29-9fq4l.md)
- [init(CVImageBuffer: CVImageBuffer, options: [CIImageOption : Any]?)](./ciimage/init%28cvimagebuffer,options%29-79c2d.md)
- [init(CVImageBuffer: CVImageBuffer, options: [CIImageOption : Any]?)](./ciimage/init%28cvimagebuffer,options%29-7g0yo.md)
- [init(CVPixelBuffer: CVPixelBuffer)](./ciimage/init%28cvpixelbuffer%29-1z0mw.md)
- [init(CVPixelBuffer: CVPixelBuffer)](./ciimage/init%28cvpixelbuffer%29-5p2mz.md)
- [init(CVPixelBuffer: CVPixelBuffer, options: [CIImageOption : Any]?)](./ciimage/init%28cvpixelbuffer,options%29-6rkzb.md)
- [init(CVPixelBuffer: CVPixelBuffer, options: [CIImageOption : Any]?)](./ciimage/init%28cvpixelbuffer,options%29-8i44g.md)
- [init(IOSurface: IOSurfaceRef)](./ciimage/init%28iosurface%29-72me3.md)
- [init(IOSurface: IOSurfaceRef)](./ciimage/init%28iosurface%29-7dwj8.md)
- [init(IOSurface: IOSurfaceRef, options: [CIImageOption : Any]?)](./ciimage/init%28iosurface,options%29-4dwl5.md)
- [init(IOSurface: IOSurfaceRef, options: [CIImageOption : Any]?)](./ciimage/init%28iosurface,options%29-7qdsg.md)
- [init(IOSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](./ciimage/init%28iosurface,plane,format,options%29-7k35r.md)
- [init?(MTLTexture: any MTLTexture, options: [CIImageOption : Any]?)](./ciimage/init%28mtltexture,options%29-510vm.md)
- [init?(MTLTexture: any MTLTexture, options: [CIImageOption : Any]?)](./ciimage/init%28mtltexture,options%29-5ou1j.md)
- [init?(coder: NSCoder)](./ciimage/init%28coder%29.md)
- [init?(contentsOfURL: URL)](./ciimage/init%28contentsofurl%29-1e9r3.md)
- [init?(contentsOfURL: URL)](./ciimage/init%28contentsofurl%29-9vlbb.md)
- [init?(contentsOfURL: URL, options: [CIImageOption : Any]?)](./ciimage/init%28contentsofurl,options%29-7g3lx.md)
- [init?(contentsOfURL: URL, options: [CIImageOption : Any]?)](./ciimage/init%28contentsofurl,options%29-93guu.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [AttachableAsImage](../Testing/attachableasimage.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [Processing an Image Using Built-in Filters](./processing-an-image-using-built-in-filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIContext](./cicontext.md)
  The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage)*
# NSBitmapImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that renders an image from bitmap data.

**Availability**:
- macOS

## Declaration

```swift
class NSBitmapImageRep
```

```objc
@interface NSBitmapImageRep : NSImageRep
```

## Overview

Supported bitmap data formats include GIF, JPEG, TIFF, PNG, and various permutations of raw bitmap data.

### Alpha Premultiplication and Bitmap Formats

When creating a bitmap using a premultiplied format, if a coverage (alpha) plane exists, the bitmap’s color components are premultiplied with it. In this case, if you modify the contents of the bitmap, you are therefore responsible for premultiplying the data. Note that premultiplying generally has negligible effect on output quality. For floating-point image data, premultiplying color components is a lossless operation, but for fixed-point image data, premultiplication can introduce small rounding errors. In either case, more rounding errors may appear when compositing many premultiplied images; however, such errors are generally not readily visible.

For this reason, you should not use an [`NSBitmapImageRep`](./nsbitmapimagerep.md) object if you want to manipulate image data. To work with data that is not premultiplied, use the Core Graphics framework instead. (Specifically, create images using the [`init(width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:)`](../CoreGraphics/cgimage/init%28width,height,bitspercomponent,bitsperpixel,bytesperrow,space,bitmapinfo,provider,decode,shouldinterpolate,intent%29.md) function and [`CGImageAlphaInfo.last`](../CoreGraphics/cgimagealphainfo/last.md) parameter.) Alternatively, include the [`NSAlphaNonpremultipliedBitmapFormat`](./nsalphanonpremultipliedbitmapformat.md) flag when creating the bitmap.

> **Note**:  Use the `bitmapFormat` parameter to the [`init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:)`](./nsbitmapimagerep/init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bitmapformat,bytesperrow,bitsperpixel%29.md) method to specify the format for creating a bitmap. When creating or retrieving a bitmap with other methods, the bitmap format depends on the original source of the image data. Check the [`bitmapFormat`](./nsbitmapimagerep/bitmapformat.md) property before working with image data.

## Topics

### Creating Bitmap Representations of Images
- [class func imageReps(with: Data) -> [NSImageRep]](./nsbitmapimagerep/imagereps%28with%29.md)
  Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.
- [func colorize(byMappingGray: CGFloat, to: NSColor?, blackMapping: NSColor?, whiteMapping: NSColor?)](./nsbitmapimagerep/colorize%28bymappinggray,to,blackmapping,whitemapping%29.md)
  Colorizes a grayscale image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bitmapFormat: NSBitmapImageRep.Format, bytesPerRow: Int, bitsPerPixel: Int)](./nsbitmapimagerep/init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bitmapformat,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bytesPerRow: Int, bitsPerPixel: Int)](./nsbitmapimagerep/init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init(cgImage: CGImage)](./nsbitmapimagerep/init%28cgimage%29-7o5tz.md)
  Returns a bitmap image representation from a Core Graphics image object.
- [init(ciImage: CIImage)](./nsbitmapimagerep/init%28ciimage%29-7bi19.md)
  Returns a bitmap image representation from a Core Image object.
- [init?(data: Data)](./nsbitmapimagerep/init%28data%29.md)
  Initializes a newly allocated bitmap image representation from the specified data.
- [init(forIncrementalLoad: ())](./nsbitmapimagerep/init%28forincrementalload%29.md)
  Initializes a newly allocated bitmap image representation for incremental loading.
- [init?(focusedViewRect: NSRect)](./nsbitmapimagerep/init%28focusedviewrect%29.md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.
- [+ imageRepWithData:](./nsbitmapimagerep/imagerepwithdata_.md)
  Creates and returns a bitmap image representation with the first image in the specified data.
### Getting Information About Images
- [var bitmapFormat: NSBitmapImageRep.Format](./nsbitmapimagerep/bitmapformat.md)
  The format of the bitmap image representation.
- [NSBitmapImageRep.Format](./nsbitmapimagerep/format.md)
  Constants that represent bitmap component formats.
- [var bitsPerPixel: Int](./nsbitmapimagerep/bitsperpixel.md)
  The number of bits allocated for each pixel in each plane of data.
- [var bytesPerPlane: Int](./nsbitmapimagerep/bytesperplane.md)
  The number of bytes in each plane or channel of data.
- [var bytesPerRow: Int](./nsbitmapimagerep/bytesperrow.md)
  The minimum number of bytes required to specify a scan line in each data plane.
- [var isPlanar: Bool](./nsbitmapimagerep/isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](./nsbitmapimagerep/numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](./nsbitmapimagerep/samplesperpixel.md)
  The number of components for each pixel.
### Getting the Bitmap Data
- [var bitmapData: UnsafeMutablePointer<UInt8>?](./nsbitmapimagerep/bitmapdata.md)
  A pointer to the bitmap data.
- [func getBitmapDataPlanes(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>)](./nsbitmapimagerep/getbitmapdataplanes%28_%29.md)
  Returns by indirection bitmap data of the bitmap image representation separated into planes.
### Producing Other Representations of Images
- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](./nsbitmapimagerep/tiffrepresentationofimagereps%28in%29.md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./nsbitmapimagerep/tiffrepresentationofimagereps%28in,using,factor%29.md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [var tiffRepresentation: Data?](./nsbitmapimagerep/tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./nsbitmapimagerep/tiffrepresentation%28using,factor%29.md)
  Returns a TIFF representation of the image using the specified compression.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./nsbitmapimagerep/representationofimagereps%28in,using,properties%29.md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./nsbitmapimagerep/representation%28using,properties%29.md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](./nsdrawbitmap%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Draws a bitmap image.
### Managing Compression Types
- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](./nsbitmapimagerep/gettiffcompressiontypes%28_,count%29.md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
- [class func localizedName(forTIFFCompressionType: NSBitmapImageRep.TIFFCompression) -> String?](./nsbitmapimagerep/localizedname%28fortiffcompressiontype%29.md)
  Returns an autoreleased string containing the localized name for the specified compression type.
- [func canBeCompressed(using: NSBitmapImageRep.TIFFCompression) -> Bool](./nsbitmapimagerep/canbecompressed%28using%29.md)
  Tests whether the bitmap image representation can be compressed by the specified compression scheme.
- [func setCompression(NSBitmapImageRep.TIFFCompression, factor: Float)](./nsbitmapimagerep/setcompression%28_,factor%29.md)
  Sets the bitmap image representation’s compression type and compression factor.
- [func getCompression(UnsafeMutablePointer<NSBitmapImageRep.TIFFCompression>?, factor: UnsafeMutablePointer<Float>?)](./nsbitmapimagerep/getcompression%28_,factor%29.md)
  Returns by indirection the bitmap image representation’s compression type and compression factor.
- [func setProperty(NSBitmapImageRep.PropertyKey, withValue: Any?)](./nsbitmapimagerep/setproperty%28_,withvalue%29.md)
  Sets the specified property of the bitmap image representation to the specified value.
- [func value(forProperty: NSBitmapImageRep.PropertyKey) -> Any?](./nsbitmapimagerep/value%28forproperty%29.md)
  Returns the value for the specified property.
- [NSBitmapImageRep.TIFFCompression](./nsbitmapimagerep/tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](./nsbitmapimagerep/propertykey.md)
  Constants that identify bitmap image representation properties.
### Loading Images Incrementally
- [func incrementalLoad(from: Data, complete: Bool) -> Int](./nsbitmapimagerep/incrementalload%28from,complete%29.md)
  Loads the current image data into an incrementally-loaded image representation and returns the current status of the image.
- [NSBitmapImageRep.LoadStatus](./nsbitmapimagerep/loadstatus.md)
  Constants that identify the loading status of the image.
### Managing Pixel Values
- [func setColor(NSColor, atX: Int, y: Int)](./nsbitmapimagerep/setcolor%28_,atx,y%29.md)
  Changes the color of the pixel at the specified coordinates.
- [func colorAt(x: Int, y: Int) -> NSColor?](./nsbitmapimagerep/colorat%28x,y%29.md)
  Returns the color of the pixel at the specified coordinates.
- [func setPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./nsbitmapimagerep/setpixel%28_,atx,y%29.md)
  Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.
- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./nsbitmapimagerep/getpixel%28_,atx,y%29.md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.
### Getting Core Graphics Images
- [var cgImage: CGImage?](./nsbitmapimagerep/cgimage.md)
  A Core Graphics image object based on the bitmap image representation’s data.
### Managing Color Spaces
- [func converting(to: NSColorSpace, renderingIntent: NSColorRenderingIntent) -> NSBitmapImageRep?](./nsbitmapimagerep/converting%28to,renderingintent%29.md)
  Converts the bitmap image representation to the specified color space.
- [func retagging(with: NSColorSpace) -> NSBitmapImageRep?](./nsbitmapimagerep/retagging%28with%29.md)
  Changes the color space tag of the bitmap image representation.
- [var colorSpace: NSColorSpace](./nsbitmapimagerep/colorspace.md)
  The color space of the bitmap.
### Constants
- [NSBitmapImageRep.FileType](./nsbitmapimagerep/filetype.md)
  Constants that specify bitmap file types.
### Initializers
- [init(CGImage: CGImage)](./nsbitmapimagerep/init%28cgimage%29-4e6yc.md)
- [init(CIImage: CIImage)](./nsbitmapimagerep/init%28ciimage%29-4ouvw.md)

## Relationships

### Inherits From
- [NSImageRep](./nsimagerep.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bitmap Formats
- [class NSCIImageRep](./nsciimagerep.md)
  An object that can render an image from a Core Image object.
- [class NSPICTImageRep](./nspictimagerep.md)
  An object that renders an image from a PICT format data stream of version 1, version 2, and extended version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep)*
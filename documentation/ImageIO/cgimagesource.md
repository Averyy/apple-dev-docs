# CGImageSource

**Framework**: Image I/O  
**Kind**: class  
**Role**: Class

An opaque type that you use to read image data from a URL, data object, or data consumer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CGImageSource
```

```c
typedef struct CGImageSource * CGImageSourceRef;
```

## Overview

Use a [`CGImageSource`](./cgimagesource.md) type to read data efficiently for most image file formats. The image source object manages the data buffers needed to load the image data and performs any operations on that data to turn it into a usable image. For example, it decompresses data stored in a compressed format. You can also use an image source to fetch or create thumbnail images and access metadata stored with the image.

Create an image source object from a [`CFURL`](../CoreFoundation/cfurl.md), [`CFData`](../CoreFoundation/cfdata.md), or [`CGDataProvider`](../CoreGraphics/cgdataprovider.md) data type. The image source object reads data from the specified type and extracts the image information for you.

For more information, see [Image I/O Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/imageio_intro/ikpg_intro.html#//apple_ref/doc/uid/TP40005462).

## Topics

### Creating an Image Source
- [func CGImageSourceCreateWithURL(CFURL, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithurl%28_,_%29.md)
  Creates an image source that reads from a location specified by a URL.
- [func CGImageSourceCreateWithData(CFData, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithdata%28_,_%29.md)
  Creates an image source that reads from a Core Foundation data object.
- [func CGImageSourceCreateWithDataProvider(CGDataProvider, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithdataprovider%28_,_%29.md)
  Creates an image source that reads data from the specified data provider.
- [func CGImageSourceCreateIncremental(CFDictionary?) -> CGImageSource](./cgimagesourcecreateincremental%28_%29.md)
  Creates an empty image source that you can use to accumulate incremental image data.
### Extracting Images From an Image Source
- [func CGImageSourceCreateImageAtIndex(CGImageSource, Int, CFDictionary?) -> CGImage?](./cgimagesourcecreateimageatindex%28_,_,_%29.md)
  Creates an image object from the data at the specified index in an image source.
- [func CGImageSourceCreateThumbnailAtIndex(CGImageSource, Int, CFDictionary?) -> CGImage?](./cgimagesourcecreatethumbnailatindex%28_,_,_%29.md)
  Creates a thumbnail version of the image at the specified index in an image source.
- [func CGImageSourceGetPrimaryImageIndex(CGImageSource) -> Int](./cgimagesourcegetprimaryimageindex%28_%29.md)
  Returns the index of the primary image for an High Efficiency Image File Format (HEIF) image.
### Getting Information From an Image Source
- [func CGImageSourceGetTypeID() -> CFTypeID](./cgimagesourcegettypeid%28%29.md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](./cgimagesourcegettype%28_%29.md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceCopyTypeIdentifiers() -> CFArray](./cgimagesourcecopytypeidentifiers%28%29.md)
  Returns an array of uniform type identifiers that are supported for image sources.
- [func CGImageSourceGetCount(CGImageSource) -> Int](./cgimagesourcegetcount%28_%29.md)
  Returns the number of images (not including thumbnails) in the image source.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](./cgimagesourcecopyproperties%28_,_%29.md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md)
  Returns the properties of the image at a specified location in an image source.
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](./cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.
### Updating an Incremental Image
- [func CGImageSourceUpdateData(CGImageSource, CFData, Bool)](./cgimagesourceupdatedata%28_,_,_%29.md)
  Updates the data in an incremental image source.
- [func CGImageSourceUpdateDataProvider(CGImageSource, CGDataProvider, Bool)](./cgimagesourceupdatedataprovider%28_,_,_%29.md)
  Updates an incremental image source with a new data provider.
### Getting the Image Status
- [func CGImageSourceGetStatus(CGImageSource) -> CGImageSourceStatus](./cgimagesourcegetstatus%28_%29.md)
  Return the status of an image source.
- [func CGImageSourceGetStatusAtIndex(CGImageSource, Int) -> CGImageSourceStatus](./cgimagesourcegetstatusatindex%28_,_%29.md)
  Returns the current status of an image at the specified location in the image source.
- [enum CGImageSourceStatus](./cgimagesourcestatus.md)
  The set of status values for images and image sources.
### Specifying the Read Options
- [let kCGImageSourceTypeIdentifierHint: CFString](./kcgimagesourcetypeidentifierhint.md)
  The uniform type identifier that represents your best guess for the image’s type.
- [let kCGImageSourceShouldAllowFloat: CFString](./kcgimagesourceshouldallowfloat.md)
  A Boolean that indicates whether to use floating-point values in returned images.
- [let kCGImageSourceShouldCache: CFString](./kcgimagesourceshouldcache.md)
  A Boolean value that indicates whether to cache the decoded image.
- [let kCGImageSourceShouldCacheImmediately: CFString](./kcgimagesourceshouldcacheimmediately.md)
  A Boolean value that indicates whether image decoding and caching happens at image creation time.
- [let kCGImageSourceCreateThumbnailFromImageIfAbsent: CFString](./kcgimagesourcecreatethumbnailfromimageifabsent.md)
  A Boolean value that indicates whether to create a thumbnail image automatically if the data source doesn’t contain one.
- [let kCGImageSourceCreateThumbnailFromImageAlways: CFString](./kcgimagesourcecreatethumbnailfromimagealways.md)
  A Boolean value that indicates whether to always create a thumbnail image.
- [let kCGImageSourceThumbnailMaxPixelSize: CFString](./kcgimagesourcethumbnailmaxpixelsize.md)
  The maximum width and height of a thumbnail image, specified in pixels.
- [let kCGImageSourceCreateThumbnailWithTransform: CFString](./kcgimagesourcecreatethumbnailwithtransform.md)
  A Boolean value that indicates whether to rotate and scale the thumbnail image to match the image’s orientation and aspect ratio.
- [let kCGImageSourceSubsampleFactor: CFString](./kcgimagesourcesubsamplefactor.md)
  The factor by which to scale down any returned images.
- [let kCGImageSourceAllowableTypes: CFString](./kcgimagesourceallowabletypes.md)
  Option key for restricting which image formats can be decoded.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Image Management
- [class CGImageDestination](./cgimagedestination.md)
  An opaque type that you use to write image data to a URL, data object, or data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesource)*
# CGImageDestination

**Framework**: Image I/O  
**Kind**: class

An opaque type that you use to write image data to a URL, data object, or data consumer.

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
class CGImageDestination
```

#### Overview

A [`CGImageDestination`](cgimagedestination.md) object provides an abstract interface for saving image data. Use an image destination to represent a single image, or multiple images packaged together. For example, you might create an image that also contains a thumbnail. You can also use the image destination to add metadata to your images.

An image destination outputs data to a URL, a `CFData` object, or a [`CGDataConsumer`](https://developer.apple.com/documentation/CoreGraphics/CGDataConsumer) object, which you specify at creation time. After you create the image destination, add the image data and properties. When you are done, call [`CGImageDestinationFinalize(_:)`](cgimagedestinationfinalize(_:).md) to finalize the image data and write it to the output location.

For more information, see [`Image I/O Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/imageio_intro/ikpg_intro.html#//apple_ref/doc/uid/TP40005462).

## Topics

### Creating an Image Destination
- [func CGImageDestinationCreateWithURL(CFURL, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithurl(_:_:_:_:).md)
  Creates an image destination that writes image data to the specified URL.
- [func CGImageDestinationCreateWithData(CFMutableData, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithdata(_:_:_:_:).md)
  Creates an image destination that writes to a Core Foundation mutable data object.
- [func CGImageDestinationCreateWithDataConsumer(CGDataConsumer, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithdataconsumer(_:_:_:_:).md)
  Creates an image destination that writes to the specified data consumer.
### Adding Images to the Destination
- [func CGImageDestinationAddImage(CGImageDestination, CGImage, CFDictionary?)](cgimagedestinationaddimage(_:_:_:).md)
  Adds an image to an image destination.
- [func CGImageDestinationAddImageFromSource(CGImageDestination, CGImageSource, Int, CFDictionary?)](cgimagedestinationaddimagefromsource(_:_:_:_:).md)
  Adds an image from an image source to an image destination.
### Adding Metadata to the Image
- [func CGImageDestinationSetProperties(CGImageDestination, CFDictionary?)](cgimagedestinationsetproperties(_:_:).md)
  Applies one or more properties to all images in an image destination.
- [func CGImageDestinationAddAuxiliaryDataInfo(CGImageDestination, CFString, CFDictionary)](cgimagedestinationaddauxiliarydatainfo(_:_:_:).md)
  Sets the auxiliary data, such as mattes and depth information, that accompany the image.
### Finalizing the Image Data
- [func CGImageDestinationFinalize(CGImageDestination) -> Bool](cgimagedestinationfinalize(_:).md)
  Writes image data and properties to the data, URL, or data consumer associated with the image destination.
### Getting the Image Types
- [func CGImageDestinationCopyTypeIdentifiers() -> CFArray](cgimagedestinationcopytypeidentifiers().md)
  Returns an array of the uniform type identifiers that are supported for image destinations.
- [func CGImageDestinationGetTypeID() -> CFTypeID](cgimagedestinationgettypeid().md)
  Returns the unique type identifier of an image destination opaque type.
### Configuring the Image Behaviors
- [let kCGImageDestinationLossyCompressionQuality: CFString](kcgimagedestinationlossycompressionquality.md)
  The desired compression quality to use when writing the image data.
- [let kCGImageDestinationBackgroundColor: CFString](kcgimagedestinationbackgroundcolor.md)
  The background color to use when the image has an alpha component, but the destination format doesn’t support alpha.
- [let kCGImageDestinationDateTime: CFString](kcgimagedestinationdatetime.md)
  The date and time information to associate with the image.
- [let kCGImageDestinationEmbedThumbnail: CFString](kcgimagedestinationembedthumbnail.md)
  A Boolean value that indicates whether to embed a thumbnail for JPEG and HEIF images.
- [let kCGImageDestinationImageMaxPixelSize: CFString](kcgimagedestinationimagemaxpixelsize.md)
  The maximum width and height of the image, in pixels.
- [let kCGImageDestinationMetadata: CFString](kcgimagedestinationmetadata.md)
  The metadata tags to include with the image.
- [let kCGImageDestinationMergeMetadata: CFString](kcgimagedestinationmergemetadata.md)
  A Boolean value that indicates whether to merge new metadata with the image’s existing metadata.
- [let kCGImageDestinationOptimizeColorForSharing: CFString](kcgimagedestinationoptimizecolorforsharing.md)
  A Boolean value that indicates whether to create the image using a colorspace.
- [let kCGImageDestinationOrientation: CFString](kcgimagedestinationorientation.md)
  The orientation of the image, specified as an EXIF value in the range 1 to 8.
- [let kCGImageDestinationPreserveGainMap: CFString](kcgimagedestinationpreservegainmap.md)
  A Boolean value that indicates whether to include a HEIF-embedded gain map in the image data.
- [let kCGImageMetadataShouldExcludeGPS: CFString](kcgimagemetadatashouldexcludegps.md)
  A Boolean value that indicates whether to exclude GPS metadata from EXIF data or the corresponding XMP tags.
- [let kCGImageMetadataShouldExcludeXMP: CFString](kcgimagemetadatashouldexcludexmp.md)
  A Boolean value that indicates whether to exclude XMP data from the destination.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CGImageSource](cgimagesource.md)
  An opaque type that you use to read image data from a URL, data object, or data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestination)*
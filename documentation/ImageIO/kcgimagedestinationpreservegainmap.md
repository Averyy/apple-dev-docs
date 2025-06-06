# kCGImageDestinationPreserveGainMap

**Framework**: Image I/O  
**Kind**: var

A Boolean value that indicates whether to include a HEIF-embedded gain map in the image data.

**Availability**:
- iOS 14.1+
- iPadOS 14.1+
- Mac Catalyst 14.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let kCGImageDestinationPreserveGainMap: CFString
```

#### Discussion

The value of this key must be a [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) value. The default value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse). If you scale the destination image using the [`kCGImageDestinationImageMaxPixelSize`](kcgimagedestinationimagemaxpixelsize.md) key, the destination also scales the gain map.

## See Also

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
- [let kCGImageMetadataShouldExcludeGPS: CFString](kcgimagemetadatashouldexcludegps.md)
  A Boolean value that indicates whether to exclude GPS metadata from EXIF data or the corresponding XMP tags.
- [let kCGImageMetadataShouldExcludeXMP: CFString](kcgimagemetadatashouldexcludexmp.md)
  A Boolean value that indicates whether to exclude XMP data from the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagedestinationpreservegainmap)*
# kCGImageDestinationMergeMetadata

**Framework**: Image I/O  
**Kind**: var

A Boolean value that indicates whether to merge new metadata with the image’s existing metadata.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImageDestinationMergeMetadata: CFString
```

#### Discussion

The value of this key must be a [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) value. The default value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse).

If you set this key to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), the image destination merges the information in the [`kCGImageDestinationMetadata`](kcgimagedestinationmetadata.md) key with the image’s existing metadata. Specifically, if a tag doesn’t exist in the source, the destination adds it. If the tag exists in the source, the destination updates its value. To remove a tag, set the value of the appropriate key to [`kCFNull`](https://developer.apple.com/documentation/CoreFoundation/kCFNull).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagedestinationmergemetadata)*
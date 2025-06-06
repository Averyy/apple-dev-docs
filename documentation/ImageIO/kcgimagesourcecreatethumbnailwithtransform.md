# kCGImageSourceCreateThumbnailWithTransform

**Framework**: Image I/O  
**Kind**: var

A Boolean value that indicates whether to rotate and scale the thumbnail image to match the image’s orientation and aspect ratio.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImageSourceCreateThumbnailWithTransform: CFString
```

#### Discussion

The value of this key must be a CFBoolean value. The default value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse).

## See Also

- [let kCGImageSourceTypeIdentifierHint: CFString](kcgimagesourcetypeidentifierhint.md)
  The uniform type identifier that represents your best guess for the image’s type.
- [let kCGImageSourceShouldAllowFloat: CFString](kcgimagesourceshouldallowfloat.md)
  A Boolean that indicates whether to use floating-point values in returned images.
- [let kCGImageSourceShouldCache: CFString](kcgimagesourceshouldcache.md)
  A Boolean value that indicates whether to cache the decoded image.
- [let kCGImageSourceShouldCacheImmediately: CFString](kcgimagesourceshouldcacheimmediately.md)
  A Boolean value that indicates whether image decoding and caching happens at image creation time.
- [let kCGImageSourceCreateThumbnailFromImageIfAbsent: CFString](kcgimagesourcecreatethumbnailfromimageifabsent.md)
  A Boolean value that indicates whether to create a thumbnail image automatically if the data source doesn’t contain one.
- [let kCGImageSourceCreateThumbnailFromImageAlways: CFString](kcgimagesourcecreatethumbnailfromimagealways.md)
  A Boolean value that indicates whether to always create a thumbnail image.
- [let kCGImageSourceThumbnailMaxPixelSize: CFString](kcgimagesourcethumbnailmaxpixelsize.md)
  The maximum width and height of a thumbnail image, specified in pixels.
- [let kCGImageSourceSubsampleFactor: CFString](kcgimagesourcesubsamplefactor.md)
  The factor by which to scale down any returned images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagesourcecreatethumbnailwithtransform)*
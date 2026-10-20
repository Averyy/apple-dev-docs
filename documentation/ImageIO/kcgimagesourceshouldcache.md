# kCGImageSourceShouldCache

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

A Boolean value that indicates whether to cache the decoded image.

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
let kCGImageSourceShouldCache: CFString
```

```c
extern CFStringRef const kCGImageSourceShouldCache;
```

#### Discussion

The value of this key is a [`CFBoolean`](../CoreFoundation/cfboolean.md). The default value is [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for 64-bit architectures, and [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for 32-bit architectures.

Include this key in the options dictionary you pass to the functions [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md) and [`CGImageSourceCreateImageAtIndex(_:_:_:)`](./cgimagesourcecreateimageatindex%28_,_,_%29.md).

## See Also

### Specifying the Read Options
- [let kCGImageSourceTypeIdentifierHint: CFString](./kcgimagesourcetypeidentifierhint.md)
  The uniform type identifier that represents your best guess for the image’s type.
- [let kCGImageSourceShouldAllowFloat: CFString](./kcgimagesourceshouldallowfloat.md)
  A Boolean that indicates whether to use floating-point values in returned images.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagesourceshouldcache)*
# kCGImageSourceAllowableTypes

**Framework**: Image I/O  
**Kind**: var

Option key for restricting which image formats can be decoded.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
let kCGImageSourceAllowableTypes: CFString
```

#### Discussion

The value is a [`CFArray`](https://developer.apple.com/documentation/corefoundation/cfarray) containing [`CFString`](https://developer.apple.com/documentation/corefoundation/cfstring) Uniform Type Identifiers (UTIs) of allowed image formats. When specified, ImageIO will only decode images whose format matches one of the entries in the allow list. If no matching reader is found, decoding fails.

Unknown format identifiers are ignored. If not specified, all supported ImageIO formats are allowed (default behavior). If process-wide format restrictions were set via [`CGImageSourceSetAllowableTypes(_:)`](cgimagesourcesetallowabletypes(_:).md), only formats allowed by both mechanisms are permitted.

See also [`System-declared uniform type identifiers`](https://developer.apple.com/documentation/uniformtypeidentifiers/system-declared-uniform-type-identifiers).

#### Example

**Swift**:

```swift
let allowedTypes = ["public.jpeg" as CFString, "public.png" as CFString]
let options = [
    kCGImageSourceAllowableTypes: allowedTypes
] as CFDictionary
```

**Objective-C**:

```objc
NSArray *allowedTypes = @[@"public.jpeg", @"public.png"];
NSDictionary *options = @{
    (id)kCGImageSourceAllowableTypes: allowedTypes
};
```

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
- [let kCGImageSourceCreateThumbnailWithTransform: CFString](kcgimagesourcecreatethumbnailwithtransform.md)
  A Boolean value that indicates whether to rotate and scale the thumbnail image to match the image’s orientation and aspect ratio.
- [let kCGImageSourceSubsampleFactor: CFString](kcgimagesourcesubsamplefactor.md)
  The factor by which to scale down any returned images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagesourceallowabletypes)*
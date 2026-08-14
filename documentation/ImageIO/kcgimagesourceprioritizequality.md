# kCGImageSourcePrioritizeQuality

**Framework**: Image I/O  
**Kind**: var

A Boolean value that indicates whether to prioritize image quality over decode speed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let kCGImageSourcePrioritizeQuality: CFString
```

#### Discussion

When you set this key to [`kCFBooleanTrue`](https://developer.apple.com/documentation/corefoundation/kcfbooleantrue), the image source decodes the full-size image using the highest-quality decode method available for the file. The value of this key is a [`CFBoolean`](https://developer.apple.com/documentation/corefoundation/cfboolean). The default value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/corefoundation/kcfbooleanfalse).

Currently, image sources support this option only for camera RAW images. This key is a no-op when it is absent or [`kCFBooleanFalse`](https://developer.apple.com/documentation/corefoundation/kcfbooleanfalse), when the image isn’t a camera RAW format, or when no higher-quality decode method is available, so it is always safe to set.

Include this key in the options dictionary you pass to the functions [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](cgimagesourcecopypropertiesatindex(_:_:_:).md) and [`CGImageSourceCreateImageAtIndex(_:_:_:)`](cgimagesourcecreateimageatindex(_:_:_:).md).

#### Example

**Swift**:

```swift
let options = [
    kCGImageSourcePrioritizeQuality: true
] as CFDictionary
let image = CGImageSourceCreateImageAtIndex(source, 0, options)
```

**Objective-C**:

```objc
NSDictionary *options = @{
    (id)kCGImageSourcePrioritizeQuality: @YES
};
CGImageRef image = CGImageSourceCreateImageAtIndex(source, 0, (CFDictionaryRef)options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagesourceprioritizequality)*
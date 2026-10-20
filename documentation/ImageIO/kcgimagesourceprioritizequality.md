# kCGImageSourcePrioritizeQuality

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

A Boolean value that indicates whether to prioritize image quality over decode speed.

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
let kCGImageSourcePrioritizeQuality: CFString
```

```c
extern CFStringRef const kCGImageSourcePrioritizeQuality;
```

#### Discussion

When you set this key to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), the image source decodes the full-size image using the highest-quality decode method available for the file. The value of this key is a [`CFBoolean`](../CoreFoundation/cfboolean.md). The default value is [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md).

Currently, image sources support this option only for camera RAW images. This key is a no-op when it is absent or [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md), when the image isn’t a camera RAW format, or when no higher-quality decode method is available, so it is always safe to set.

Include this key in the options dictionary you pass to the functions [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md) and [`CGImageSourceCreateImageAtIndex(_:_:_:)`](./cgimagesourcecreateimageatindex%28_,_,_%29.md).

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
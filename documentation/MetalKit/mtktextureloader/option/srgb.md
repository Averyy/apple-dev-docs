# SRGB

**Framework**: MetalKit  
**Kind**: property

A key used to specify whether the texture data is stored as sRGB image data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let SRGB: MTKTextureLoader.Option
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a boolean value.

If the value is [`false`](https://developer.apple.com/documentation/swift/false), the image data is treated as linear pixel data. If the value is [`true`](https://developer.apple.com/documentation/swift/true), the image data is treated as sRGB pixel data. If this key is not specified and the image being loaded has been gamma-corrected, the image data uses the specified sRGB information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/srgb)*
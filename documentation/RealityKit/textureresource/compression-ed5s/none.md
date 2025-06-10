# none

**Framework**: RealityKit  
**Kind**: property

A texture you can create with no compression.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
static var none: TextureResource.Compression { get }
```

#### Discussion

If you export this to a `.reality` file using [`write(to:)`](entity/write(to:).md), the texture remains uncompressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression-ed5s/none)*
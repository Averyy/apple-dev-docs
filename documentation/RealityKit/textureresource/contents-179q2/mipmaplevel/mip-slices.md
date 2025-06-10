# mip(slices:)

**Framework**: RealityKit  
**Kind**: method

Specifies a single mipmap level of a 2D or 3D texture resource that slices provide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
static func mip(slices: [TextureResource.Contents.Slice]) -> TextureResource.Contents.MipmapLevel
```

## Parameters

- `slices`: The source slices.   A 2D array texture requires one slice per  .   A cube texture requires six slices, containing faces  .   2D and 3D textures need a single slice, and you can build their   with    or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents-179q2/mipmaplevel/mip(slices:))*
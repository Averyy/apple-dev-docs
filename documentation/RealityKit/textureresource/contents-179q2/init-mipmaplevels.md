# init(mipmapLevels:)

**Framework**: RealityKit  
**Kind**: init

Creates a texture contents object from an array of mipmaps.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
init(mipmapLevels: [TextureResource.Contents.MipmapLevel])
```

#### Discussion

> **Note**: Creating 3D textures requires you to build `MipmapLevel` with `mip()` methods that have a `bytesPerImage` parameter.

## Parameters

- `mipmapLevels`: Pixel data for each mipmap level, starting with mipmap level  .   Supply at least one mipmap level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents-179q2/init(mipmaplevels:))*
# replace(with:)

**Framework**: RealityKit  
**Kind**: method

Replaces a texture resource with a low-level texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func replace(with texture: LowLevelTexture)
```

#### Discussion

> ⚠️ **Warning**: It’s more efficient to use [`replace(using:)`](lowleveltexture/replace(using:).md) to update a [`LowLevelTexture`](lowleveltexture.md) on the GPU than it is to update the `TextureResource`. Prefer to update the `LowLevelTexture` directly instead.

## Parameters

- `texture`: The texture data that defines the resource.

## See Also

- [func replace(withDrawables: TextureResource.DrawableQueue)](textureresource/replace(withdrawables:).md)
  Dynamically replaces the texture with a drawable queue.
- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](textureresource/replace(withimage:options:).md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(using:options:)](textureresource/replace(using:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(with:))*
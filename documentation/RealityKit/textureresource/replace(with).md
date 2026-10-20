# replace(with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replaces a texture resource with a low-level texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func replace(with texture: LowLevelTexture)
```

#### Discussion

> ⚠️ **Warning**: It’s more efficient to use [`replace(using:)`](../lowleveltexture/replace%28using%29.md) to update a [`LowLevelTexture`](../lowleveltexture.md) on the GPU than it is to update the `TextureResource`. Prefer to update the `LowLevelTexture` directly instead.

> **Note**: This method marks the asset as mutated, preventing newly loaded entities from sharing the texture.

## Parameters

- `texture`: The texture data that defines the resource.

## See Also

### Modifying the texture
- [func replace(withDrawables: TextureResource.DrawableQueue)](./replace%28withdrawables%29.md)
  Dynamically replaces the texture with a drawable queue.
- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](./replace%28withimage,options%29.md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(using: CGImage, options: TextureResource.CreateOptions) async throws](./replace%28using,options%29.md)
  Asynchronously replaces the texture with a Core Graphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(with:))*
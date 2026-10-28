# replace(withImage:options:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Dynamically replaces the texture with a Core Graphics image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func replace(withImage cgImage: CGImage, options: TextureResource.CreateOptions) throws
```

## Discussion

This method blocks until the resource updates. Don’t use this method for updates at frame-rate frequency. For frequent texture changes, see [`replace(withDrawables:)`](./replace%28withdrawables%29.md). If you have an attached [`TextureResource.DrawableQueue`](./drawablequeue-swift.class.md) on this resource, this function detaches it.

To  ensure consistent usage of this texture resource, pass the same semantic in `options` that you use to create the resource.

> **Note**: The contents of a modified texture resource don’t sync between network clients.

## Parameters

- `cgImage`: The source image.
- `options`: Options that specify the type of texture to create.

## See Also

### Modifying the texture
- [func replace(withDrawables: TextureResource.DrawableQueue)](./replace%28withdrawables%29.md)
  Dynamically replaces the texture with a drawable queue.
- [func replace(using: CGImage, options: TextureResource.CreateOptions) async throws](./replace%28using,options%29.md)
  Asynchronously replaces the texture with a Core Graphics image.
- [func replace(with: LowLevelTexture)](./replace%28with%29.md)
  Replaces a texture resource with a low-level texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(withimage:options:))*
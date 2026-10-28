# replace(using:options:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously replaces the texture with a Core Graphics image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func replace(using cgImage: CGImage, options: TextureResource.CreateOptions) async throws
```

## Discussion

Don’t use this method for updates at frame-rate frequency. For frequent texture changes, see [`replace(withDrawables:)`](./replace%28withdrawables%29.md). To ensure consistent usage of this texture resource, pass the same semantic in `options` that you use to create the resource.

> **Note**: The contents of a modified texture resource don’t sync between network clients.

## Parameters

- `cgImage`: The source image.
- `options`: Options that specify the type of texture to create. To preserve `TextureResource` usage, specify the same semantic.

## See Also

### Modifying the texture
- [func replace(withDrawables: TextureResource.DrawableQueue)](./replace%28withdrawables%29.md)
  Dynamically replaces the texture with a drawable queue.
- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](./replace%28withimage,options%29.md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(with: LowLevelTexture)](./replace%28with%29.md)
  Replaces a texture resource with a low-level texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(using:options:))*
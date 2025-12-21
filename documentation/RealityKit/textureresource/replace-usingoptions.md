# replace(using:options:)

**Framework**: RealityKit  
**Kind**: method

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

#### Discussion

Don’t use this method for updates at frame-rate frequency. For frequent texture changes, see [`replace(withDrawables:)`](textureresource/replace(withdrawables:).md). To ensure consistent usage of this texture resource, pass the same semantic in `options` that you use to create the resource.

> **Note**: The contents of a modified texture resource don’t sync between network clients.

## Parameters

- `cgImage`: The source image.
- `options`: Options that specify the type of texture to create. To preserve   usage, specify the same semantic.

## See Also

- [func replace(withDrawables: TextureResource.DrawableQueue)](textureresource/replace(withdrawables:).md)
  Dynamically replaces the texture with a drawable queue.
- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](textureresource/replace(withimage:options:).md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(with: LowLevelTexture)](textureresource/replace(with:).md)
  Replaces a texture resource with a low-level texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(using:options:))*
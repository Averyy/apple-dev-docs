# replace(withDrawables:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Dynamically replaces the texture with a drawable queue.

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
@preconcurrency func replace(withDrawables drawableQueue: TextureResource.DrawableQueue)
```

## See Also

### Modifying the texture
- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](./replace%28withimage,options%29.md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(using: CGImage, options: TextureResource.CreateOptions) async throws](./replace%28using,options%29.md)
  Asynchronously replaces the texture with a Core Graphics image.
- [func replace(with: LowLevelTexture)](./replace%28with%29.md)
  Replaces a texture resource with a low-level texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(withdrawables:))*
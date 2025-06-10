# replace(withDrawables:)

**Framework**: RealityKit  
**Kind**: method

Dynamically replaces the texture with a drawable queue.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func replace(withDrawables drawableQueue: TextureResource.DrawableQueue)
```

## See Also

- [func replace(withImage: CGImage, options: TextureResource.CreateOptions) throws](textureresource/replace(withimage:options:).md)
  Dynamically replaces the texture with a Core Graphics image.
- [func replace(using:options:)](textureresource/replace(using:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.
- [func replace(with:)](textureresource/replace(with:).md)
  Replaces a texture resource with a low-level texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replace(withdrawables:))*
# replaceAsync(withImage:options:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously replaces the texture with a Core Graphics image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func replaceAsync(withImage cgImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>
```

#### Discussion

Don’t use this method for updates at frame-rate frequency. For frequent texture changes, see [`replace(withDrawables:)`](textureresource/replace(withdrawables:).md). To ensure consistent usage of this texture resource, pass the same semantic in `options` that you use to create the resource.

> **Note**: The contents of a modified texture resource don’t sync between network clients.

## Parameters

- `cgImage`: The source image.
- `options`: Options that specify the type of texture to create.   To preserve   usage, specify the same semantic.

## See Also

- [static func generate(from: CGImage, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/generate(from:withname:options:).md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/generateasync(from:withname:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static generate(from:named:options:)](textureresource/generate(from:named:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static func loadAsync(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/loadasync(contentsof:withname:options:).md)
  Asynchronously loads a texture resource from a URL with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replaceasync(withimage:options:))*
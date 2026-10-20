# replaceAsync(withImage:options:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously replaces the texture with a Core Graphics image.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: replace(using:options:))
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: replace(using:options:))
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: replace(using:options:))
- macOS 12.0+ - Deprecated in 15.0 (renamed: replace(using:options:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: replace(using:options:))

## Declaration

```swift
@MainActor
@preconcurrency func replaceAsync(withImage cgImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>
```

#### Discussion

Don’t use this method for updates at frame-rate frequency. For frequent texture changes, see [`replace(withDrawables:)`](./replace%28withdrawables%29.md). To ensure consistent usage of this texture resource, pass the same semantic in `options` that you use to create the resource.

> **Note**: The contents of a modified texture resource don’t sync between network clients.

## Parameters

- `cgImage`: The source image.
- `options`: Options that specify the type of texture to create. To preserve `TextureResource` usage, specify the same semantic.

## See Also

### Deprecated
- [static func generate(from: CGImage, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](./generate%28from,withname,options%29.md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](./generateasync%28from,withname,options%29.md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static func generate(from: CGImage, named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](./generate%28from,named,options%29.md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static func loadAsync(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](./loadasync%28contentsof,withname,options%29.md)
  Asynchronously loads a texture resource from a URL with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/replaceasync(withimage:options:))*
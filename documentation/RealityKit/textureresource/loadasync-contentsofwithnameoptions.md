# loadAsync(contentsOf:withName:options:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads a texture resource from a URL with options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(contentsOf url: URL, withName resourceName: String? = nil, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>
```

#### Return Value

A load operation that publishes the resource.

#### Discussion

RealityKit uses the resource name to distinguish resources locally, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `url`: The path or address of the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.
- `options`: A configuration for generating the texture.

## See Also

- [static func generate(from: CGImage, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/generate(from:withname:options:).md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/generateasync(from:withname:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [func replaceAsync(withImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/replaceasync(withimage:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.
- [static func generate(from: CGImage, named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/generate(from:named:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/loadasync(contentsof:withname:options:))*
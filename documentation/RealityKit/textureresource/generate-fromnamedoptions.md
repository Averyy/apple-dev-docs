# generate(from:named:options:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously generates a texture resource from an in-memory Core Graphics image.

**Availability**:
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(from cgImage: CGImage, named resourceName: String? = nil, options: TextureResource.CreateOptions) async throws -> TextureResource
```

#### Return Value

A texture resource.

#### Discussion

This method creates a texture resource from an existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) with specific options. RealityKit uses the resource name to identify resources, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `cgImage`: The source image.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.

## See Also

- [static func generate(from: CGImage, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/generate(from:withname:options:).md)
  Synchronously creates a texture resource from an in-memory Core Graphics image.
- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/generateasync(from:withname:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [func replaceAsync(withImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/replaceasync(withimage:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.
- [static func loadAsync(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/loadasync(contentsof:withname:options:).md)
  Asynchronously loads a texture resource from a URL with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/generate(from:named:options:))*
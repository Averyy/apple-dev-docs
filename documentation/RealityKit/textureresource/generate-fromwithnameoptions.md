# generate(from:withName:options:)

**Framework**: RealityKit  
**Kind**: method

Synchronously creates a texture resource from an in-memory Core Graphics image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(from cgImage: CGImage, withName resourceName: String? = nil, options: TextureResource.CreateOptions) throws -> TextureResource
```

#### Return Value

A texture resource.

#### Discussion

This method creates a texture resource from an existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) with specific options.

RealityKit uses the resource name to identify resources, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `cgImage`: The source image.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.

## See Also

- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/generateasync(from:withname:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [func replaceAsync(withImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/replaceasync(withimage:options:).md)
  Asynchronously replaces the texture with a Core Graphics image.
- [static func generate(from: CGImage, named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/generate(from:named:options:).md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static func loadAsync(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](textureresource/loadasync(contentsof:withname:options:).md)
  Asynchronously loads a texture resource from a URL with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/generate(from:withname:options:))*
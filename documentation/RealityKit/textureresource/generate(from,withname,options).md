# generate(from:withName:options:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Synchronously creates a texture resource from an in-memory Core Graphics image.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: init(image:withName:options:))
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: init(image:withName:options:))
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: init(image:withName:options:))
- macOS 12.0+ - Deprecated in 15.0 (renamed: init(image:withName:options:))
- visionOS 1.0+ - Deprecated in 2.0 (renamed: init(image:withName:options:))

## Declaration

```swift
@MainActor
@preconcurrency static func generate(from cgImage: CGImage, withName resourceName: String? = nil, options: TextureResource.CreateOptions) throws -> TextureResource
```

#### Return Value

A texture resource.

#### Discussion

This method creates a texture resource from an existing [`CGImage`](../../CoreGraphics/cgimage.md) with specific options.

RealityKit uses the resource name to identify resources, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `cgImage`: The source image.
- `resourceName`: A unique name for syncing the texture resource across the network. The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.

## See Also

### Deprecated
- [static func generateAsync(from: CGImage, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](./generateasync%28from,withname,options%29.md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [func replaceAsync(withImage: CGImage, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](./replaceasync%28withimage,options%29.md)
  Asynchronously replaces the texture with a Core Graphics image.
- [static func generate(from: CGImage, named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](./generate%28from,named,options%29.md)
  Asynchronously generates a texture resource from an in-memory Core Graphics image.
- [static func loadAsync(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](./loadasync%28contentsof,withname,options%29.md)
  Asynchronously loads a texture resource from a URL with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/generate(from:withname:options:))*
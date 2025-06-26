# loadAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads a texture resource from a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<TextureResource>
```

#### Return Value

A load operation that publishes the resource.

#### Discussion

RealityKit uses the resource name to distinguish resources locally, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `url`: The path or address of the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [convenience(named:in:)](textureresource/init(named:in:).md)
  Asynchronously loads a texture resource from a bundle.
- [convenience(named:in:options:)](textureresource/init(named:in:options:).md)
  Asynchronously loads a texture resource from a bundle with options.
- [convenience(contentsOf:withName:options:)](textureresource/init(contentsof:withname:options:).md)
  Asynchronously creates a texture resource from a file URL with creation options.
- [convenience(contentsOf:withName:)](textureresource/init(contentsof:withname:).md)
  Synchronously creates a texture resource from a file URL.
- [static load(named:in:)](textureresource/load(named:in:).md)
  Returns a texture resource by synchronously loading it from a bundle.
- [static load(named:in:options:)](textureresource/load(named:in:options:).md)
  Returns a texture resource by synchronously loading it from a bundle with options.
- [static func load(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/load(contentsof:withname:options:).md)
  Synchronously loads a texture resource from a URL with options.
- [static func load(contentsOf: URL, withName: String?) throws -> TextureResource](textureresource/load(contentsof:withname:).md)
  Synchronously loads a texture resource from a URL.
- [static loadAsync(named:in:)](textureresource/loadasync(named:in:).md)
  Returns a load request that creates a texture resource by asynchronously loading it from a bundle.
- [static loadAsync(named:in:options:)](textureresource/loadasync(named:in:options:).md)
  Returns a load request that creates a texture resource by asynchronously loading it from a bundle with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/loadasync(contentsof:withname:))*
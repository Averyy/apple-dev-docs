# init(named:in:options:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously loads a texture resource from a bundle with options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(named name: String, in bundle: Bundle? = nil, options: TextureResource.CreateOptions) async throws
```

#### Discussion

RealityKit automatically creates a resource name for the texture resource based on the values of `name` and `bundle`. RealityKit uses the resource name to identify resources, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

See [`init(named:in:)`](textureresource/init(named:in:).md) for an example of optimally loading textures with other content.

## Parameters

- `name`: The name of the resource. The filename extension is optional.
- `bundle`: The bundle to search for the resource. Use   to indicate the app’s bundle.
- `options`: Configuration options for texture creation.

## See Also

- [convenience(named:in:)](textureresource/init(named:in:).md)
  Asynchronously loads a texture resource from a bundle.
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
- [static func loadAsync(contentsOf: URL, withName: String?) -> LoadRequest<TextureResource>](textureresource/loadasync(contentsof:withname:).md)
  Asynchronously loads a texture resource from a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(named:in:options:))*
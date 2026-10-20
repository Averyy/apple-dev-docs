# init(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously creates a texture resource from a file URL.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(contentsOf url: URL, withName resourceName: String? = nil) async throws
```

## Parameters

- `url`: The path or address of the file to load into the texture resource.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

### Loading a texture
- [convenience init(named: String, in: Bundle?) async throws](./init%28named,in%29.md)
  Asynchronously loads a texture resource from a bundle.
- [convenience init(named: String, in: Bundle?, options: TextureResource.CreateOptions) async throws](./init%28named,in,options%29.md)
  Asynchronously loads a texture resource from a bundle with options.
- [convenience init(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) async throws](./init%28contentsof,withname,options%29.md)
  Asynchronously creates a texture resource from a file URL with creation options.
- [static func load(named: String, in: Bundle?) throws -> TextureResource](./load%28named,in%29.md)
  Returns a texture resource by synchronously loading it from a bundle.
- [static func load(named: String, in: Bundle?, options: TextureResource.CreateOptions) throws -> TextureResource](./load%28named,in,options%29.md)
  Returns a texture resource by synchronously loading it from a bundle with options.
- [static func load(contentsOf: URL, withName: String?, options: TextureResource.CreateOptions) throws -> TextureResource](./load%28contentsof,withname,options%29.md)
  Synchronously loads a texture resource from a URL with options.
- [static func load(contentsOf: URL, withName: String?) throws -> TextureResource](./load%28contentsof,withname%29.md)
  Synchronously loads a texture resource from a URL.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<TextureResource>](./loadasync%28named,in%29.md)
  Returns a load request that creates a texture resource by asynchronously loading it from a bundle.
- [static func loadAsync(named: String, in: Bundle?, options: TextureResource.CreateOptions) -> LoadRequest<TextureResource>](./loadasync%28named,in,options%29.md)
  Returns a load request that creates a texture resource by asynchronously loading it from a bundle with options.
- [static func loadAsync(contentsOf: URL, withName: String?) -> LoadRequest<TextureResource>](./loadasync%28contentsof,withname%29.md)
  Asynchronously loads a texture resource from a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(contentsof:withname:))*
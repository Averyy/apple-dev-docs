# load(named:in:options:)

**Framework**: RealityKit  
**Kind**: method

Returns a texture resource by synchronously loading it from a bundle with options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency static func load(named name: String, in bundle: Bundle? = nil, options: TextureResource.CreateOptions) throws -> TextureResource
```

#### Return Value

The loaded resource.

#### Discussion

Loading a [`TextureResource`](textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](textureresource/init(named:in:).md) for an example that demonstrates how to safely load content.

This method loads the image that the `URL` specifies, and creates a texture resource from it. The method blocks until it finishes loading the image and creating the texture resource. RealityKit automatically creates a resource name based on the `name` and `bundle` values.

RealityKit uses the resource name to identify resources, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `name`: The name of the resource. The filename extension is optional.
- `bundle`: The bundle to search for the resource. Use   to indicate the app’s bundle.
- `options`: Configurable options that affect texture loading.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/load(named:in:options:))*
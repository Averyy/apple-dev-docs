# init(dimensions:format:contents:)

**Framework**: RealityKit  
**Kind**: init

Synchronously creates a 3D texture resource from a pixel Metal buffer, or data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) throws
```

#### Discussion

RealityKit efficiently creates a 3D texture from raw pixel bytes, with full control over the values and pixel format. See [`init(dimensions:format:contents:)`](textureresource/init(dimensions:format:contents:)-64sua.md) for more details.

Loading a [`TextureResource`](textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](textureresource/init(named:in:).md) for an example that demonstrates how to safely load content.

## Parameters

- `dimensions`: The dimensions of the 3D texture to create.
- `format`: The semantic interpretation of the pixel data.
- `contents`: Pixel data the system copies into the created texture.

## See Also

- [static func texture3D(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/texture3d(slices:named:options:)-6pude.md)
  Asynchronously creates a 3D texture by generating it from images.
- [static func texture3D(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) throws -> TextureResource](textureresource/texture3d(slices:named:options:)-orb.md)
  Synchronously creates a 3D texture by generating it from images.
- [convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-64sua.md)
  Asynchronously creates a 3D texture resource from a pixel Metal buffer, or data.
- [TextureResource.Dimensions3D](textureresource/dimensions3d.md)
  The dimensions of the 3D texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(dimensions:format:contents:)-5l84l)*
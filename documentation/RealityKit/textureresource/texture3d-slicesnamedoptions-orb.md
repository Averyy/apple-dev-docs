# texture3D(slices:named:options:)

**Framework**: RealityKit  
**Kind**: method

Synchronously creates a 3D texture by generating it from images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func texture3D(slices: [CGImage], named resourceName: String? = nil, options: TextureResource.CreateOptions) throws -> TextureResource
```

#### Discussion

RealityKit creates a [`MTLTextureType.type3D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type3D) texture with `depth == slices.count` from an array of images.

You can assign the resulting texture to a material you create in Reality Composer Pro that requires a 3D texture.

Loading a [`TextureResource`](textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](textureresource/init(named:in:).md) for an example that demonstrates how to safely load content.

```swift
// Create a 3D texture from image slices.
let texture3D = try TextureResource.texture3D(
    slices: [image0, image1, image2, image3],
    options: TextureResource.CreateOptions(semantic: .color))

Task {
    // Assign the 3D texture to a compatible shader graph material parameter.
    var material = try await ShaderGraphMaterial(
        named: "/Root/Alien/MaterialWith3DTexture", from: url)

    try material.setParameter(
        name: "input3DTexture",
        value: .textureResource(texture3D))
}
```

## Parameters

- `slices`: The source images, one per depth index.   All images need to be square, and of equal size and format.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.

## See Also

- [static func texture3D(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/texture3d(slices:named:options:)-6pude.md)
  Asynchronously creates a 3D texture by generating it from images.
- [convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-5l84l.md)
  Synchronously creates a 3D texture resource from a pixel Metal buffer, or data.
- [convenience init(dimensions: TextureResource.Dimensions3D, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-64sua.md)
  Asynchronously creates a 3D texture resource from a pixel Metal buffer, or data.
- [TextureResource.Dimensions3D](textureresource/dimensions3d.md)
  The dimensions of the 3D texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/texture3d(slices:named:options:)-orb)*
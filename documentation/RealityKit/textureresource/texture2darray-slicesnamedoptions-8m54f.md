# texture2DArray(slices:named:options:)

**Framework**: RealityKit  
**Kind**: method

Synchronously creates a 2D texture array by generating it from images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func texture2DArray(slices: [CGImage], named resourceName: String? = nil, options: TextureResource.CreateOptions) throws -> TextureResource
```

#### Discussion

RealityKit creates a [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray) texture with`'arrayLength == slices.count` from an array of images.

You can assign the resulting texture to a material you create in Reality Composer Pro that requires a 2D texture array.

Loading a [`TextureResource`](textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](textureresource/init(named:in:).md) for an example that demonstrates how to safely load content.

```swift
// Create a 2D array texture from image slices.
let texture2DArray = try await TextureResource.texture2DArray(
    slices: [image0, image1, image2],
    options: TextureResource.CreateOptions(semantic: .color))

// Assign the 2D array texture to a compatible shader graph material parameter.
var material = try await ShaderGraphMaterial(
    named: "/Root/Spaceship/MaterialWith2DArray", from: url)

try material.setParameter(
    name: "input2DArray", value: .textureResource(texture2DArray))
```

## Parameters

- `slices`: The source images, one per 2D array index. All images need to have the same size and format.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.

## See Also

- [static func texture2DArray(slices: [CGImage], named: String?, options: TextureResource.CreateOptions) async throws -> TextureResource](textureresource/texture2darray(slices:named:options:)-50g10.md)
  Asynchronously creates a 2D texture array by generating it from images.
- [convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) async throws](textureresource/init(dimensions:format:contents:)-324ls.md)
  Asynchronously creates a 2D array texture resource from a pixel Metal buffer, or data.
- [convenience init(dimensions: TextureResource.Dimensions2DArray, format: TextureResource.Format, contents: TextureResource.Contents) throws](textureresource/init(dimensions:format:contents:)-7p7hr.md)
  Synchronously creates a 2D array texture resource from a pixel Metal buffer, or data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/texture2darray(slices:named:options:)-8m54f)*
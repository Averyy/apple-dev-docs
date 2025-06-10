# texture2DArray(slices:named:options:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously creates a 2D texture array by generating it from images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func texture2DArray(slices: [CGImage], named resourceName: String? = nil, options: TextureResource.CreateOptions) async throws -> TextureResource
```

#### Discussion

RealityKit creates a [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray) texture with `arrayLength == slices.count` from an array of images.

You can assign the resulting texture to a material you create in Reality Composer Pro that requires a 2D texture array.

```swift
// Create a 2D array texture from image slices.
let texture2DArray = try TextureResource.texture2DArray(
    slices: [image0, image1, image2],
    options: TextureResource.CreateOptions(semantic: .color))

Task {
    // Assign the 2D array texture to a compatible shader graph material parameter.
    var material = try await ShaderGraphMaterial(
        named: "/Root/Spaceship/MaterialWith2DArray", from: url)

    try material.setParameter(
        name: "input2DArray", value: .textureResource(texture2DArray))
}
```

## Parameters

- `slices`: The source images, one per 2D array index. All images need to have the same size and format.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/texture2darray(slices:named:options:))*
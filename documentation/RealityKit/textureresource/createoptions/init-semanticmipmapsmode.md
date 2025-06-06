# init(semantic:mipmapsMode:)

**Framework**: RealityKit  
**Kind**: init

Creates a texture creation options structure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
init(semantic: TextureResource.Semantic?, mipmapsMode: TextureResource.MipmapsMode = .allocateAndGenerateAll)
```

#### Discussion

The `semantic` value you pass tells RealityKit how you plan to use the texture data from this resource. For example, passing [`TextureResource.Semantic.color`](textureresource/semantic-swift.enum/color.md) lets RealityKit know you’re using the texture to pass perceptual color information to the shaders, such as for providing a UV-mapped base color for physically based rendering materials. Passing [`TextureResource.Semantic.raw`](textureresource/semantic-swift.enum/raw.md) tells RealityKit to pass the pixel values with as little processing as possible.

If semantic is `nil`, RealityKit tries to infer a semantic from the texture’s source data. If it’s unable to determine a semantic from the texture source data, it will infer a semantic from the texture’s usage. Providing a value for `semantic` ensures that RealityKit passes the texture resource exactly as you intend.

> **Note**: RealityKit only takes embedded color space data into account when rendering a texture if you pass [`TextureResource.Semantic.color`](textureresource/semantic-swift.enum/color.md) for `semantic`.

RealityKit only takes embedded color space data into account when rendering a texture if you pass [`TextureResource.Semantic.color`](textureresource/semantic-swift.enum/color.md) for `semantic`.

## Parameters

- `semantic`: The intended use of the texture resource.
- `mipmapsMode`: Whether to automatically allocate or generate mipmaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/createoptions/init(semantic:mipmapsmode:))*
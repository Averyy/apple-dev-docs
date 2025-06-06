# init(texture:)

**Framework**: RealityKit  
**Kind**: init

Create an object from a specified texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(texture: CustomMaterial.Texture? = nil)
```

#### Discussion

This initializer creates an object from a normal map texture.  is a real-time rendering technique that captures fine surface details for a model using a texture instead of increasing the number of polygons in the model. It works by storing , which are vectors perpendicular to the surface of the model, from a much higher-resolution version of the same 3D object. A normal map stores each vector in the image by storing the vectors’ `X`, `Y`, and `Z` values as the `R`, `G`, and `B` components of the corresponding pixel in the UV-mapped image.

To render an entity using a normal map, set [`lightingModel`](custommaterial/lightingmodel-swift.property.md) to [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md), and call `params.surface().set_normal()` from its surface shader.

The following Metal code demonstrates how to sample and use a value from the normal map in your surface shader function:

```swift
    // Retrieve the entity's UV texture coordinates.
    float2 uv = params.geometry().uv0();

    // Models loaded from USDZ or Reality Composer use UVs that are flipped
    // on the y-axis. This compensates for that.
    uv.y = 1.0 - uv.y;

    // Sample the normal map texture based on the resulting UV coordinates.
    auto tex = params.textures();
    float3 normal = (float3)tex.normal().sample(textureSampler, uv).rgb;

    // Set the sampled value as this pixel's normal.
    params.surface().set_normal(normal);
```

## Parameters

- `texture`: The image’s texture.

## See Also

- [init(PhysicallyBasedMaterial.Normal)](custommaterial/normal-swift.struct/init(_:).md)
  Creates an object containing surface details for an entity from a custom material’s normal property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/normal-swift.struct/init(texture:))*
# init(surfaceShader:geometryModifier:lightingModel:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a custom material from a lighting model, surface shader, and geometry modifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier? = nil, lightingModel: CustomMaterial.LightingModel) throws
```

## Mentions

- [Modifying RealityKit rendering using custom materials](../modifying-realitykit-rendering-using-custom-materials.md)

#### Discussion

This initializer creates a custom material using a lighting model you specify, which determines how RealityKit renders the output of your shader functions. The [`CustomMaterial.LightingModel.lit`](./lightingmodel-swift.enum/lit.md) and [`CustomMaterial.LightingModel.clearcoat`](./lightingmodel-swift.enum/clearcoat.md) use RealityKit’s physically-based shaders to render the entity based on the output of your shader functions. When using these lighting models, RealityKit uses all provided material attributes like [`baseColor`](./basecolor-swift.property.md), [`metallic`](./metallic-swift.property.md) and [`normal`](./normal-swift.property.md).

The [`CustomMaterial.LightingModel.unlit`](./lightingmodel-swift.enum/unlit.md) lighting model renders the entity with no shadows or surface effects. This lighting model only supports [`baseColor`](./basecolor-swift.property.md) and [`blending`](./blending-swift.property.md).

## Parameters

- `surfaceShader`: The surface shader function.
- `geometryModifier`: The geometry modifier shader function.
- `lightingModel`: The lighting model.

## See Also

### Creating custom materials
- [init(from: any Material, geometryModifier: CustomMaterial.GeometryModifier) throws](./init%28from,geometrymodifier%29.md)
  Creates a custom material from an existing material and a geometry modifier.
- [init(from: any Material, surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier?) throws](./init%28from,surfaceshader,geometrymodifier%29.md)
  Creates a custom material from an existing material, surface shader, and geometry modifier.
- [init(program: CustomMaterial.Program)](./init%28program%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/init(surfaceshader:geometrymodifier:lightingmodel:))*
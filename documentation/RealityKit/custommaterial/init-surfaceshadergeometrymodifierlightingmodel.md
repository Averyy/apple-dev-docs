# init(surfaceShader:geometryModifier:lightingModel:)

**Framework**: RealityKit  
**Kind**: init

Creates a custom material from a lighting model, surface shader, and geometry modifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier? = nil, lightingModel: CustomMaterial.LightingModel) throws
```

## Mentions

- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)

#### Discussion

This initializer creates a custom material using a lighting model you specify, which determines how RealityKit renders the output of your shader functions. The [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) and [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) use RealityKit’s physically-based shaders to render the entity based on the output of your shader functions. When using these lighting models, RealityKit uses all provided material attributes like [`baseColor`](custommaterial/basecolor-swift.property.md), [`metallic`](custommaterial/metallic-swift.property.md) and [`normal`](custommaterial/normal-swift.property.md).

The [`CustomMaterial.LightingModel.unlit`](custommaterial/lightingmodel-swift.enum/unlit.md) lighting model renders the entity with no shadows or surface effects. This lighting model only supports [`baseColor`](custommaterial/basecolor-swift.property.md) and [`blending`](custommaterial/blending-swift.property.md).

## Parameters

- `surfaceShader`: The surface shader function.
- `geometryModifier`: The geometry modifier shader function.
- `lightingModel`: The lighting model.

## See Also

- [init(from: any Material, geometryModifier: CustomMaterial.GeometryModifier) throws](custommaterial/init(from:geometrymodifier:).md)
  Creates a custom material from an existing material and a geometry modifier.
- [init(from: any Material, surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier?) throws](custommaterial/init(from:surfaceshader:geometrymodifier:).md)
  Creates a custom material from an existing material, surface shader, and geometry modifier.
- [init(program: CustomMaterial.Program)](custommaterial/init(program:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/init(surfaceshader:geometrymodifier:lightingmodel:))*
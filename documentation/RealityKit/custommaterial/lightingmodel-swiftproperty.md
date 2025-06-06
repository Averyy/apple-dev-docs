# lightingModel

**Framework**: RealityKit  
**Kind**: property

The lighting model that the material uses.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var lightingModel: CustomMaterial.LightingModel { get }
```

## Mentions

- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)

#### Discussion

A custom material’s lighting model determines exactly how RealityKit uses the values set in your surface shader’s to render the entity.

Custom materials supports the following lighting models:

| Lighting Model | Description | Supported Shader Outputs |
| --- | --- | --- |
| `.lit` | Uses physically based rendering techniques, but excludes clearcoat. | All except `set_clearcoat()` and `set_clearcoat_roughness()` |
| `.clearcoat` | Uses physically based rendering techniques, including clearcoat. | All |
| `.unlit` | Renders without any shading or lighting calculations. The result is similar to using an [`UnlitMaterial`](unlitmaterial.md). | Uses `set_emissive_color()` only |

## See Also

- [var program: CustomMaterial.Program](custommaterial/program-swift.property.md)
- [var custom: CustomMaterial.Custom](custommaterial/custom-swift.property.md)
  User-defined properties for the material’s shader functions.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader and geometry modifier.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, stage: CustomShaderStage, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:stage:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader or geometry modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/lightingmodel-swift.property)*
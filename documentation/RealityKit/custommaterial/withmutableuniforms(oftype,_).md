# withMutableUniforms(ofType:_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader and geometry modifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
mutating func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, _ callback: (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)
```

#### Discussion

This method operates like [`withMutableUniforms(ofType:stage:_:)`](./withmutableuniforms%28oftype,stage,_%29.md) but sets the same value for all stages at once.

When using this form, ensure that the custom uniforms arguments passed to each stage of your CustomMaterial are of the same type.

## See Also

### Setting shader properties
- [var program: CustomMaterial.Program](./program-swift.property.md)
- [var custom: CustomMaterial.Custom](./custom-swift.property.md)
  User-defined properties for the material’s shader functions.
- [var lightingModel: CustomMaterial.LightingModel](./lightingmodel-swift.property.md)
  The lighting model that the material uses.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, stage: CustomShaderStage, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](./withmutableuniforms%28oftype,stage,_%29.md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader or geometry modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/withmutableuniforms(oftype:_:))*
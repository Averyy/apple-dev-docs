# withMutableUniforms(ofType:_:)

**Framework**: RealityKit  
**Kind**: method

Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader and geometry modifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
mutating func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, _ callback: (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)
```

#### Discussion

This method operates like [`withMutableUniforms(ofType:stage:_:)`](custommaterial/withmutableuniforms(oftype:stage:_:).md) but sets the same value for all stages at once.

When using this form, ensure that the custom uniforms arguments passed to each stage of your CustomMaterial are of the same type.

## See Also

- [var program: CustomMaterial.Program](custommaterial/program-swift.property.md)
- [var custom: CustomMaterial.Custom](custommaterial/custom-swift.property.md)
  User-defined properties for the material’s shader functions.
- [var lightingModel: CustomMaterial.LightingModel](custommaterial/lightingmodel-swift.property.md)
  The lighting model that the material uses.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, stage: CustomShaderStage, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:stage:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader or geometry modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/withmutableuniforms(oftype:_:))*
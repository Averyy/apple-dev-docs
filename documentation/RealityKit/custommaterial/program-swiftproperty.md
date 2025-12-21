# program

**Framework**: RealityKit  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
var program: CustomMaterial.Program { get set }
```

## See Also

- [var custom: CustomMaterial.Custom](custommaterial/custom-swift.property.md)
  User-defined properties for the material’s shader functions.
- [var lightingModel: CustomMaterial.LightingModel](custommaterial/lightingmodel-swift.property.md)
  The lighting model that the material uses.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader and geometry modifier.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, stage: CustomShaderStage, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:stage:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader or geometry modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/program-swift.property)*
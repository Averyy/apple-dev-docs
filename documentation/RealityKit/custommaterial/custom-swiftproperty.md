# custom

**Framework**: Realitykit  
**Kind**: property

User-defined properties for the material’s shader functions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var custom: CustomMaterial.Custom { get set }
```

#### Discussion

Use a [`CustomMaterial.Custom`](custommaterial/custom-swift.struct.md) object to send custom data to your shader functions. A custom object can hold a texture or a vector value, or both. Both the texture and vector value are available in your shader functions.

> **Note**: Unlike other [`CustomMaterial`](custommaterial.md) properties, you don’t need to create a [`CustomMaterial.Custom`](custommaterial/custom-swift.struct.md) object for your material. All [`CustomMaterial`](custommaterial.md) objects have one by default; you just need to set the [`value`](custommaterial/custom-swift.struct/value.md) property, [`texture`](custommaterial/custom-swift.struct/texture.md) property, or both.

The following code demonstrates how to use the custom property to pass a vector to your shader functions:

```swift
// Specify a custom vector to pass to the shader functions.
customMaterial.custom.value = [0.25, 0.25, 0.25, 1.0]
```

You can also use it to pass up to four scalar values instead of a vector:

```swift
let customValue1: Float = 0.25
let customValue2: Float = 0.75
customMaterial.custom.value[0] = customValue1
customMaterial.custom.value[1] = customValue2
```

The custom property can also include a texture. The following code demonstrates how to add a texture to the custom property:

```swift
if let theResource = try? TextureResource.load(named: "MyCustomTexture") {
    let myTexture = CustomMaterial.Texture(theResource)
    customMaterial.custom.texture = .init(myTexture)
}
```

The following Metal code shows how to retrieve the custom vector in a shader function:

```cpp
float4 myCustomVector = params.uniforms().custom_parameter();
```

The following Metal code shows how to retrieve individual values from the custom vector in your shader functions:

```cpp
float firstCustomValue = params.uniforms().custom_parameter()[0];
float secondCustomValue = params.uniforms().custom_parameter()[1];
```

Here’s how to retrieve the custom texture in your shader functions:

```cpp
float voronoiColor = params.textures()
    .custom().sample(textureSampler, UV).r;
```

## See Also

- [var program: CustomMaterial.Program](custommaterial/program-swift.property.md)
- [var lightingModel: CustomMaterial.LightingModel](custommaterial/lightingmodel-swift.property.md)
  The lighting model that the material uses.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader and geometry modifier.
- [func withMutableUniforms<UniformsType>(ofType: UniformsType.Type, stage: CustomShaderStage, (inout UniformsType, inout CustomMaterial.ResourceStorage<UniformsType>) -> Void)](custommaterial/withmutableuniforms(oftype:stage:_:).md)
  Calls the given closure with an inout reference to the underlying storage bound to the custom uniforms argument of a surface shader or geometry modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/custom-swift.property)*
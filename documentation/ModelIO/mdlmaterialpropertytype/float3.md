# MDLMaterialPropertyType.float3

**Framework**: Model I/O  
**Kind**: case

The material property’s value is a 3-component floating-point vector.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case float3
```

#### Discussion

Use the [`float3Value`](mdlmaterialproperty/float3value.md) property to access the material property’s value.

## See Also

- [MDLMaterialPropertyType.none](mdlmaterialpropertytype/none.md)
  The material property’s value has not been initialized.
- [MDLMaterialPropertyType.string](mdlmaterialpropertytype/string.md)
  The material’s value is a string.
- [MDLMaterialPropertyType.URL](mdlmaterialpropertytype/url.md)
  The material property’s value is a URL—typically, a URL referencing a texture image.
- [MDLMaterialPropertyType.texture](mdlmaterialpropertytype/texture.md)
  The material property’s value is a [`MDLTextureSampler`](mdltexturesampler.md) object that provides both a texture image and texture rendering parameters.
- [MDLMaterialPropertyType.color](mdlmaterialpropertytype/color.md)
  The material property’s value is a uniform color.
- [MDLMaterialPropertyType.float](mdlmaterialpropertytype/float.md)
  The material property’s value is a floating-point scalar.
- [MDLMaterialPropertyType.float2](mdlmaterialpropertytype/float2.md)
  The material property’s value is a 2-component floating-point vector.
- [MDLMaterialPropertyType.float4](mdlmaterialpropertytype/float4.md)
  The material property’s value is a 4-component floating-point vector.
- [MDLMaterialPropertyType.matrix44](mdlmaterialpropertytype/matrix44.md)
  The material property’s value is a 4 x 4 floating-point matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/float3)*
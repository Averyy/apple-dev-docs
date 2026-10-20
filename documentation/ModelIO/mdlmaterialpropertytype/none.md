# MDLMaterialPropertyType.none

**Framework**: Model I/O  
**Kind**: case  
**Role**: Case

The material property’s value has not been initialized.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

```c
MDLMaterialPropertyTypeNone
```

#### Discussion

Set one of the properties listed in Working with a Material Property’s Value to provide a value for the material property. After setting a value, the [`type`](../mdlmaterialproperty/type.md) property reflects the data type of that value.

## See Also

### Constants
- [MDLMaterialPropertyType.string](./string.md)
  The material’s value is a string.
- [MDLMaterialPropertyType.URL](./url.md)
  The material property’s value is a URL—typically, a URL referencing a texture image.
- [MDLMaterialPropertyType.texture](./texture.md)
  The material property’s value is a [`MDLTextureSampler`](../mdltexturesampler.md) object that provides both a texture image and texture rendering parameters.
- [MDLMaterialPropertyType.color](./color.md)
  The material property’s value is a uniform color.
- [MDLMaterialPropertyType.float](./float.md)
  The material property’s value is a floating-point scalar.
- [MDLMaterialPropertyType.float2](./float2.md)
  The material property’s value is a 2-component floating-point vector.
- [MDLMaterialPropertyType.float3](./float3.md)
  The material property’s value is a 3-component floating-point vector.
- [MDLMaterialPropertyType.float4](./float4.md)
  The material property’s value is a 4-component floating-point vector.
- [MDLMaterialPropertyType.matrix44](./matrix44.md)
  The material property’s value is a 4 x 4 floating-point matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialpropertytype/none)*
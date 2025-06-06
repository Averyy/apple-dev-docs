# stringValue

**Framework**: Model I/O  
**Kind**: property

The string value for the material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var stringValue: String? { get set }
```

#### Discussion

The meaning of a string value depends on the renderer (or other software component) processing the material. For example, a string value might be treated as the name of a texture image to be loaded from a default path.

## See Also

- [var urlValue: URL?](mdlmaterialproperty/urlvalue.md)
  The URL value for the material property—typically, the URL to a texture image.
- [var textureSamplerValue: MDLTextureSampler?](mdlmaterialproperty/texturesamplervalue.md)
  A texture sampler object that provides the texture image value for the material property.
- [var color: CGColor?](mdlmaterialproperty/color.md)
  The color value for the material property.
- [var floatValue: Float](mdlmaterialproperty/floatvalue.md)
  The scalar floating-point value for the material property.
- [var float2Value: vector_float2](mdlmaterialproperty/float2value.md)
  The 2-component floating-point vector value for the material property.
- [var float3Value: vector_float3](mdlmaterialproperty/float3value.md)
  The 3-component floating-point vector value for the material property.
- [var float4Value: vector_float4](mdlmaterialproperty/float4value.md)
  The 4-component floating-point vector value for the material property.
- [var matrix4x4: matrix_float4x4](mdlmaterialproperty/matrix4x4.md)
  The 4 x 4 floating-point matrix value for the material property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/stringvalue)*
# textureSamplerValue

**Framework**: Model I/O  
**Kind**: property

A texture sampler object that provides the texture image value for the material property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var textureSamplerValue: MDLTextureSampler? { get set }
```

#### Discussion

Unlike the URL to a texture image, a texture sampler object specifies both a texture image and parameters for rendering that image.

## See Also

- [var stringValue: String?](mdlmaterialproperty/stringvalue.md)
  The string value for the material.
- [var urlValue: URL?](mdlmaterialproperty/urlvalue.md)
  The URL value for the material property—typically, the URL to a texture image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/texturesamplervalue)*
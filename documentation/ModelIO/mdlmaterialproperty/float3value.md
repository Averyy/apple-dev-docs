# float3Value

**Framework**: Model I/O  
**Kind**: property

The 3-component floating-point vector value for the material property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var float3Value: vector_float3 { get set }
```

#### Discussion

A 3-component vector can also be used to store RGB3 color values. In this case, color components should be interpreted using the Rec. 709 color space standard.

## See Also

- [var stringValue: String?](mdlmaterialproperty/stringvalue.md)
  The string value for the material.
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
- [var float4Value: vector_float4](mdlmaterialproperty/float4value.md)
  The 4-component floating-point vector value for the material property.
- [var matrix4x4: matrix_float4x4](mdlmaterialproperty/matrix4x4.md)
  The 4 x 4 floating-point matrix value for the material property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/float3value)*
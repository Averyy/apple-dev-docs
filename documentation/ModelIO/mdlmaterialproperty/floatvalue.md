# floatValue

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The scalar floating-point value for the material property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var floatValue: Float { get set }
```

```objc
@property (nonatomic, assign) float floatValue;
```

## Discussion

Scalar values are appropriate for some semantics, such as the [`MDLMaterialSemantic.specularTint`](../mdlmaterialsemantic/speculartint.md) semantic (which controls the balance between material and light colors in specular highlighting). Providing a float value for the material property applies that value for all pixels rendered using the material; to provide variation in the semantic’s value across a surface, use a grayscale texture image instead.

## See Also

### Working with a Material Property’s Value
- [var stringValue: String?](./stringvalue.md)
  The string value for the material.
- [var urlValue: URL?](./urlvalue.md)
  The URL value for the material property—typically, the URL to a texture image.
- [var textureSamplerValue: MDLTextureSampler?](./texturesamplervalue.md)
  A texture sampler object that provides the texture image value for the material property.
- [var color: CGColor?](./color.md)
  The color value for the material property.
- [var float2Value: vector_float2](./float2value.md)
  The 2-component floating-point vector value for the material property.
- [var float3Value: vector_float3](./float3value.md)
  The 3-component floating-point vector value for the material property.
- [var float4Value: vector_float4](./float4value.md)
  The 4-component floating-point vector value for the material property.
- [var matrix4x4: matrix_float4x4](./matrix4x4.md)
  The 4 x 4 floating-point matrix value for the material property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/floatvalue)*
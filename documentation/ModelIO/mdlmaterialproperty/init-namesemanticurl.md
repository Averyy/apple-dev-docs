# init(name:semantic:url:)

**Framework**: Model I/O  
**Kind**: init

Initializes a material property with a URL value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, semantic: MDLMaterialSemantic, url URL: URL?)
```

#### Return Value

A new material property object whose [`type`](mdlmaterialproperty/type.md) property is [`MDLMaterialPropertyType.URL`](mdlmaterialpropertytype/url.md).

#### Discussion

A renderer (or other software component processing a material) is responsible for loading a texture image from the specified URL.

## Parameters

- `name`: A descriptive name for the material property. For details, see the   property.
- `semantic`: The semantic meaning for the material property’s value. For details, see the   property.
- `URL`: The URL value for the material property—typically, the URL to a texture image.

## See Also

- [init(name: String, semantic: MDLMaterialSemantic)](mdlmaterialproperty/init(name:semantic:).md)
  Initializes a material property without a value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, string: String?)](mdlmaterialproperty/init(name:semantic:string:).md)
  Initializes a material property with a string value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, textureSampler: MDLTextureSampler?)](mdlmaterialproperty/init(name:semantic:texturesampler:).md)
  Initializes a material property with a texture sampler object.
- [convenience init(name: String, semantic: MDLMaterialSemantic, color: CGColor)](mdlmaterialproperty/init(name:semantic:color:).md)
  Initializes a material property with a color value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float: Float)](mdlmaterialproperty/init(name:semantic:float:).md)
  Initializes a material property with a scalar value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float2: vector_float2)](mdlmaterialproperty/init(name:semantic:float2:).md)
  Initializes a material property with a 2-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float3: vector_float3)](mdlmaterialproperty/init(name:semantic:float3:).md)
  Initializes a material property with a 3-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float4: vector_float4)](mdlmaterialproperty/init(name:semantic:float4:).md)
  Initializes a material property with a 4-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, matrix4x4: matrix_float4x4)](mdlmaterialproperty/init(name:semantic:matrix4x4:).md)
  Initializes a material property with a 4 x 4 matrix value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/init(name:semantic:url:))*
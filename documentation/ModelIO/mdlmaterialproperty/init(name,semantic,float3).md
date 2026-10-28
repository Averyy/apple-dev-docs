# init(name:semantic:float3:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

Initializes a material property with a 3-component vector value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, semantic: MDLMaterialSemantic, float3 value: vector_float3)
```

```objc
- (instancetype) initWithName:(NSString *) name semantic:(MDLMaterialSemantic) semantic float3:(vector_float3) value;
```

## Return Value

A new material property object whose [`type`](./type.md) property is [`MDLMaterialPropertyType.float3`](../mdlmaterialpropertytype/float3.md).

## Discussion

A 3-component vector can also be used to store RGB color values. In this case, color components should be interpreted using the Rec. 709 color space standard.

## Parameters

- `name`: A descriptive name for the material property. For details, see the [`name`](./name.md) property.
- `semantic`: The semantic meaning for the material property’s value. For details, see the [`semantic`](./semantic.md) property.
- `value`: The 3-component floating-point vector value for the material property.

## See Also

### Creating a Material Property
- [init(name: String, semantic: MDLMaterialSemantic)](./init%28name,semantic%29.md)
  Initializes a material property without a value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, string: String?)](./init%28name,semantic,string%29.md)
  Initializes a material property with a string value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, url: URL?)](./init%28name,semantic,url%29-2ldk4.md)
  Initializes a material property with a URL value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, textureSampler: MDLTextureSampler?)](./init%28name,semantic,texturesampler%29.md)
  Initializes a material property with a texture sampler object.
- [convenience init(name: String, semantic: MDLMaterialSemantic, color: CGColor)](./init%28name,semantic,color%29.md)
  Initializes a material property with a color value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float: Float)](./init%28name,semantic,float%29.md)
  Initializes a material property with a scalar value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float2: vector_float2)](./init%28name,semantic,float2%29.md)
  Initializes a material property with a 2-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float4: vector_float4)](./init%28name,semantic,float4%29.md)
  Initializes a material property with a 4-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, matrix4x4: matrix_float4x4)](./init%28name,semantic,matrix4x4%29.md)
  Initializes a material property with a 4 x 4 matrix value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/init(name:semantic:float3:))*
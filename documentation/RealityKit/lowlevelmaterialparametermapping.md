# LowLevelMaterialParameterMapping

**Framework**: RealityKit  
**Kind**: struct

A mapping of named buffer and texture parameters to binding indices for a compiled shader function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LowLevelMaterialParameterMapping
```

#### Overview

Use `bufferLocation(named:)`, `constantLocation(named:)`, and `textureLocation(named:)` to look up the binding index for a named parameter, then bind a resource to that slot with [`setBufferSlice(_:at:)`](lowlevelargumenttable/setbufferslice(_:at:).md) or [`setTexture(_:at:)`](lowlevelargumenttable/settexture(_:at:).md).

## Topics

### Accessing parameter mappings
- [var buffers: [LowLevelMaterialParameterMapping.Buffer]](lowlevelmaterialparametermapping/buffers.md)
  The ordered buffer slot descriptions for this function.
- [LowLevelMaterialParameterMapping.Buffer](lowlevelmaterialparametermapping/buffer.md)
  The contents of a buffer slot, either a collection of packed constants or a single structured buffer.
- [LowLevelMaterialParameterMapping.BufferParameter](lowlevelmaterialparametermapping/bufferparameter.md)
  A structured buffer parameter.
- [var textures: [LowLevelMaterialParameterMapping.TextureParameter]](lowlevelmaterialparametermapping/textures.md)
  The ordered texture slot descriptions for this function.
- [LowLevelMaterialParameterMapping.TextureParameter](lowlevelmaterialparametermapping/textureparameter.md)
  A texture parameter.
- [LowLevelMaterialParameterMapping.ConstantParameter](lowlevelmaterialparametermapping/constantparameter.md)
  A constant parameter embedded within a buffer slot.
### Locating parameters
- [func bufferLocation(named: String) -> Int?](lowlevelmaterialparametermapping/bufferlocation(named:).md)
  Returns the argument table buffer slot index for the named buffer parameter, or `nil` if no parameter with that name exists.
- [func textureLocation(named: String) -> Int?](lowlevelmaterialparametermapping/texturelocation(named:).md)
  Returns the argument table texture slot index for the named texture parameter, or `nil` if no parameter with that name exists.
- [func constantLocation(named: String) -> LowLevelMaterialParameterMapping.ConstantLocation?](lowlevelmaterialparametermapping/constantlocation(named:).md)
  Returns the resolved buffer and constant indices for the named constant parameter, or `nil` if no parameter with that name exists.
- [LowLevelMaterialParameterMapping.ConstantLocation](lowlevelmaterialparametermapping/constantlocation.md)
  The resolved buffer and constant slot indices for a named constant parameter.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class LowLevelRenderPipelineState](lowlevelrenderpipelinestate.md)
  A compiled Metal render pipeline state for a specific mesh descriptor, material, and render target configuration.
- [class LowLevelRenderTarget](lowlevelrendertarget.md)
  An object that describes the pixel format configuration for a render pass’s color and depth attachments.
- [class LowLevelArgumentTable](lowlevelargumenttable.md)
  A table of buffer slices and textures bound to a single shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialparametermapping)*
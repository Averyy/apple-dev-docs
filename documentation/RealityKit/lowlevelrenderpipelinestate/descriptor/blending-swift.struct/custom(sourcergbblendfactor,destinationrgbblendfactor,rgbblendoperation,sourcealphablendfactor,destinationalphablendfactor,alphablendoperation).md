# custom(sourceRGBBlendFactor:destinationRGBBlendFactor:rgbBlendOperation:sourceAlphaBlendFactor:destinationAlphaBlendFactor:alphaBlendOperation:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a custom blending configuration with explicit Metal blend factors and operations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func custom(sourceRGBBlendFactor: MTLBlendFactor = .one, destinationRGBBlendFactor: MTLBlendFactor = .zero, rgbBlendOperation: MTLBlendOperation = .add, sourceAlphaBlendFactor: MTLBlendFactor = .one, destinationAlphaBlendFactor: MTLBlendFactor = .zero, alphaBlendOperation: MTLBlendOperation = .add) -> LowLevelRenderPipelineState.Descriptor.Blending
```

## Return Value

A [`LowLevelRenderPipelineState.Descriptor.Blending`](../blending-swift.struct.md) with the specified configuration.

## Parameters

- `sourceRGBBlendFactor`: The blend factor applied to the source RGB values.
- `destinationRGBBlendFactor`: The blend factor applied to the destination RGB values.
- `rgbBlendOperation`: The blend operation used to combine source and destination RGB values.
- `sourceAlphaBlendFactor`: The blend factor applied to the source alpha value.
- `destinationAlphaBlendFactor`: The blend factor applied to the destination alpha value.
- `alphaBlendOperation`: The blend operation used to combine source and destination alpha values.

## See Also

### Creating a blending mode
- [static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending](./sourceover.md)
  Standard source-over alpha blending with pre-multiplied alpha.
- [static var add: LowLevelRenderPipelineState.Descriptor.Blending](./add.md)
  Additive blending that combines source and destination colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct/custom(sourcergbblendfactor:destinationrgbblendfactor:rgbblendoperation:sourcealphablendfactor:destinationalphablendfactor:alphablendoperation:))*
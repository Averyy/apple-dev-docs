# custom(sourceRGBBlendFactor:destinationRGBBlendFactor:sourceAlphaBlendFactor:destinationAlphaBlendFactor:alphaBlendOperation:)

**Framework**: RealityKit  
**Kind**: method

Creates a custom blending configuration with explicit Metal blend factors and operations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func custom(sourceRGBBlendFactor: MTLBlendFactor = .one, destinationRGBBlendFactor: MTLBlendFactor = .zero, sourceAlphaBlendFactor: MTLBlendFactor = .one, destinationAlphaBlendFactor: MTLBlendFactor = .zero, alphaBlendOperation: MTLBlendOperation = .add) -> LowLevelRenderPipelineState.Descriptor.Blending
```

#### Return Value

A [`LowLevelRenderPipelineState.Descriptor.Blending`](lowlevelrenderpipelinestate/descriptor/blending-swift.struct.md) with the specified configuration.

## Parameters

- `sourceRGBBlendFactor`: The blend factor applied to the source RGB values.
- `destinationRGBBlendFactor`: The blend factor applied to the destination RGB values.
- `sourceAlphaBlendFactor`: The blend factor applied to the source alpha value.
- `destinationAlphaBlendFactor`: The blend factor applied to the destination alpha value.
- `alphaBlendOperation`: The blend operation used to combine source and destination alpha values.

## See Also

- [static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/sourceover.md)
  Standard source-over alpha blending with pre-multiplied alpha.
- [static var add: LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/add.md)
  Additive blending that combines source and destination colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct/custom(sourcergbblendfactor:destinationrgbblendfactor:sourcealphablendfactor:destinationalphablendfactor:alphablendoperation:))*
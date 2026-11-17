# add

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

Additive blending that combines source and destination colors.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var add: LowLevelRenderPipelineState.Descriptor.Blending { get }
```

## See Also

### Creating a blending mode
- [static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending](./sourceover.md)
  Standard source-over alpha blending with pre-multiplied alpha.
- [static func custom(sourceRGBBlendFactor: MTLBlendFactor, destinationRGBBlendFactor: MTLBlendFactor, rgbBlendOperation: MTLBlendOperation, sourceAlphaBlendFactor: MTLBlendFactor, destinationAlphaBlendFactor: MTLBlendFactor, alphaBlendOperation: MTLBlendOperation) -> LowLevelRenderPipelineState.Descriptor.Blending](./custom%28sourcergbblendfactor,destinationrgbblendfactor,rgbblendoperation,sourcealphablendfactor,destinationalphablendfactor,alphablendoperation%29.md)
  Creates a custom blending configuration with explicit Metal blend factors and operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct/add)*
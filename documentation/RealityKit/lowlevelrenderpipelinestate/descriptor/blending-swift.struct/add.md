# add

**Framework**: RealityKit  
**Kind**: property

Additive blending that combines source and destination colors.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var add: LowLevelRenderPipelineState.Descriptor.Blending { get }
```

## See Also

- [static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/sourceover.md)
  Standard source-over alpha blending with pre-multiplied alpha.
- [static func custom(sourceRGBBlendFactor: MTLBlendFactor, destinationRGBBlendFactor: MTLBlendFactor, sourceAlphaBlendFactor: MTLBlendFactor, destinationAlphaBlendFactor: MTLBlendFactor, alphaBlendOperation: MTLBlendOperation) -> LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/custom(sourcergbblendfactor:destinationrgbblendfactor:sourcealphablendfactor:destinationalphablendfactor:alphablendoperation:).md)
  Creates a custom blending configuration with explicit Metal blend factors and operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct/add)*
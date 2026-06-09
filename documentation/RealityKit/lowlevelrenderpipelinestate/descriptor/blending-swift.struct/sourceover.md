# sourceOver

**Framework**: RealityKit  
**Kind**: property

Standard source-over alpha blending with pre-multiplied alpha.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending { get }
```

## See Also

- [static var add: LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/add.md)
  Additive blending that combines source and destination colors.
- [static func custom(sourceRGBBlendFactor: MTLBlendFactor, destinationRGBBlendFactor: MTLBlendFactor, sourceAlphaBlendFactor: MTLBlendFactor, destinationAlphaBlendFactor: MTLBlendFactor, alphaBlendOperation: MTLBlendOperation) -> LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/custom(sourcergbblendfactor:destinationrgbblendfactor:sourcealphablendfactor:destinationalphablendfactor:alphablendoperation:).md)
  Creates a custom blending configuration with explicit Metal blend factors and operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct/sourceover)*
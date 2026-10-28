# LowLevelRenderTarget.DescriptorSet

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An unordered set of render target descriptors that defines the output format combination a pipeline state or mesh instance array is compatible with.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct DescriptorSet
```

## Overview

`DescriptorSet` conforms to `ExpressibleByArrayLiteral`, so you can initialize it directly with an array literal of [`LowLevelRenderTarget.Descriptor`](./descriptor.md) values.

## Topics

### Creating a descriptor set
- [init(arrayLiteral: LowLevelRenderTarget.Descriptor...)](./descriptorset/init%28arrayliteral%29.md)
  Creates a descriptor set from an array literal of render target descriptors.
### Initializers
- [init([LowLevelRenderTarget.Descriptor])](./descriptorset/init%28_%29.md)
  Creates a descriptor set from an array of render target descriptors.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing the render target
- [LowLevelRenderTarget.Descriptor](./descriptor.md)
  A color and depth pixel format combination for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendertarget/descriptorset)*
# LowLevelRenderTarget.DescriptorSet

**Framework**: RealityKit  
**Kind**: struct

An unordered set of render target descriptors that defines the output format combination a pipeline state or mesh instance array is compatible with.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DescriptorSet
```

#### Overview

`DescriptorSet` conforms to `ExpressibleByArrayLiteral`, so you can initialize it directly with an array literal of [`LowLevelRenderTarget.Descriptor`](lowlevelrendertarget/descriptor.md) values.

## Topics

### Creating a descriptor set
- [init(arrayLiteral: LowLevelRenderTarget.Descriptor...)](lowlevelrendertarget/descriptorset/init(arrayliteral:).md)
  Creates a descriptor set from an array literal of render target descriptors.
### Initializers
- [init([LowLevelRenderTarget.Descriptor])](lowlevelrendertarget/descriptorset/init(_:).md)
  Creates a descriptor set from an array of render target descriptors.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LowLevelRenderTarget.Descriptor](lowlevelrendertarget/descriptor.md)
  A color and depth pixel format combination for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendertarget/descriptorset)*
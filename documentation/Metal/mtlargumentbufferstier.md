# MTLArgumentBuffersTier

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The values that determine the limits and capabilities of argument buffers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLArgumentBuffersTier
```

```c
enum MTLArgumentBuffersTier : NSUInteger;
```

## Overview

See [Improving CPU performance by using argument buffers](./improving-cpu-performance-by-using-argument-buffers.md) for more information about argument buffer tiers, limits, and capabilities. Query the [`argumentBuffersSupport`](./mtldevice/argumentbufferssupport.md) property to determine argument buffer tier support for a given device.

## Topics

### Enumeration cases
- [MTLArgumentBuffersTier.tier1](./mtlargumentbufferstier/tier1.md)
  Support for tier 1 argument buffers.
- [MTLArgumentBuffersTier.tier2](./mtlargumentbufferstier/tier2.md)
  Support for tier 2 argument buffers.
### Initializers
- [init?(rawValue: UInt)](./mtlargumentbufferstier/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [MTLTensorError.Code](./mtltensorerror-swift.struct/code.md)
  The error codes that Metal can raise when you create a tensor.
- [enum MTLLogStateError](./mtllogstateerror.md)
- [enum MTLMathFloatingPointFunctions](./mtlmathfloatingpointfunctions.md)
  Indicates which FP32 math functions Metal uses.
- [enum MTLMathMode](./mtlmathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [enum MTLMatrixLayout](./mtlmatrixlayout.md)
- [enum MTLReadWriteTextureTier](./mtlreadwritetexturetier.md)
  The support level for read-write texture formats.
- [enum MTLShaderValidation](./mtlshadervalidation.md)
  Indicates whether shader validation in an enabled or disabled state, or neither state.
- [enum MTLTransformType](./mtltransformtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentbufferstier)*
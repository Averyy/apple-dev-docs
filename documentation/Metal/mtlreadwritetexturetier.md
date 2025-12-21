# MTLReadWriteTextureTier

**Framework**: Metal  
**Kind**: enum

The support level for read-write texture formats.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLReadWriteTextureTier
```

## Topics

### Enumeration cases
- [MTLReadWriteTextureTier.tier1](mtlreadwritetexturetier/tier1.md)
  Indicates the system supports tier 1 read-write textures.
- [MTLReadWriteTextureTier.tier2](mtlreadwritetexturetier/tier2.md)
  Indicates the system supports tier 2 read-write textures.
- [MTLReadWriteTextureTier.tierNone](mtlreadwritetexturetier/tiernone.md)
  Indicates the system doesn’t support read-write textures.
### Initializers
- [init?(rawValue: UInt)](mtlreadwritetexturetier/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MTLTensorError.Code](mtltensorerror-swift.struct/code.md)
  The error codes that Metal can raise when you create a tensor.
- [enum MTLArgumentBuffersTier](mtlargumentbufferstier.md)
  The values that determine the limits and capabilities of argument buffers.
- [enum MTLLogStateError](mtllogstateerror.md)
- [enum MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md)
  Indicates which FP32 math functions Metal uses.
- [enum MTLMathMode](mtlmathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [enum MTLMatrixLayout](mtlmatrixlayout.md)
- [enum MTLShaderValidation](mtlshadervalidation.md)
  Indicates whether shader validation in an enabled or disabled state, or neither state.
- [enum MTLTransformType](mtltransformtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlreadwritetexturetier)*
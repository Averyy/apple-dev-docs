# MTLMathFloatingPointFunctions

**Framework**: Metal  
**Kind**: enum

Indicates which FP32 math functions Metal uses.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MTLMathFloatingPointFunctions
```

## Topics

### Function sets
- [MTLMathFloatingPointFunctions.fast](mtlmathfloatingpointfunctions/fast.md)
  An indication that Metal uses the fast version of the 32b floating-point math functions.
- [MTLMathFloatingPointFunctions.precise](mtlmathfloatingpointfunctions/precise.md)
  An indication that Metal uses the precise version of the 32b floating-point math functions.
### Initializers
- [init?(rawValue: Int)](mtlmathfloatingpointfunctions/init(rawvalue:).md)

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
- [enum MTLMathMode](mtlmathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [enum MTLMatrixLayout](mtlmatrixlayout.md)
- [enum MTLReadWriteTextureTier](mtlreadwritetexturetier.md)
  The support level for read-write texture formats.
- [enum MTLShaderValidation](mtlshadervalidation.md)
  Indicates whether shader validation in an enabled or disabled state, or neither state.
- [enum MTLTransformType](mtltransformtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmathfloatingpointfunctions)*
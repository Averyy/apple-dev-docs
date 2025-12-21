# MTLTensorError.Code

**Framework**: Metal  
**Kind**: enum

The error codes that Metal can raise when you create a tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Code
```

## Topics

### Enumeration Cases
- [MTLTensorError.Code.internalError](mtltensorerror-swift.struct/code/internalerror.md)
- [MTLTensorError.Code.invalidDescriptor](mtltensorerror-swift.struct/code/invaliddescriptor.md)
- [MTLTensorError.Code.none](mtltensorerror-swift.struct/code/none.md)
### Initializers
- [init?(rawValue: Int)](mtltensorerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MTLArgumentBuffersTier](mtlargumentbufferstier.md)
  The values that determine the limits and capabilities of argument buffers.
- [enum MTLLogStateError](mtllogstateerror.md)
- [enum MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md)
  Indicates which FP32 math functions Metal uses.
- [enum MTLMathMode](mtlmathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [enum MTLMatrixLayout](mtlmatrixlayout.md)
- [enum MTLReadWriteTextureTier](mtlreadwritetexturetier.md)
  The support level for read-write texture formats.
- [enum MTLShaderValidation](mtlshadervalidation.md)
  Indicates whether shader validation in an enabled or disabled state, or neither state.
- [enum MTLTransformType](mtltransformtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorerror-swift.struct/code)*
# MTLShaderValidation

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Indicates whether shader validation in an enabled or disabled state, or neither state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum MTLShaderValidation
```

```c
enum MTLShaderValidation : NSInteger;
```

## Topics

### Validation states
- [MTLShaderValidation.default](./mtlshadervalidation/default.md)
  The default value when the property isn’t set.
- [MTLShaderValidation.disabled](./mtlshadervalidation/disabled.md)
  Disables shader validation.
- [MTLShaderValidation.enabled](./mtlshadervalidation/enabled.md)
  Enables shader validation.
### Initializers
- [init?(rawValue: Int)](./mtlshadervalidation/init%28rawvalue%29.md)

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
- [enum MTLArgumentBuffersTier](./mtlargumentbufferstier.md)
  The values that determine the limits and capabilities of argument buffers.
- [enum MTLLogStateError](./mtllogstateerror.md)
- [enum MTLMathFloatingPointFunctions](./mtlmathfloatingpointfunctions.md)
  Indicates which FP32 math functions Metal uses.
- [enum MTLMathMode](./mtlmathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [enum MTLMatrixLayout](./mtlmatrixlayout.md)
- [enum MTLReadWriteTextureTier](./mtlreadwritetexturetier.md)
  The support level for read-write texture formats.
- [enum MTLTransformType](./mtltransformtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlshadervalidation)*
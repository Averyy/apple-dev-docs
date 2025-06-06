# MTLMathMode

**Framework**: Metal  
**Kind**: enum

An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MTLMathMode
```

## Topics

### Modes
- [MTLMathMode.fast](mtlmathmode/fast.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathMode.relaxed](mtlmathmode/relaxed.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.
- [MTLMathMode.safe](mtlmathmode/safe.md)
  An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.
### Initializers
- [init?(rawValue: Int)](mtlmathmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MTLArgumentBuffersTier](mtlargumentbufferstier.md)
  The values that determine the limits and capabilities of argument buffers.
- [enum MTLLogStateError](mtllogstateerror.md)
- [enum MTLMathFloatingPointFunctions](mtlmathfloatingpointfunctions.md)
  Indicates which FP32 math functions Metal uses.
- [enum MTLMatrixLayout](mtlmatrixlayout.md)
- [enum MTLReadWriteTextureTier](mtlreadwritetexturetier.md)
  The support level for read-write texture formats.
- [enum MTLShaderValidation](mtlshadervalidation.md)
  Indicates whether shader validation in an enabled or disabled state, or neither state.
- [enum MTLTransformType](mtltransformtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmathmode)*
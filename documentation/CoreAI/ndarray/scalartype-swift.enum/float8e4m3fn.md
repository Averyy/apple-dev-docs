# NDArray.ScalarType.float8e4m3fn

**Framework**: Core AI  
**Kind**: case

An 8-bit floating-point type with 4 exponent bits and 3 mantissa bits, without a sign bit.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case float8e4m3fn
```

#### Discussion

FP8 E4M3FN (Finite Number) format emphasizes precision over range with additional mantissa bits. This type is used for quantization and in some activation functions.

## See Also

- [NDArray.ScalarType.float8e5m2](ndarray/scalartype-swift.enum/float8e5m2.md)
  An 8-bit floating-point type with 5 exponent bits and 2 mantissa bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/scalartype-swift.enum/float8e4m3fn)*
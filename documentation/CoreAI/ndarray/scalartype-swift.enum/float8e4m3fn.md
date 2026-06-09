# NDArray.ScalarType.float8e4m3fn

**Framework**: Core AI  
**Kind**: case

An 8-bit floating-point type with 4 exponent bits and 3 mantissa bits, without a sign bit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
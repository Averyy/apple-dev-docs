# NDArray.ScalarType.float8e5m2

**Framework**: Core AI  
**Kind**: case

An 8-bit floating-point type with 5 exponent bits and 2 mantissa bits.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case float8e5m2
```

#### Discussion

FP8 E5M2 format emphasizes dynamic range over precision with its larger exponent field. This type is used for quantization and in some activation functions.

## See Also

- [NDArray.ScalarType.float8e4m3fn](ndarray/scalartype-swift.enum/float8e4m3fn.md)
  An 8-bit floating-point type with 4 exponent bits and 3 mantissa bits, without a sign bit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/scalartype-swift.enum/float8e5m2)*
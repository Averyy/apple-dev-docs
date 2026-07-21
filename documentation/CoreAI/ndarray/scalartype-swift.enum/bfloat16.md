# NDArray.ScalarType.bfloat16

**Framework**: Core AI  
**Kind**: case

A 16-bit brain floating-point type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case bfloat16
```

#### Discussion

BFloat16 (Brain Floating Point) uses 8 exponent bits and 7 mantissa bits, matching the exponent range of Float32 but with reduced precision. This type is widely supported across most operations including matrix multiplication, activation functions, and quantization.

## See Also

- [NDArray.ScalarType.float16](ndarray/scalartype-swift.enum/float16.md)
  A 16-bit floating-point type.
- [NDArray.ScalarType.float32](ndarray/scalartype-swift.enum/float32.md)
  A 32-bit floating-point type.
- [NDArray.ScalarType.float64](ndarray/scalartype-swift.enum/float64.md)
  A 64-bit floating-point type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/scalartype-swift.enum/bfloat16)*
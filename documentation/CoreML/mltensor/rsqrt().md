# rsqrt()

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Computes reverse square root of the tensor’s elements.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func rsqrt() -> MLTensor
```

## Discussion

The reverse square root operation is the reciprocal of the square root.

## See Also

### Computing the exponent, pow and square root
- [func exp() -> MLTensor](./exp%28%29.md)
  Computes the natural exponent of the tensor’s elements.
- [func exp2() -> MLTensor](./exp2%28%29.md)
  Computes the exponent with base two of the tensor’s elements.
- [func pow(_:)](./pow%28_%29.md)
  Computes element-wise power of each element with `exponent`.
- [func squared() -> MLTensor](./squared%28%29.md)
  Computes square of the tensor’s elements.
- [func squareRoot() -> MLTensor](./squareroot%28%29.md)
  Computes square root of the tensor’s elements.
- [func log() -> MLTensor](./log%28%29.md)
  Computes the natural logarithm of the tensor’s elements.
- [func round() -> MLTensor](./round%28%29.md)
  Rounds the tensor’s elements.
- [func matmul(MLTensor) -> MLTensor](./matmul%28_%29.md)
  Multiplies two tensors together using matrix multiplication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/rsqrt())*
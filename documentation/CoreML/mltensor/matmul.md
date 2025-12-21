# matmul(_:)

**Framework**: Core ML  
**Kind**: method

Multiplies two tensors together using matrix multiplication.

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
func matmul(_ other: MLTensor) -> MLTensor
```

#### Return Value

The result of the matrix multiplication.

#### Discussion

The specific behaviour is determined by the dimensionality of the inputs, as described below:

- If both tensors are 1-dimensional, the dot-product is returned.
- If the first is 2-dimensional and other 1-dimensional, the matrix-vector product is returned.
- If both have a rank of 2, the matrix-matrix product is returned and when the rank is greater than 2, the batched matrix multiply is returned

For example:

```swift
let v1 = MLTensor([1.0, 2.0, 3.0, 4.0])
let v2 = MLTensor([5.0, 6.0, 7.0, 8.0])
let v3 = v1.matmul(v2)
v3.shape // is []
await v3.shapedArray(of: Float.self) // is 70.0

let m1 = MLTensor(shape: [2, 3], scalars: [
    1, 2, 3,
    4, 5, 6
], scalarType: Float.self)
let m2 = MLTensor(shape: [3, 2], scalars: [
     7,  8,
     9, 10,
    11, 12
], scalarType: Float.self)
let m3 = t1.matmul(r2)
m3.shape // is [2, 2]
await m3.shapedArray(of: Float.self) // is [[58, 64], [139, 154]]

// Supports broadcasting
let m4 = MLTensor(randomNormal: [3, 1, 1, 4], scalarType: Float.self)
let m5 = MLTensor(randomNormal: [4, 2], scalarType: Float.self)
let m6 = t4.matmul(t5)
m6.shape // is [3, 1, 1, 2]
```

## Parameters

- `other`: The right-hand side tensor to be multiplied.

## See Also

- [func exp() -> MLTensor](mltensor/exp.md)
  Computes the natural exponent of the tensor’s elements.
- [func exp2() -> MLTensor](mltensor/exp2.md)
  Computes the exponent with base two of the tensor’s elements.
- [func pow(_:)](mltensor/pow(_:).md)
  Computes element-wise power of each element with `exponent`.
- [func rsqrt() -> MLTensor](mltensor/rsqrt.md)
  Computes reverse square root of the tensor’s elements.
- [func squared() -> MLTensor](mltensor/squared.md)
  Computes square of the tensor’s elements.
- [func squareRoot() -> MLTensor](mltensor/squareroot.md)
  Computes square root of the tensor’s elements.
- [func log() -> MLTensor](mltensor/log.md)
  Computes the natural logarithm of the tensor’s elements.
- [func round() -> MLTensor](mltensor/round.md)
  Rounds the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/matmul(_:))*
# tiled(multiples:)

**Framework**: Core ML  
**Kind**: method

Returns a tensor by replicating its elements multiple times.

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
func tiled(multiples: [Int]) -> MLTensor
```

#### Return Value

The replicated tensor.

#### Discussion

The `multiples` argument specifies the multiplier across each dimensions, i.e., the output dimension at index `i` is equal to `shape[i] * multiples[i]`.

For example:

```swift
let x = MLTensor(shape: [2, 2], scalars: [1, 2, 3, 4], scalarType: Float.self)
let y = x.tiled(multiples: [1, 2])
y.shape // is [2, 4]
```

If `multiples` specifies fewer dimensions than the tensor, then ones are prepended to `multiples` until all the dimensions are specified.

If tensor has fewer dimensions than `multiples`, then the tensor is reshaped by prepending ones to the dimensions until all the dimensions are specified.

## Parameters

- `multiples`: The multiplier across each dimension. All values must be greater than zero.

## See Also

- [func expandingShape(at:)](mltensor/expandingshape(at:).md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](mltensor/bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func sign() -> MLTensor](mltensor/sign.md)
  Returns the sign of the tensor’s elements.
- [func reciprocal() -> MLTensor](mltensor/reciprocal.md)
  Computes the reciprocal of the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/tiled(multiples:))*
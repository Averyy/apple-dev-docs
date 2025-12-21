# bandPart(lowerBandCount:upperBandCount:)

**Framework**: Core ML  
**Kind**: method

Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.

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
func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor
```

#### Return Value

The band part of the tensor.

#### Discussion

The framework copies a diagonal band of values from the tensor to the result tensor of the same size. A coordinate `[..., i, j]` is considered in band if

```md
(lowerBandCount < 0 || (i-j) <= lowerBandCount) && (upperBandCount < 0 || (j-i) <= upperBandCount)
```

Values outside of the band are set to `0`.

For example:

```swift
let t = Tensor([
    [ 5,  1,  2, 3],
    [-1,  5,  1, 2],
    [-2, -1,  5, 1],
    [-3, -2, -1, 5]
], scalarType: Float.self)

t.bandPart(lowerBandCount: 0, upperBandCount: 0)
// [[ 5,  0,  0, 0]
//  [ 0,  5,  0, 0]
//  [ 0,  0,  5, 0]
//  [ 0,  0,  0, 5]]

t.bandPart(lowerBandCount: 0, upperBandCount: -1)
// [[ 5,  1,  2, 3]
//  [ 0,  5,  1, 2]
//  [ 0,  0,  5, 1]
//  [ 0,  0,  0, 5]]

t.bandPart(lowerBandCount: -1, upperBandCount: 0)
// [[ 5,  0,  0, 0]
//  [-1,  5,  0, 0]
//  [-2, -1,  5, 0]
//  [-3, -2, -1, 5]]
```

## Parameters

- `lowerBandCount`: The number of diagonals in the lower triangle to keep. If  , keep the entire lower triangle.
- `upperBandCount`: The number of diagonals in the upper triangle to keep. If  , keep the entire upper triangle.

## See Also

- [func expandingShape(at:)](mltensor/expandingshape(at:).md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func tiled(multiples: [Int]) -> MLTensor](mltensor/tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.
- [func sign() -> MLTensor](mltensor/sign.md)
  Returns the sign of the tensor’s elements.
- [func reciprocal() -> MLTensor](mltensor/reciprocal.md)
  Computes the reciprocal of the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/bandpart(lowerbandcount:upperbandcount:))*
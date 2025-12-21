# expandingShape(at:)

**Framework**: Core ML  
**Kind**: method

Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

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
func expandingShape(at axes: Int...) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor(shape: [2], scalars: [1, 2], scalarType: Float.self)
let y = x.expandingShape(at: 0)
y.shape // is [1, 2]
```

## Parameters

- `axes`: The axes at which to expand the shape.

## See Also

- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](mltensor/bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func tiled(multiples: [Int]) -> MLTensor](mltensor/tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.
- [func sign() -> MLTensor](mltensor/sign.md)
  Returns the sign of the tensor’s elements.
- [func reciprocal() -> MLTensor](mltensor/reciprocal.md)
  Computes the reciprocal of the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/expandingshape(at:))*
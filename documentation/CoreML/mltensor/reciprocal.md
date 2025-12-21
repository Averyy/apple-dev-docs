# reciprocal()

**Framework**: Core ML  
**Kind**: method

Computes the reciprocal of the tensor’s elements.

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
func reciprocal() -> MLTensor
```

## See Also

- [func expandingShape(at:)](mltensor/expandingshape(at:).md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](mltensor/bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func tiled(multiples: [Int]) -> MLTensor](mltensor/tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.
- [func sign() -> MLTensor](mltensor/sign.md)
  Returns the sign of the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/reciprocal())*
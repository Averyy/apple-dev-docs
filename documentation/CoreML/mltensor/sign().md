# sign()

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns the sign of the tensor’s elements.

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
func sign() -> MLTensor
```

#### Discussion

This operation returns `1.0` if the correspnding element is greater than `0`, `-1.0` if it is less than `0`, `-0.0` if it is equal to `-0.0`, and `+0.0` if it is equal to `+0.0`.

## See Also

### Accessing the extended tensor, sign and reciprocal
- [func expandingShape(at:)](./expandingshape%28at%29.md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](./bandpart%28lowerbandcount,upperbandcount%29.md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func tiled(multiples: [Int]) -> MLTensor](./tiled%28multiples%29.md)
  Returns a tensor by replicating its elements multiple times.
- [func reciprocal() -> MLTensor](./reciprocal%28%29.md)
  Computes the reciprocal of the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/sign())*
# .>(_:_:)

**Framework**: Core ML  
**Kind**: op

Computes element-wise greater comparison between two tensors.

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
static func .> (lhs: MLTensor, rhs: MLTensor) -> MLTensor
```

#### Return Value

A Boolean tensor where each element is true if the left hand side tensor is greater than the corresponding element of the right hand side, and false otherwise.

#### Discussion

Shapes must be broadcastable, where the broadcasted shape becomes the shape of the output.

## See Also

- [static *(_:_:)](mltensor/*(_:_:).md)
  Computes element-wise multiplication.
- [static func *= (inout MLTensor, MLTensor)](mltensor/*=(_:_:).md)
  Computes element-wise multiplication.
- [static +(_:_:)](mltensor/+(_:_:).md)
  Computes element-wise addition.
- [static func += (inout MLTensor, MLTensor)](mltensor/+=(_:_:).md)
  Computes element-wise addition.
- [static func - (MLTensor) -> MLTensor](mltensor/-(_:).md)
  Returns the negation of the tensor.
- [static -(_:_:)](mltensor/-(_:_:).md)
  Computes element-wise subtraction.
- [static func -= (inout MLTensor, MLTensor)](mltensor/-=(_:_:).md)
  Computes element-wise subtraction.
- [static func .! (MLTensor) -> MLTensor](mltensor/'.!(_:).md)
  Computes logical not on the tensor’s elements.
- [static .!=(_:_:)](mltensor/'.!=(_:_:).md)
  Computes element-wise inequality between two tensors.
- [static func .& (MLTensor, MLTensor) -> MLTensor](mltensor/'.&(_:_:).md)
  Computes element-wise logical AND where both operands are expected contain Boolean scalar elements.
- [static .==(_:_:)](mltensor/'.==(_:_:).md)
  Computes element-wise equality between two tensors.
- [static .<(_:_:)](mltensor/'._(_:_:)-6kfoh.md)
  Computes element-wise less comparison between two tensors.
- [static func .| (MLTensor, MLTensor) -> MLTensor](mltensor/'._(_:_:)-7z7ks.md)
  Computes element-wise logical OR where both operands are expected contain Boolean scalar elements.
- [static func .^ (MLTensor, MLTensor) -> MLTensor](mltensor/'._(_:_:)-8il7w.md)
  Computes element-wise logical XOR where both operands are expected contain Boolean scalar elements.
- [static .>=(_:_:)](mltensor/'._=(_:_:)-5qa2u.md)
  Computes element-wise greater than or equal to comparison between two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/'._(_:_:)-3m3ro)*
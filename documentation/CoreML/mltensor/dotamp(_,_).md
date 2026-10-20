# .&(_:_:)

**Framework**: Core ML  
**Kind**: op  
**Role**: Operator

Computes element-wise logical AND where both operands are expected contain Boolean scalar elements.

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
static func .& (lhs: MLTensor, rhs: MLTensor) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([true, true, true])
let y = MLTensor([true, false, true])
x .& y // is [true, false, true]
```

## See Also

### Performing arithmetic operations
- [static *(_:_:)](./star%28_,_%29.md)
  Computes element-wise multiplication.
- [static func *= (inout MLTensor, MLTensor)](./stareq%28_,_%29.md)
  Computes element-wise multiplication.
- [static +(_:_:)](./plus%28_,_%29.md)
  Computes element-wise addition.
- [static func += (inout MLTensor, MLTensor)](./pluseq%28_,_%29.md)
  Computes element-wise addition.
- [static func - (MLTensor) -> MLTensor](./minus%28_%29.md)
  Returns the negation of the tensor.
- [static -(_:_:)](./minus%28_,_%29.md)
  Computes element-wise subtraction.
- [static func -= (inout MLTensor, MLTensor)](./minuseq%28_,_%29.md)
  Computes element-wise subtraction.
- [static func .! (MLTensor) -> MLTensor](./dotnot%28_%29.md)
  Computes logical not on the tensor’s elements.
- [static .!=(_:_:)](./dotnoteq%28_,_%29.md)
  Computes element-wise inequality between two tensors.
- [static .==(_:_:)](./doteqeq%28_,_%29.md)
  Computes element-wise equality between two tensors.
- [static .>(_:_:)](./dotop%28_,_%29-3m3ro.md)
  Computes element-wise greater comparison between two tensors.
- [static .<(_:_:)](./dotop%28_,_%29-6kfoh.md)
  Computes element-wise less comparison between two tensors.
- [static func .| (MLTensor, MLTensor) -> MLTensor](./dotop%28_,_%29-7z7ks.md)
  Computes element-wise logical OR where both operands are expected contain Boolean scalar elements.
- [static func .^ (MLTensor, MLTensor) -> MLTensor](./dotop%28_,_%29-8il7w.md)
  Computes element-wise logical XOR where both operands are expected contain Boolean scalar elements.
- [static .>=(_:_:)](./dotopeq%28_,_%29-5qa2u.md)
  Computes element-wise greater than or equal to comparison between two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/'.&(_:_:))*
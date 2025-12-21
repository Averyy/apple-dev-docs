# SparseScaling_t

**Framework**: Accelerate  
**Kind**: struct

Options that define which scaling algorithm to use.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SparseScaling_t
```

## Topics

### Constants
- [var SparseScalingDefault: SparseScaling_t](sparsescalingdefault.md)
  Default scaling.
- [var SparseScalingUser: SparseScaling_t](sparsescalinguser.md)
  User scaling.
- [var SparseScalingEquilibriationInf: SparseScaling_t](sparsescalingequilibriationinf.md)
  The norm equilibration scaling using infinity norm.
- [var SparseScalingHungarianScalingOnly: SparseScaling_t](sparsescalinghungarianscalingonly.md)
  Scaling using the Hungarian algorithm.
- [var SparseScalingHungarianScalingAndOrdering: SparseScaling_t](sparsescalinghungarianscalingandordering.md)
  Scaling and ordering using the Hungarian algorithm.
### Raw Values
- [init(UInt8)](sparsescaling_t/init(_:).md)
- [init(rawValue: UInt8)](sparsescaling_t/init(rawvalue:).md)
- [var rawValue: UInt8](sparsescaling_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var control: SparseControl_t](sparsenumericfactoroptions/control.md)
  The flags that control the computation.
- [struct SparseControl_t](sparsecontrol_t.md)
  Options that control the computation.
- [var scalingMethod: SparseScaling_t](sparsenumericfactoroptions/scalingmethod.md)
  The scaling method.
- [var scaling: UnsafeMutableRawPointer?](sparsenumericfactoroptions/scaling.md)
  An array that scales the matrix before factorization.
- [var pivotTolerance: Double](sparsenumericfactoroptions/pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](sparsenumericfactoroptions/zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsescaling_t)*
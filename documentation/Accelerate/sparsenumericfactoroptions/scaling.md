# scaling

**Framework**: Accelerate  
**Kind**: property

An array that scales the matrix before factorization.

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
var scaling: UnsafeMutableRawPointer?
```

#### Discussion

This array can either be `nil` or a pointer to an array of real values with a length greater than or equal to the size of the matrix that you’re factoring. The type of the array values is the element type of the matrix (but real, even if the matrix is complex).

If [`scalingMethod`](sparsenumericfactoroptions/scalingmethod.md) is [`SparseScalingUser`](sparsescalinguser.md), and this pointer is `nil`, the system doesn’t apply scaling.

If [`scalingMethod`](sparsenumericfactoroptions/scalingmethod.md) is [`SparseScalingUser`](sparsescalinguser.md), and this pointer isn’t `nil`, the system uses the user-provided array to scale the matrix before factorization.

If [`scalingMethod`](sparsenumericfactoroptions/scalingmethod.md) isn’t [`SparseScalingUser`](sparsescalinguser.md), the factor function computes its own scaling.

If this pointer isn’t `nil`, the computed scaling returns in the array.

## See Also

- [var control: SparseControl_t](sparsenumericfactoroptions/control.md)
  The flags that control the computation.
- [struct SparseControl_t](sparsecontrol_t.md)
  Options that control the computation.
- [var scalingMethod: SparseScaling_t](sparsenumericfactoroptions/scalingmethod.md)
  The scaling method.
- [struct SparseScaling_t](sparsescaling_t.md)
  Options that define which scaling algorithm to use.
- [var pivotTolerance: Double](sparsenumericfactoroptions/pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](sparsenumericfactoroptions/zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/scaling)*
# scalingMethod

**Framework**: Accelerate  
**Kind**: property

The scaling method.

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
var scalingMethod: SparseScaling_t
```

## See Also

- [var control: SparseControl_t](sparsenumericfactoroptions/control.md)
  The flags that control the computation.
- [struct SparseControl_t](sparsecontrol_t.md)
  Options that control the computation.
- [var scaling: UnsafeMutableRawPointer?](sparsenumericfactoroptions/scaling.md)
  An array that scales the matrix before factorization.
- [struct SparseScaling_t](sparsescaling_t.md)
  Options that define which scaling algorithm to use.
- [var pivotTolerance: Double](sparsenumericfactoroptions/pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](sparsenumericfactoroptions/zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/scalingmethod)*
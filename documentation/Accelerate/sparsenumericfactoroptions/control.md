# control

**Framework**: Accelerate  
**Kind**: property

The flags that control the computation.

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
var control: SparseControl_t
```

## See Also

- [struct SparseControl_t](sparsecontrol_t.md)
  Options that control the computation.
- [var scalingMethod: SparseScaling_t](sparsenumericfactoroptions/scalingmethod.md)
  The scaling method.
- [var scaling: UnsafeMutableRawPointer?](sparsenumericfactoroptions/scaling.md)
  An array that scales the matrix before factorization.
- [struct SparseScaling_t](sparsescaling_t.md)
  Options that define which scaling algorithm to use.
- [var pivotTolerance: Double](sparsenumericfactoroptions/pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](sparsenumericfactoroptions/zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/control)*
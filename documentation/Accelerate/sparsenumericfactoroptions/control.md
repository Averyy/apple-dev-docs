# control

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The flags that control the computation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var control: SparseControl_t
```

```c
SparseControl_t control;
```

## See Also

### Instance Properties
- [struct SparseControl_t](../sparsecontrol_t.md)
  Options that control the computation.
- [var scalingMethod: SparseScaling_t](./scalingmethod.md)
  The scaling method.
- [var scaling: UnsafeMutableRawPointer?](./scaling.md)
  An array that scales the matrix before factorization.
- [struct SparseScaling_t](../sparsescaling_t.md)
  Options that define which scaling algorithm to use.
- [var pivotTolerance: Double](./pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](./zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/control)*
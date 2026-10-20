# zeroTolerance

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The zero tolerance that some pivoting modes use.

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
var zeroTolerance: Double
```

```c
double zeroTolerance;
```

#### Discussion

> **Note**:  Only the symmetric factorization algorithms use the [`zeroTolerance`](./zerotolerance.md) parameter. [`SparseFactorizationQR`](../sparsefactorizationqr.md) ignores the zero tolerance value.

## See Also

### Instance Properties
- [var control: SparseControl_t](./control.md)
  The flags that control the computation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/zerotolerance)*
# pivotTolerance

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The pivot tolerance that threshold partial pivoting uses.

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
var pivotTolerance: Double
```

```c
double pivotTolerance;
```

## Discussion

The system clamps this to range `[0,0.5]`.

> **Note**:  Only the symmetric factorization algorithms use the [`pivotTolerance`](./pivottolerance.md) parameter. [`SparseFactorizationQR`](../sparsefactorizationqr.md)  ignores the pivot tolerance value.

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
- [var zeroTolerance: Double](./zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/pivottolerance)*
# scalingMethod

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The scaling method.

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
var scalingMethod: SparseScaling_t
```

```c
SparseScaling_t scalingMethod;
```

## See Also

### Instance Properties
- [var control: SparseControl_t](./control.md)
  The flags that control the computation.
- [struct SparseControl_t](../sparsecontrol_t.md)
  Options that control the computation.
- [var scaling: UnsafeMutableRawPointer?](./scaling.md)
  An array that scales the matrix before factorization.
- [struct SparseScaling_t](../sparsescaling_t.md)
  Options that define which scaling algorithm to use.
- [var pivotTolerance: Double](./pivottolerance.md)
  The pivot tolerance that threshold partial pivoting uses.
- [var zeroTolerance: Double](./zerotolerance.md)
  The zero tolerance that some pivoting modes use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/scalingmethod)*
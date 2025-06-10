# SparseNumericFactorOptions

**Framework**: Accelerate  
**Kind**: struct

A structure that contains options that affect the numerical stage of a sparse factorization.

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
struct SparseNumericFactorOptions
```

#### Overview

[`SparseNumericFactorOptions`](sparsenumericfactoroptions.md) supports the following types of scaling:

| [`SparseScalingDefault`](sparsescalingdefault.md) | Default scaling — [`SparseScalingEquilibriationInf`](sparsescalingequilibriationinf.md) if , or no scaling if Cholesky. |
| --- | --- |
| [`SparseScalingUser`](sparsescalinguser.md) | User scaling if [`scaling`](sparsenumericfactoroptions/scaling.md) is nonnull; otherwise, no scaling. |
| [`SparseScalingEquilibriationInf`](sparsescalingequilibriationinf.md) | Norm equilibration scaling using infinity norm. |

Note that the system clamps [`pivotTolerance`](sparsenumericfactoroptions/pivottolerance.md) to range `[0,0.5]`.

## Topics

### Creating a Numeric Factor Options Stucture
- [init(control: SparseControl_t, scalingMethod: SparseScaling_t, scaling: UnsafeMutableRawPointer?, pivotTolerance: Double, zeroTolerance: Double)](sparsenumericfactoroptions/init(control:scalingmethod:scaling:pivottolerance:zerotolerance:).md)
  Returns a new numeric factor options structure with the specified properties.
- [init()](sparsenumericfactoroptions/init.md)
  Returns a new numeric factor options structure with default properties.
### Instance Properties
- [var control: SparseControl_t](sparsenumericfactoroptions/control.md)
  The flags that control the computation.
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

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.
- [struct SparseSymbolicFactorOptions](sparsesymbolicfactoroptions.md)
  A structure that contains options that affect the symbolic stage of a sparse factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions)*
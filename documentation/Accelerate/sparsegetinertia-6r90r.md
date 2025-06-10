# SparseGetInertia(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the inertia of a single-precision  factorization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func SparseGetInertia(_ Factored: SparseOpaqueFactorization_Float, _ num_positive: UnsafeMutablePointer<Int32>, _ num_zero: UnsafeMutablePointer<Int32>, _ num_negative: UnsafeMutablePointer<Int32>) -> Int32
```

#### Return Value

`0` on success; otherwise, a nonzero value on error.

#### Discussion

This function returns the number of negative, zero, and positive pivots that the sparse factorization functions, [`SparseFactor(_:_:)`](sparsefactor(_:_:)-38shj.md) and [`SparseFactor(_:_:_:_:)`](sparsefactor(_:_:_:_:)-8apyz.md), take during an  factorization.

In some cases — for example, when the original matrix’s eigenvalues are close to zero — the computed numerical inertia may not be an accurate reflection of the true inertia. In such cases, the computed numerical inertia is dependent on the [`zeroTolerance`](sparsenumericfactoroptions/zerotolerance.md) and [`pivotTolerance`](sparsenumericfactoroptions/pivottolerance.md) values of the [`SparseNumericFactorOptions`](sparsenumericfactoroptions.md) structure.

> ❗ **Important**:  This function supports only [`SparseFactorizationLDLTTPP`](sparsefactorizationldlttpp.md) factorizations.

## Parameters

- `Factored`: The   factorization.
- `num_positive`: On return, the number of positive pivots the sparse factorization functions take during the factorization of  .
- `num_zero`: On return, the number of zero pivots the sparse factorization functions take during the factorization of  .
- `num_negative`: On return, the number of negative pivots the sparse factorization functions take during the factorization of  .

## See Also

- [func SparseGetInertia(SparseOpaqueFactorization_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2ykzq.md)
  Returns the inertia of a double-precision  factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2gc7f.md)
  Returns the inertia of an LDLT factorization in complex double.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-6ca5h.md)
  Returns the inertia of an LDLT factorization in complex float.
- [struct SparseUpdate_t](sparseupdate_t.md)
  Low-rank update algorithm selector
- [var SparseUpdatePartialRefactor: SparseUpdate_t](sparseupdatepartialrefactor.md)
  Low-rank update algorithm selector


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetinertia(_:_:_:_:)-6r90r)*
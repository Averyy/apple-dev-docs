# SparseRetain(_:)

**Framework**: Accelerate  
**Kind**: func

Increase reference count on a numeric factorization object, returning a copy.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseRetain(_ NumericFactor: SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float
```

#### Return Value

A copy of NumericFactor.

## Parameters

- `NumericFactor`: The symbolic factorization to increase the underlying   reference count of.

## See Also

- [func SparseRetain(SparseOpaqueSymbolicFactorization) -> SparseOpaqueSymbolicFactorization](sparseretain(_:)-8r2dm.md)
  Increases the reference count on a symbolic factorization object.
- [func SparseRetain(SparseOpaqueFactorization_Double) -> SparseOpaqueFactorization_Double](sparseretain(_:)-8943y.md)
  Increases the reference count on a double-precision numeric factorization object.
- [func SparseRetain(SparseOpaqueFactorization_Float) -> SparseOpaqueFactorization_Float](sparseretain(_:)-7onhr.md)
  Increases the reference count on a single-precision numeric factorization object.
- [func SparseRetain(SparseOpaqueSubfactor_Double) -> SparseOpaqueSubfactor_Double](sparseretain(_:)-2pmdl.md)
  Increases the reference count on a double-precision subfactor object.
- [func SparseRetain(SparseOpaqueSubfactor_Float) -> SparseOpaqueSubfactor_Float](sparseretain(_:)-6mr6d.md)
  Increases the reference count on a single-precision subfactor object.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparseretain(_:)-5sahb.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparseretain(_:)-6pp40.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparseretain(_:)-92857.md)
  Increase reference count on a numeric factorization object, returning a copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseretain(_:)-92v4w)*
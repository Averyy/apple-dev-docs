# SparseRetain(_:)

**Framework**: Accelerate  
**Kind**: func

Increases the reference count on a single-precision subfactor object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseRetain(_ Subfactor: SparseOpaqueSubfactor_Float) -> SparseOpaqueSubfactor_Float
```

#### Return Value

The supplied numeric subfactor object.

## Parameters

- `Subfactor`: The subfactor object to increase the reference count upon.

## See Also

- [func SparseRetain(SparseOpaqueSymbolicFactorization) -> SparseOpaqueSymbolicFactorization](sparseretain(_:)-8r2dm.md)
  Increases the reference count on a symbolic factorization object.
- [func SparseRetain(SparseOpaqueFactorization_Double) -> SparseOpaqueFactorization_Double](sparseretain(_:)-8943y.md)
  Increases the reference count on a double-precision numeric factorization object.
- [func SparseRetain(SparseOpaqueFactorization_Float) -> SparseOpaqueFactorization_Float](sparseretain(_:)-7onhr.md)
  Increases the reference count on a single-precision numeric factorization object.
- [func SparseRetain(SparseOpaqueSubfactor_Double) -> SparseOpaqueSubfactor_Double](sparseretain(_:)-2pmdl.md)
  Increases the reference count on a double-precision subfactor object.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparseretain(_:)-5sahb.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparseretain(_:)-6pp40.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparseretain(_:)-92857.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparseretain(_:)-92v4w.md)
  Increase reference count on a numeric factorization object, returning a copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseretain(_:)-6mr6d)*
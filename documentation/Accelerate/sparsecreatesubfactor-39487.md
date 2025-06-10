# SparseCreateSubfactor(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns an opaque object representing a sub-factor of a factorization in complex double.

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
func SparseCreateSubfactor(_ subfactor: SparseSubfactor_t, _ Factor: SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double
```

#### Return Value

Object representing the requested sub-factor. Must be cleaned up by a call to `SparseCleanup` once it is no longer required.

#### Discussion

Here the term “sub-factor” is used to mean one or more parts of the whole factorization. For example, just the `Q` factor from `A=QRP`. The returned object is a wrapper around the orignal factorization, and does not actually perform any extraction (sub-factors are stored in non-standard formats that exploit implicit structure for efficiency, and formation of the sub-factor explicitly can be expensive). It is intended to be used as an argument to `SparseMultiply` and `SparseSolve` functions only.

As `Factor` is contained in the returned object, its underlying reference count in incremented, and the returned object must hence be destroyed through a call to `SparseCleanup` to prevent a memory leak (however it is safe to call `SparseCleanup` on the original factorization whilst this object is still being used).

## Parameters

- `subfactor`: The sub-factor the new object should represent.
- `Factor`: The factorization to extract the sub-factor from.

## See Also

- [struct SparseSubfactor_t](sparsesubfactor_t.md)
  Constants that define the subfactor of a factorization.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Double) -> SparseOpaqueSubfactor_Double](sparsecreatesubfactor(_:_:)-49d8w.md)
  Returns an opaque object that represents a subfactor of a factorization of a matrix of double-precision values.
- [struct SparseOpaqueFactorization_Double](sparseopaquefactorization_double.md)
  A structure that represents the factorization of a matrix of double-precision, floating-point values.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Float) -> SparseOpaqueSubfactor_Float](sparsecreatesubfactor(_:_:)-4renf.md)
  Returns an opaque object that represents a subfactor of a factorization of a matrix of single-precision values.
- [struct SparseOpaqueFactorization_Float](sparseopaquefactorization_float.md)
  A structure that represents the factorization of a matrix of single-precision, floating-point values.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsecreatesubfactor(_:_:)-udwd.md)
  Returns an opaque object representing a sub-factor of a factorization in complex float.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecreatesubfactor(_:_:)-39487)*
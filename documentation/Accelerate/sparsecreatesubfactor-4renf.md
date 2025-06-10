# SparseCreateSubfactor(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns an opaque object that represents a subfactor of a factorization of a matrix of single-precision values.

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
func SparseCreateSubfactor(_ subfactor: SparseSubfactor_t, _ Factor: SparseOpaqueFactorization_Float) -> SparseOpaqueSubfactor_Float
```

#### Return Value

A `SparseOpaqueSubfactor_Float` structure that represents the subfactor. You must free the resource through a call to [`SparseCleanup(_:)`](sparsecleanup(_:)-15kpj.md) after you finish with the object.

## Parameters

- `subfactor`: Defines which subfactor to extract.
- `Factor`: The factorization to extract the subfactor from.

## See Also

- [struct SparseSubfactor_t](sparsesubfactor_t.md)
  Constants that define the subfactor of a factorization.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Double) -> SparseOpaqueSubfactor_Double](sparsecreatesubfactor(_:_:)-49d8w.md)
  Returns an opaque object that represents a subfactor of a factorization of a matrix of double-precision values.
- [struct SparseOpaqueFactorization_Double](sparseopaquefactorization_double.md)
  A structure that represents the factorization of a matrix of double-precision, floating-point values.
- [struct SparseOpaqueFactorization_Float](sparseopaquefactorization_float.md)
  A structure that represents the factorization of a matrix of single-precision, floating-point values.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsecreatesubfactor(_:_:)-39487.md)
  Returns an opaque object representing a sub-factor of a factorization in complex double.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsecreatesubfactor(_:_:)-udwd.md)
  Returns an opaque object representing a sub-factor of a factorization in complex float.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecreatesubfactor(_:_:)-4renf)*
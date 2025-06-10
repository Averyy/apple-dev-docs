# SparseSubfactor_t

**Framework**: Accelerate  
**Kind**: struct

Constants that define the subfactor of a factorization.

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
struct SparseSubfactor_t
```

## Topics

### Constants
- [var SparseSubfactorInvalid: SparseSubfactor_t](sparsesubfactorinvalid.md)
  An invalid subfactor that indicates the requested type is incompatible with the supplied factorization or the system has destroyed it.
- [var SparseSubfactorP: SparseSubfactor_t](sparsesubfactorp.md)
  A permutation subfactor that’s valid for all factorization types.
- [var SparseSubfactorS: SparseSubfactor_t](sparsesubfactors.md)
  A diagonal scaling subfactor that’s valid for Cholesky and  only.
- [var SparseSubfactorL: SparseSubfactor_t](sparsesubfactorl.md)
  An  factor subfactor that’s valid for Cholesky and  only.
- [var SparseSubfactorD: SparseSubfactor_t](sparsesubfactord.md)
  A  factor subfactor that’s valid for ` `only.
- [var SparseSubfactorPLPS: SparseSubfactor_t](sparsesubfactorplps.md)
  A half-solve subfactor that’s valid for Cholesky and  only.
- [var SparseSubfactorQ: SparseSubfactor_t](sparsesubfactorq.md)
  A  factor subfactor that’s valid for QR only.
- [var SparseSubfactorR: SparseSubfactor_t](sparsesubfactorr.md)
  An  factor subfactor that’s valid for QR and Cholesky  only.
- [var SparseSubfactorRP: SparseSubfactor_t](sparsesubfactorrp.md)
  A half-solve subfactor that’s valid for QR and Cholesky  only.
- [var SparseSubfactorSc: SparseSubfactor_t](sparsesubfactorsc.md)
  Types of sub-factor object.
- [var SparseSubfactorSr: SparseSubfactor_t](sparsesubfactorsr.md)
  Types of sub-factor object.
### Raw Values
- [init(UInt8)](sparsesubfactor_t/init(_:).md)
- [init(rawValue: UInt8)](sparsesubfactor_t/init(rawvalue:).md)
- [var rawValue: UInt8](sparsesubfactor_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Double) -> SparseOpaqueSubfactor_Double](sparsecreatesubfactor(_:_:)-49d8w.md)
  Returns an opaque object that represents a subfactor of a factorization of a matrix of double-precision values.
- [struct SparseOpaqueFactorization_Double](sparseopaquefactorization_double.md)
  A structure that represents the factorization of a matrix of double-precision, floating-point values.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Float) -> SparseOpaqueSubfactor_Float](sparsecreatesubfactor(_:_:)-4renf.md)
  Returns an opaque object that represents a subfactor of a factorization of a matrix of single-precision values.
- [struct SparseOpaqueFactorization_Float](sparseopaquefactorization_float.md)
  A structure that represents the factorization of a matrix of single-precision, floating-point values.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsecreatesubfactor(_:_:)-39487.md)
  Returns an opaque object representing a sub-factor of a factorization in complex double.
- [func SparseCreateSubfactor(SparseSubfactor_t, SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsecreatesubfactor(_:_:)-udwd.md)
  Returns an opaque object representing a sub-factor of a factorization in complex float.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesubfactor_t)*
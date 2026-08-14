# SparseFactorization_t

**Framework**: Accelerate  
**Kind**: struct

Constants that define the factorization type.

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
struct SparseFactorization_t
```

## Topics

### LU factorization types
- [var SparseFactorizationLU: SparseFactorization_t](sparsefactorizationlu.md)
  Default LU factorization, currently LU with TPP.
- [var SparseFactorizationLUSPP: SparseFactorization_t](sparsefactorizationluspp.md)
  LU factorization with partial pivoting restricted to within supernodes only.
- [var SparseFactorizationLUTPP: SparseFactorization_t](sparsefactorizationlutpp.md)
  LU factorization with threshold partial pivoting.
- [var SparseFactorizationLUUnpivoted: SparseFactorization_t](sparsefactorizationluunpivoted.md)
  LU factorization with no numerical pivoting.
### Factorization types for symmetric coefficient matrices
- [var SparseFactorizationCholesky: SparseFactorization_t](sparsefactorizationcholesky.md)
  A constant that represents Cholesky (*LLᵀ*) factorization.
- [var SparseFactorizationLDLT: SparseFactorization_t](sparsefactorizationldlt.md)
  A constant that represents the default *LDLᵀ* factorization.
- [var SparseFactorizationLDLTUnpivoted: SparseFactorization_t](sparsefactorizationldltunpivoted.md)
  A constant that represents Cholesky-like *LDLᵀ* factorization with only one-by-one pivots and no pivoting.
- [var SparseFactorizationLDLTSBK: SparseFactorization_t](sparsefactorizationldltsbk.md)
  A constant that represents *LDLᵀ* factorization with Supernode-Bunch-Kaufman and static pivoting.
- [var SparseFactorizationLDLTTPP: SparseFactorization_t](sparsefactorizationldlttpp.md)
  A constant that represents *LDLᵀ* factorization with full-threshold partial pivoting.
### Factorization types for overdetermined and underdetermined systems
- [var SparseFactorizationQR: SparseFactorization_t](sparsefactorizationqr.md)
  A constant that represents QR factorization.
- [var SparseFactorizationCholeskyAtA: SparseFactorization_t](sparsefactorizationcholeskyata.md)
  A constant that represents *QR* factorization without storing *Q*.
### Raw Values
- [init(UInt8)](sparsefactorization_t/init(_:).md)
- [init(rawValue: UInt8)](sparsefactorization_t/init(rawvalue:).md)
- [var rawValue: UInt8](sparsefactorization_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct SparseSymbolicFactorOptions](sparsesymbolicfactoroptions.md)
  A structure that contains options that affect the symbolic stage of a sparse factorization.
- [struct SparseNumericFactorOptions](sparsenumericfactoroptions.md)
  A structure that contains options that affect the numerical stage of a sparse factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactorization_t)*
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
  Types of factorization than can be performed.
- [var SparseFactorizationLUSPP: SparseFactorization_t](sparsefactorizationluspp.md)
  Types of factorization than can be performed.
- [var SparseFactorizationLUTPP: SparseFactorization_t](sparsefactorizationlutpp.md)
  Types of factorization than can be performed.
- [var SparseFactorizationLUUnpivoted: SparseFactorization_t](sparsefactorizationluunpivoted.md)
  Types of factorization than can be performed.
### Factorization types for symmetric coefficient matrices
- [var SparseFactorizationCholesky: SparseFactorization_t](sparsefactorizationcholesky.md)
  A constant that represents Cholesky () factorization.
- [var SparseFactorizationLDLT: SparseFactorization_t](sparsefactorizationldlt.md)
  A constant that represents the default  factorization.
- [var SparseFactorizationLDLTUnpivoted: SparseFactorization_t](sparsefactorizationldltunpivoted.md)
  A constant that represents Cholesky-like  factorization with only one-by-one pivots and no pivoting.
- [var SparseFactorizationLDLTSBK: SparseFactorization_t](sparsefactorizationldltsbk.md)
  A constant that represents  factorization with Supernode-Bunch-Kaufman and static pivoting.
- [var SparseFactorizationLDLTTPP: SparseFactorization_t](sparsefactorizationldlttpp.md)
  A constant that represents  factorization with full-threshold partial pivoting.
### Factorization types for overdetermined and underdetermined systems
- [var SparseFactorizationQR: SparseFactorization_t](sparsefactorizationqr.md)
  A constant that represents QR factorization.
- [var SparseFactorizationCholeskyAtA: SparseFactorization_t](sparsefactorizationcholeskyata.md)
  A constant that represents  factorization without storing .
### Raw Values
- [init(UInt8)](sparsefactorization_t/init(_:).md)
- [init(rawValue: UInt8)](sparsefactorization_t/init(rawvalue:).md)
- [var rawValue: UInt8](sparsefactorization_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SparseSymbolicFactorOptions](sparsesymbolicfactoroptions.md)
  A structure that contains options that affect the symbolic stage of a sparse factorization.
- [struct SparseNumericFactorOptions](sparsenumericfactoroptions.md)
  A structure that contains options that affect the numerical stage of a sparse factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactorization_t)*
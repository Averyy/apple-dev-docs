# SparseSubfactorSc

**Framework**: Accelerate  
**Kind**: var

Types of sub-factor object.

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
var SparseSubfactorSc: SparseSubfactor_t { get }
```

#### Discussion

- **`SparseSubfactorInvalid`**: Invalid subfactor (requested type not compatible with supplied factorization or already destroyed).
- **`SparseSubfactorP`**: Permutation subfactor, valid for all factorization types. (this is the row permutation for LU factorization)
- **`SparseSubfactorS`**: Diagonal scaling subfactor, valid for Cholesky and LDL^T only.
- **`SparseSubfactorL`**: L factor subfactor, valid for Cholesky and LDL^T only.
- **`SparseSubfactorD`**: D factor subfactor, valid for LDL^T only.
- **`SparseSubfactorPLPS`**: Half-solve subfactor, valid for Cholesky and LDL^T only. Corresponds to PLP’ on forward (non-transpose) solve, and corresponds to PLDP’ on backward (transpose) solve (D=I for Chokesky).
- **`SparseSubfactorQ`**: Q factor subfactor, valid for QR only. Column permutation, valid for LU only.
- **`SparseSubfactorR`**: R factor subfactor, valid for QR and CholeskyAtA only.
- **`SparseSubfactorRP`**: Half-solve subfactor, valid for QR and CholeskyAtA only.
- **`SparseSubfactorSr`**: Diagonal row scaling subfactor, valid for LU only.
- **`SparseSubfactorSc`**: Diagonal column scaling subfactor, valid for LU only.

## See Also

- [var SparseSubfactorInvalid: SparseSubfactor_t](sparsesubfactorinvalid.md)
  An invalid subfactor that indicates the requested type is incompatible with the supplied factorization or the system has destroyed it.
- [var SparseSubfactorP: SparseSubfactor_t](sparsesubfactorp.md)
  A permutation subfactor that’s valid for all factorization types.
- [var SparseSubfactorS: SparseSubfactor_t](sparsesubfactors.md)
  A diagonal scaling subfactor that’s valid for Cholesky and *LDLᵀ* only.
- [var SparseSubfactorL: SparseSubfactor_t](sparsesubfactorl.md)
  An *L* factor subfactor that’s valid for Cholesky and *LDLᵀ* only.
- [var SparseSubfactorD: SparseSubfactor_t](sparsesubfactord.md)
  A *D* factor subfactor that’s valid for *LDLᵀ*` `only.
- [var SparseSubfactorPLPS: SparseSubfactor_t](sparsesubfactorplps.md)
  A half-solve subfactor that’s valid for Cholesky and *LDLᵀ* only.
- [var SparseSubfactorQ: SparseSubfactor_t](sparsesubfactorq.md)
  A *Q* factor subfactor that’s valid for QR only.
- [var SparseSubfactorR: SparseSubfactor_t](sparsesubfactorr.md)
  An *R* factor subfactor that’s valid for QR and Cholesky *AᵀA* only.
- [var SparseSubfactorRP: SparseSubfactor_t](sparsesubfactorrp.md)
  A half-solve subfactor that’s valid for QR and Cholesky *AᵀA* only.
- [var SparseSubfactorSr: SparseSubfactor_t](sparsesubfactorsr.md)
  Types of sub-factor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesubfactorsc)*
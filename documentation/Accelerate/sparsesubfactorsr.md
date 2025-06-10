# SparseSubfactorSr

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
var SparseSubfactorSr: SparseSubfactor_t { get }
```

#### Discussion

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesubfactorsr)*
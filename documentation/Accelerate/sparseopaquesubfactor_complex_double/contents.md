# contents

**Framework**: Accelerate  
**Kind**: property

Types of sub-factor object.

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
var contents: SparseSubfactor_t
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_complex_double/contents)*
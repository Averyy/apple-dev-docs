# symbolicFactorization

**Framework**: Accelerate  
**Kind**: property

The symbolic factorization that this numeric factorization depends on.

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
var symbolicFactorization: SparseOpaqueSymbolicFactorization
```

## See Also

- [var attributes: SparseAttributes_t](sparseopaquefactorization_float/attributes.md)
  The attributes of a factorization object.
- [var numericFactorization: UnsafeMutableRawPointer?](sparseopaquefactorization_float/numericfactorization.md)
  The pointer to a private internal representation of a numeric factor.
- [var solveWorkspaceRequiredPerRHS: Int](sparseopaquefactorization_float/solveworkspacerequiredperrhs.md)
  The required size of the per-right-hand-side workspace for a call to a sparse solve function.
- [var solveWorkspaceRequiredStatic: Int](sparseopaquefactorization_float/solveworkspacerequiredstatic.md)
  The required size of the static workspace for a call to a sparse solve function.
- [var status: SparseStatus_t](sparseopaquefactorization_float/status.md)
  The status of the factorization object.
- [var userFactorStorage: Bool](sparseopaquefactorization_float/userfactorstorage.md)
  A Boolean value that indicates whether user-provided storage backs this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_float/symbolicfactorization)*
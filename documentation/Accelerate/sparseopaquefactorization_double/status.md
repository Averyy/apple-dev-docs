# status

**Framework**: Accelerate  
**Kind**: property

The status of the factorization object.

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
var status: SparseStatus_t
```

## See Also

- [var attributes: SparseAttributes_t](sparseopaquefactorization_double/attributes.md)
  The attributes of a factorization object.
- [var numericFactorization: UnsafeMutableRawPointer?](sparseopaquefactorization_double/numericfactorization.md)
  The pointer to a private internal representation of a numeric factor.
- [var solveWorkspaceRequiredPerRHS: Int](sparseopaquefactorization_double/solveworkspacerequiredperrhs.md)
  The required size of the per-right-hand-side workspace for a call to a sparse solve function.
- [var solveWorkspaceRequiredStatic: Int](sparseopaquefactorization_double/solveworkspacerequiredstatic.md)
  The required size of the static workspace for a call to a sparse solve function.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](sparseopaquefactorization_double/symbolicfactorization.md)
  The symbolic factorization that this numeric factorization depends on.
- [var userFactorStorage: Bool](sparseopaquefactorization_double/userfactorstorage.md)
  A Boolean value that indicates whether user-provided storage backs this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_double/status)*
# userFactorStorage

**Framework**: Accelerate  
**Kind**: property

A Boolean value that indicates whether user-provided storage backs this object.

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
var userFactorStorage: Bool
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the user must free factor storage after all references finish (though [`SparseCleanup(_:)`](sparsecleanup(_:)-3cnxt.md) still frees any additional allocated storage due to pivoting).

## See Also

- [var attributes: SparseAttributes_t](sparseopaquefactorization_double/attributes.md)
  The attributes of a factorization object.
- [var numericFactorization: UnsafeMutableRawPointer?](sparseopaquefactorization_double/numericfactorization.md)
  The pointer to a private internal representation of a numeric factor.
- [var solveWorkspaceRequiredPerRHS: Int](sparseopaquefactorization_double/solveworkspacerequiredperrhs.md)
  The required size of the per-right-hand-side workspace for a call to a sparse solve function.
- [var solveWorkspaceRequiredStatic: Int](sparseopaquefactorization_double/solveworkspacerequiredstatic.md)
  The required size of the static workspace for a call to a sparse solve function.
- [var status: SparseStatus_t](sparseopaquefactorization_double/status.md)
  The status of the factorization object.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](sparseopaquefactorization_double/symbolicfactorization.md)
  The symbolic factorization that this numeric factorization depends on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_double/userfactorstorage)*
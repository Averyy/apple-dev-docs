# solveWorkspaceRequiredStatic

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The required size of the static workspace for a call to a sparse solve function.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var solveWorkspaceRequiredStatic: Int
```

```c
size_t solveWorkspaceRequiredStatic;
```

## Discussion

The required size of workspace in bytes for a call to a sparse solve function is [`solveWorkspaceRequiredStatic`](./solveworkspacerequiredstatic.md) `+ nrhs *` [`solveWorkspaceRequiredPerRHS`](./solveworkspacerequiredperrhs.md) where `nrhs` is the number of right-hand-side vectors.

## See Also

### Instance Properties
- [var attributes: SparseAttributes_t](./attributes.md)
  The attributes of a factorization object.
- [var numericFactorization: UnsafeMutableRawPointer?](./numericfactorization.md)
  The pointer to a private internal representation of a numeric factor.
- [var solveWorkspaceRequiredPerRHS: Int](./solveworkspacerequiredperrhs.md)
  The required size of the per-right-hand-side workspace for a call to a sparse solve function.
- [var status: SparseStatus_t](./status.md)
  The status of the factorization object.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](./symbolicfactorization.md)
  The symbolic factorization that this numeric factorization depends on.
- [var userFactorStorage: Bool](./userfactorstorage.md)
  A Boolean value that indicates whether user-provided storage backs this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_double/solveworkspacerequiredstatic)*
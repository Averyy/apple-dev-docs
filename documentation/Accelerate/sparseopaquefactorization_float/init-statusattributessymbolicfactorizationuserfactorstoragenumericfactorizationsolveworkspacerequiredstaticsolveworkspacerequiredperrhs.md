# init(status:attributes:symbolicFactorization:userFactorStorage:numericFactorization:solveWorkspaceRequiredStatic:solveWorkspaceRequiredPerRHS:)

**Framework**: Accelerate  
**Kind**: init

Creates a new opaque factorization with the specified parameters.

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
init(status: SparseStatus_t, attributes: SparseAttributes_t, symbolicFactorization: SparseOpaqueSymbolicFactorization, userFactorStorage: Bool, numericFactorization: UnsafeMutableRawPointer?, solveWorkspaceRequiredStatic: Int, solveWorkspaceRequiredPerRHS: Int)
```

#### Return Value

A new opaque factorization.

## Parameters

- `status`: The status of the factorization object.
- `attributes`: The attributes of the factorization object.
- `symbolicFactorization`: The symbolic factorization that this numeric factorization depends on.
- `userFactorStorage`: A Boolean value that indicates whether user-provided storage backs this object.
- `numericFactorization`: A pointer to a private internal representation of the numeric factor.
- `solveWorkspaceRequiredStatic`: The required size of the static workspace for a call to a sparse solve function.
- `solveWorkspaceRequiredPerRHS`: The required size of the per-right-hand-side workspace for a call to a sparse solve function.

## See Also

- [init()](sparseopaquefactorization_float/init.md)
  Creates a new opaque factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_float/init(status:attributes:symbolicfactorization:userfactorstorage:numericfactorization:solveworkspacerequiredstatic:solveworkspacerequiredperrhs:))*
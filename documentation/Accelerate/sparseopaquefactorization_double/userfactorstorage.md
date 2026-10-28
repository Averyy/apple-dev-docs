# userFactorStorage

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether user-provided storage backs this object.

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
var userFactorStorage: Bool
```

```c
bool userFactorStorage;
```

## Discussion

If [`true`](../../Swift/true.md), the user must free factor storage after all references finish (though [`SparseCleanup(_:)`](../sparsecleanup%28_%29-3cnxt.md) still frees any additional allocated storage due to pivoting).

## See Also

### Instance Properties
- [var attributes: SparseAttributes_t](./attributes.md)
  The attributes of a factorization object.
- [var numericFactorization: UnsafeMutableRawPointer?](./numericfactorization.md)
  The pointer to a private internal representation of a numeric factor.
- [var solveWorkspaceRequiredPerRHS: Int](./solveworkspacerequiredperrhs.md)
  The required size of the per-right-hand-side workspace for a call to a sparse solve function.
- [var solveWorkspaceRequiredStatic: Int](./solveworkspacerequiredstatic.md)
  The required size of the static workspace for a call to a sparse solve function.
- [var status: SparseStatus_t](./status.md)
  The status of the factorization object.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](./symbolicfactorization.md)
  The symbolic factorization that this numeric factorization depends on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_double/userfactorstorage)*
# attributes

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The attributes of a factorization object.

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
var attributes: SparseAttributes_t
```

```c
SparseAttributes_t attributes;
```

#### Discussion

In particular, the [`transpose`](../sparseattributes_t/transpose.md) field indicates whether the object is a factorization of *A* or *A__ᵀ*.

## See Also

### Instance Properties
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
- [var userFactorStorage: Bool](./userfactorstorage.md)
  A Boolean value that indicates whether user-provided storage backs this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_double/attributes)*
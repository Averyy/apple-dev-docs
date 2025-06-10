# SparseUpdateFactor(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Apply a low-rank update to an existing factorization of a matrix of complex double values.

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
func SparseUpdateFactor(_ updateAlgorithm: SparseUpdate_t, _ Factorization: UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, _ updateCount: Int32, _ updatedIndices: UnsafePointer<Int32>, _ Update: SparseMatrix_Complex_Double)
```

#### Discussion

If we have a factorization `A = LU` and now wish to solve a system `ĀX = B` where `Ā = A + UV^T` for some low-rank update matrices `U` of size `m x k` and `V` of size `k x n` for some small `k` there exist methods to modify (update) the original factors at a lower cost than a full factorization.

Supported techniques are:

- `SparseUpdatePartialRefactor`: The most stable, but most expensive, method is to perform a partial refactorization that will recalculate the L and U factor values that would be different if performing an LU factorization from scratch. For the partial refactorization, `updatedIndices` should be a list of `updateCount` (row, column) pairs indicating modified values (i.e. a total of `2*updateCount` integers), and `Update` should be a full copy of the original matrix with those value modified to their new values. The structure of `Update` must be identical to that of the original matrix.

## Parameters

- `updateAlgorithm`: The update algorithm to use
- `Factorization`: The existing factorization to be updated. The existing factorization will   be modified and will no longer solve  .
- `updateCount`: Number of updated entries or columns
- `updatedIndices`: List of updated indices, interpreted as described above
- `Update`: The updated entries.

## See Also

- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, Int32, UnsafePointer<Int32>, SparseMatrix_Complex_Float)](sparseupdatefactor(_:_:_:_:_:)-1n2be.md)
  Apply a low-rank update to an existing factorization of a matrix of complex float values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, Int32, UnsafePointer<Int32>, SparseMatrix_Float)](sparseupdatefactor(_:_:_:_:_:)-9qg54.md)
  Apply a low-rank update to an existing factorization of a matrix of float values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, Int32, UnsafePointer<Int32>, SparseMatrix_Double)](sparseupdatefactor(_:_:_:_:_:)-wrqg.md)
  Apply a low-rank update to an existing factorization of a matrix of double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseupdatefactor(_:_:_:_:_:)-9h956)*
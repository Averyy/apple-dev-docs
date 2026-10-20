# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ B: DenseMatrix_Complex_Float, _ X: DenseMatrix_Complex_Float, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseSolve(SparseOpaqueSubfactor_Complex_Float Subfactor, DenseMatrix_Complex_Float B, DenseMatrix_Complex_Float X, void *workspace);
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by `SparseCreateSubfactor()`.
- `B`: (Input) The right-hand sides `B`. If `Subfactor` is `m x n`, then `B` must have dimension `m x nrhs`, where `nrhs` is the number of right-hand sides.
- `X`: (Output) The solutions `X`. If `Subfactor` is `m x n`, and `B` is `m x nrhs`, then `X` must have dimension `n x nrhs`.
- `workspace`: (Scratch) A workspace of size `Subfactor.workspaceRequiredStatic + nrhs * Subfactor.workspaceRequiredPerRHS * 2`. This memory must be 16-byte aligned (any allocation returned by `malloc()` has this property).

## See Also

### Complex subfactor-solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](./sparsesolve%28_,_%29-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](./sparsesolve%28_,_%29-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](./sparsesolve%28_,_%29-78cl0.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](./sparsesolve%28_,_%29-879na.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-5stp5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-9ui81.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-9xxqn.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-6afcf)*
# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the equation *Subfactor * X = B* in place for the matrix of single-precision values *X*, without any internal memory allocations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Float, _ XB: DenseMatrix_Float, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseSolve(SparseOpaqueSubfactor_Float Subfactor, DenseMatrix_Float XB, void *workspace);
```

## Parameters

- `Subfactor`: The *Subfactor* in *Subfactor* ** X = B* that [`SparseCreateSubfactor(_:_:)`](./sparsecreatesubfactor%28_,_%29-4renf.md) returns.
- `XB`: On input, the matrix *B*. On return, the matrix *X* overwrites it.
- `workspace`: A workspace of size `workspaceRequiredStatic` `+ nrhs *` `workspaceRequiredPerRHS` where `nrhs` is the number of right-hand-side vectors.

## See Also

### Matrix-solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-8k0w9.md)
  Solves the equation *Subfactor * X = B* in place for the matrix of double-precision values *X*, without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-90z8f.md)
  Solves the equation *Subfactor * X = B* for the matrix of double-precision values *X*, without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-1hhdi.md)
  Solves the equation *Subfactor * X = B* for the matrix of single-precision values *X*, without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-9kp2g)*
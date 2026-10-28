# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Perform the multiply operation `Y = Subfactor * X `for complex double values, in place.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ XY: DenseMatrix_Complex_Double, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseMultiply(SparseOpaqueSubfactor_Complex_Double Subfactor, DenseMatrix_Complex_Double XY, void *workspace);
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by `SparseCreateSubfactor()`.
- `XY`: (Input/Output) On input, the matrix `X`. On return it is overwritten with the matrix `Y`. If `Subfactor` is `m x n`, then `XB` must have dimension `k x nrhs`, where `k = max(m, n)` and `nrhs` is the number of right-hand side vectors. If `m != n`, then only the first `min(m,n)` entries are used for input or output as approriate.
- `workspace`: (Scratch) A workspace of size `Subfactor.workspaceRequiredStatic + nrhs * Subfactor.workspaceRequiredPerRHS * 2`. This memory must be 16-byte aligned (any allocation returned by `malloc()` has this property).

## See Also

### Subfactor and dense matrix multiplication with user-defined workspace
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-20xvs.md)
  Performs the multiply operation *Y* *= Subfactor \* X*, in place on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-6thvw.md)
  Performs the multiply operation *Y* *= Subfactor \* X*, in place on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-2osop.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-9v8hk.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-6strd.md)
  Perform the multiply operation `Y = Subfactor * X `for complex float values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-581zl.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-7mdi8)*
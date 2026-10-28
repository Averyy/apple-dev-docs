# SparseMultiply(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Perform the multiply operation `Y = Subfactor * X` for complex double values.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ X: DenseMatrix_Complex_Double, _ Y: DenseMatrix_Complex_Double, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseMultiply(SparseOpaqueSubfactor_Complex_Double Subfactor, DenseMatrix_Complex_Double X, DenseMatrix_Complex_Double Y, void *workspace);
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by `SparseCreateSubfactor()`.
- `X`: (Input) The right-hand side vectors `X`. If `Subfactor` is `m x n`, then `X` must have dimension `n x nrhs`, where nrhs is the number of right-hand side vectors.
- `Y`: (Output) The result vectors `Y`. If `Subfactor` is `m x n`, and `X` is `m x nrhs`, then `Y` must have dimension `m x nrhs`.
- `workspace`: (Scratch) A workspace of size `Subfactor.workspaceRequiredStatic + nrhs * Subfactor.workspaceRequiredPerRHS * 2`. This memory must be 16-byte aligned (any allocation returned by `malloc()` has this property).

## See Also

### Subfactor and dense vector multiplication with user-defined workspace
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-9tahm.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values *X*, in place and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-4u1y3.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of single-precision values *X*, in place and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-1ooyi.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values *X*, without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-3l60d.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values *X*, without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-5etjg.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-5kh07.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-4xr8.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-7xipz.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:_:)-9v0nu)*
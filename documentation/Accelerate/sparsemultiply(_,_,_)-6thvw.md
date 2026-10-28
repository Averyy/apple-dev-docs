# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiply operation *Y* *= Subfactor \* X*, in place on a dense matrix of single-precision values and without any internal memory allocations.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Float, _ XY: DenseMatrix_Float, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseMultiply(SparseOpaqueSubfactor_Float Subfactor, DenseMatrix_Float XY, void *workspace);
```

## Parameters

- `Subfactor`: The subfactor to multiply by, which [`SparseCreateSubfactor(_:_:)`](./sparsecreatesubfactor%28_,_%29-4renf.md) returns.
- `XY`: On input, the matrix *X*. On return, the matrix *Y* overwrites it.
- `workspace`: A workspace of size `workspaceRequiredStatic` `+ nrhs *` `workspaceRequiredPerRHS` where `nrhs` is the number of right-hand-side vectors.

## See Also

### Subfactor and dense matrix multiplication with user-defined workspace
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-20xvs.md)
  Performs the multiply operation *Y* *= Subfactor \* X*, in place on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-2osop.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-9v8hk.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-6strd.md)
  Perform the multiply operation `Y = Subfactor * X `for complex float values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-7mdi8.md)
  Perform the multiply operation `Y = Subfactor * X `for complex double values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-581zl.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-6thvw)*
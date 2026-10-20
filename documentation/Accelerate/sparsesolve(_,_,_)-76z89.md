# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the equation *Subfactor * X = B* for the matrix of single-precision values *X*.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Float, _ B: DenseMatrix_Float, _ X: DenseMatrix_Float)
```

```c
static void SparseSolve(SparseOpaqueSubfactor_Float Subfactor, DenseMatrix_Float B, DenseMatrix_Float X);
```

## Parameters

- `Subfactor`: The *Subfactor* in *Subfactor* ** X = B* that [`SparseCreateSubfactor(_:_:)`](./sparsecreatesubfactor%28_,_%29-4renf.md) returns.
- `B`: The matrix *B*.
- `X`: The matrix *X*.

## See Also

### Matrix-solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double)](./sparsesolve%28_,_%29-2oyl1.md)
  Solves the equation *Subfactor * X = B* in place for the matrix of double-precision values *X*.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](./sparsesolve%28_,_%29-2tyws.md)
  Solves the equation *Subfactor * X = B* in place for the matrix of single-precision values *X*.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsesolve%28_,_,_%29-1lads.md)
  Solves the equation *Subfactor * X = B* for the matrix of double-precision values *X*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-76z89)*
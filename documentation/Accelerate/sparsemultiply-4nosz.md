# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation   on a dense matrix of double-precision values.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Double, _ X: DenseMatrix_Double, _ Y: DenseMatrix_Double)
```

## Parameters

- `Subfactor`: The subfactor to multiply by, which   returns.
- `X`: The matrix  .
- `Y`: The matrix  .

## See Also

- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double)](sparsemultiply(_:_:)-88trz.md)
  Performs the multiply operation   __in place on a dense matrix of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](sparsemultiply(_:_:)-3r4mf.md)
  Performs the multiply operation _ _, in place on a dense matrix of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiply(_:_:_:)-88stx.md)
  Performs the multiply operation   on a dense matrix of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:)-34fp6.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:)-3dwed.md)
  Perform the multiply operation `y = Subfactor * x` for complex floatr values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:_:)-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiply(_:_:_:)-7q8gs.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-4nosz)*
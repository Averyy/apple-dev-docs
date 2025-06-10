# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Perform the multiply operation `y = Subfactor * x` for complex double values..

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ X: DenseVector_Complex_Double, _ Y: DenseVector_Complex_Double)
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by   .

## See Also

- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double)](sparsemultiply(_:_:)-8ehhn.md)
  Performs the multiply operation , in place on a vector of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float)](sparsemultiply(_:_:)-7l3sr.md)
  Performs the multiply operation , in place on a vector of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double)](sparsemultiply(_:_:_:)-6abql.md)
  Performs the multiply operation  on a vector of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float)](sparsemultiply(_:_:_:)-2h425.md)
  Performs the multiply operation   on a vector of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiply(_:_:)-3s0hu.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](sparsemultiply(_:_:)-9fn7j.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:_:)-58wuo.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:_:)-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-4fwfv)*
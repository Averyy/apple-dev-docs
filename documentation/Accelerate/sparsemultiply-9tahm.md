# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation  on a vector of double-precision values , in place and without any internal memory allocations.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Double, _ XY: DenseVector_Double, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: The subfactor to multiply by, which   returns.
- `XY`: On input, the vector  . On return, the vector   overwrites it.
- `workspace`: A workspace of size      .

## See Also

- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-4u1y3.md)
  Performs the multiply operation  on a vector of single-precision values , in place and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-1ooyi.md)
  Performs the multiply operation  on a vector of double-precision values , without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-3l60d.md)
  Performs the multiply operation  on a vector of double-precision values , without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-5etjg.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-5kh07.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-4xr8.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-7xipz.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-9v0nu.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-9tahm)*
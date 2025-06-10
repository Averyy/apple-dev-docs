# SparseMultiply(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Perform the multiply operation `y = Subfactor * x` for complex double values.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ X: DenseVector_Complex_Double, _ Y: DenseVector_Complex_Double, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by   .
- `workspace`: (Scratch) A workspace of size   .   This memory must be 16-byte aligned (any allocation returned   by   has this property).

## See Also

- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-9tahm.md)
  Performs the multiply operation  on a vector of double-precision values , in place and without any internal memory allocations.
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
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-9v0nu.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:_:)-7xipz)*
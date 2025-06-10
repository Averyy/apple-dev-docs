# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by   .
- `XY`: (Input/Output) On input, the matrix  . On return it is overwritten   with the matrix  . If   is  , then   must have dimension   , where   and   is the number of right-hand   side vectors. If  , then only the first   entries are   used for input or output as approriate.
- `workspace`: (Scratch) A workspace of size   .   This memory must be 16-byte aligned (any allocation returned   by   has this property).

## See Also

- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-20xvs.md)
  Performs the multiply operation  , in place on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-6thvw.md)
  Performs the multiply operation  , in place on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-2osop.md)
  Performs the multiply operation   on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-9v8hk.md)
  Performs the multiply operation   on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:)-6strd.md)
  Perform the multiply operation `Y = Subfactor * X `for complex float values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsemultiply(_:_:_:_:)-581zl.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-7mdi8)*
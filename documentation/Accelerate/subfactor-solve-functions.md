# Subfactor Solve Functions

**Framework**: Accelerate

Solve systems with the equation .

## Topics

### Matrix-solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double)](sparsesolve(_:_:)-2oyl1.md)
  Solves the equation  in place for the matrix of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](sparsesolve(_:_:)-2tyws.md)
  Solves the equation  in place for the matrix of single-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsesolve(_:_:_:)-1lads.md)
  Solves the equation  for the matrix of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsesolve(_:_:_:)-76z89.md)
  Solves the equation  for the matrix of single-precision values .
### Matrix-solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-8k0w9.md)
  Solves the equation  in place for the matrix of double-precision values , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-9kp2g.md)
  Solves the equation  in place for the matrix of single-precision values , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-90z8f.md)
  Solves the equation  for the matrix of double-precision values , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-1hhdi.md)
  Solves the equation  for the matrix of single-precision values , without any internal memory allocations.
### Vector-solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double)](sparsesolve(_:_:)-87v8w.md)
  Solves the equation  in place for the vector of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float)](sparsesolve(_:_:)-6pxrq.md)
  Solves the equation  in place for the vector of single-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double)](sparsesolve(_:_:_:)-g0wb.md)
  Solves the equation  in place for the vector of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float)](sparsesolve(_:_:_:)-5mq7s.md)
  Solves the equation  in place for the vector of single-precision values .
### Vector-solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-7auge.md)
  Solves the equation  for the vector of double-precision values , in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-1xw9b.md)
  Solves the equation  for the vector of single-precision values , in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-eaq9.md)
  Solves the equation  for the vector of double-precision values , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-2p6e3.md)
  Solves the equation  for the vector of single-precision values , without any internal memory allocations.
### Complex subfactor-solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:)-78cl0.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:)-879na.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-5stp5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6afcf.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-9ui81.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-9xxqn.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values.

## See Also

- [Subfactor Multiplication Functions](subfactor-multiplication-functions.md)
  Multiply subfactors by matrices and vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/subfactor-solve-functions)*
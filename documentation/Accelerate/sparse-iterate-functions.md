# Sparse Iterate Functions

**Framework**: Accelerate

Perform a single iteration of the specified iterative method.

## Topics

### Sparse Iterate Functions
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparseiterate(_:_:_:_:_:_:_:_:)-c54n.md)
  Performs a single iteration of the specified iterative method for double-precision matrices.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparseiterate(_:_:_:_:_:_:_:_:)-1el7r.md)
  Performs a single iteration of the specified iterative method for single-precision matrices.
### Sparse Iterate Functions with Preconditioner
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double, SparseOpaquePreconditioner_Double)](sparseiterate(_:_:_:_:_:_:_:_:_:)-99ji7.md)
  Performs a single iteration of the specified iterative method for double-precision matrices, applying a preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float)](sparseiterate(_:_:_:_:_:_:_:_:_:)-1anay.md)
  Performs a single iteration of the specified iterative method for single-precision matrices, applying a preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparseiterate(_:_:_:_:_:_:_:_:)-315ym.md)
  Perform a single iteration of the specified iterative method for complex double values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparseiterate(_:_:_:_:_:_:_:_:)-9v7qh.md)
  Perform a single iteration of the specified iterative method for complex float values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double)](sparseiterate(_:_:_:_:_:_:_:_:_:)-1wv28.md)
  Perform a single iteration of the specified iterative method for complex double values with preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float)](sparseiterate(_:_:_:_:_:_:_:_:_:)-4td1l.md)
  Perform a single iteration of the specified iterative method for complex float values with preconditioner.
### Functions that Calculate Iterate State Size
- [func SparseGetStateSize_Double(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_double(_:_:_:_:_:).md)
  Returns the size in bytes necessary for a call to the double-precision sparse iterate method.
- [func SparseGetStateSize_Float(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_float(_:_:_:_:_:).md)
  Returns the size in bytes necessary for a call to the single-precision sparse iterate method.
- [func SparseGetStateSize_Complex_Double(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_double(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex double values.
- [func SparseGetStateSize_Complex_Float(SparseIterativeMethod, Bool, Int32, Int32, Int32) -> Int](sparsegetstatesize_complex_float(_:_:_:_:_:).md)
  Returns size in bytes of state space required for call to `SparseIterate()` for complex float values.

## See Also

- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Sparse Iterative Solving Functions (Matrix RHS)](sparse-iterative-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using iterative methods.
- [Sparse Iterative Solving Functions (Vector RHS)](sparse-iterative-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using iterative methods.
- [Sparse Iterative Methods](sparse-iterative-methods.md)
  Select a suitable iterative method to solve a system.
- [Preconditioners](preconditioners.md)
  Create preconditioners for iterative solves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-iterate-functions)*
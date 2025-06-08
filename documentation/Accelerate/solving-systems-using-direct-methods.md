# Solving systems using direct methods

**Framework**: Accelerate

Use direct methods to solve systems of equations where the coefficient matrix is sparse.

#### Overview

Direct methods offer high-precision solving with a simple API when compared to iterative methods. The code example below uses sparse Cholesky factorization to solve the following equation:

![A mathematical equation that consists of a four-by-four sparse matrix multiplied by a four-element vector of unknown values equals a four-element vector of known values.](https://docs-assets.developer.apple.com/published/2c13eba9c0f47ff54e7774d087efc9f1/media-2904628%402x.png)

In the equation above,  refers to the four-by-four coefficient matrix and  to the right-hand-side vector. The code in this article solves the equation  by finding .

Note that  is sparse. Some entries (those that are blank) are zero. For small matrices such as this, there’s little gain in exploiting this structure. However, it’s essential for larger systems that don’t otherwise fit in memory, even on a large computer.

The code in this article performs a sparse Cholesky factorization, equivalent to calling the LAPACK function `dpotrf_(_:_:_:_:_:)` on a dense matrix. The main requirement for sparse Cholesky factorization is that the matrix is symmetric positive-definite (that is,  and all eigenvalues are greater than zero. A sufficient, but not necessary, condition is that the matrix is diagonally dominant (that is, the sum of the absolute values of the off-diagonal entries in each row or column is less than the value of the diagonal). This is the case for the above matrix.

##### Create the Matrix Structure

Use the code below to define the matrix structure. As [`Creating sparse matrices`](creating-sparse-matrices.md) explains, because  is symmetric, it stores only half of the data.

##### Create and Factorize the Matrix

The [`SparseFactor(_:_:)`](sparsefactor(_:_:)-8gl6j.md) function performs the actual Cholesky factorization, finding  such that .

If the factorization function encounters an error, the code prints an error message and terminates. You may instead want to capture the error by using the optional [`SparseSymbolicFactorOptions`](sparsesymbolicfactoroptions.md) parameter and set the [`reportError`](sparsesymbolicfactoroptions/reporterror.md) parameter to a user-supplied error-handling routine. The returned [`SparseOpaqueFactorization_Double`](sparseopaquefactorization_double.md) structure reflects the error.

##### Solve the Equation

Use the factorization to solve the equation. The right-hand-side and solution vectors are arrays that you wrap in [`DenseVector_Double`](densevector_double.md) structures. The actual values of `x` don’t matter because the function overwrites them.

The solve call takes the factorization  and solves the system  as  by solving the two triangular systems:

However, you need only to supply the right-hand-side vector and the factorization.

The [`SparseSolve(_:_:_:)`](sparsesolve(_:_:_:)-416bj.md) function solves the equation and populates `x` with the solution.

If the [`SparseSolve(_:_:_:)`](sparsesolve(_:_:_:)-416bj.md) function encounters an error, the code prints an error message and terminates, unless you set [`reportError`](sparsesymbolicfactoroptions/reporterror.md) on the initial call to [`SparseFactor(_:_:)`](sparsefactor(_:_:)-8gl6j.md).

The following code iterates over the solution vector, `x`, and prints the solution, `x = 0.10 0.20 0.30 0.40`.

## See Also

- [Creating sparse matrices](creating-sparse-matrices.md)
  Create sparse matrices for factorization and solving systems.
- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)
  Use separate coordinate format arrays to create sparse matrices.
- [Sparse Solvers](sparse-solvers-library.md)
  Solve systems of equations where the coefficient matrix is sparse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/solving-systems-using-direct-methods)*
# Solving systems of linear equations with LAPACK

**Framework**: Accelerate

Select the optimal LAPACK routine to solve a system of linear equations.

**Availability**:
- macOS 13.3+
- Xcode 15.0+

#### Overview

The Accelerate framework provides the LAPACK library for numerical linear algebra. A basic technique of linear algebra is to solve systems of simultaneous equations. For example, the following shows three equations that contain the unknowns , , and :

![Set of three simultaneous equations.](https://docs-assets.developer.apple.com/published/1c138a77e2929a2876e51b74728891dd/simultaneous-equations_2x.png)

You can solve this system by rewriting the simultaneous equations as a matrix equation with the following form:

![Mathematical formula that describes the matrix equation, A x equals b. A three-by-three matrix multiplied by a three-element column matrix equals a three-element column matrix.](https://docs-assets.developer.apple.com/published/db8e672916663cd9c5c5caaf6837e83f/simulataneous-ax%3Db_2x.png)

This form is an  form, where  is the coefficient matrix,  is a column vector that contains the unknown values, and  is a column vector that contains the constant values. The number of elements in  is equal to the number of columns of , and the number of elements in  is equal to the number of rows of .

The process of solving this system computes the values for , , and  as `-2`, `24`, and `8`, respectively.

![Mathematical formula that describes the matrix equation, A x equals b with the computed unknowns on the left, and the same system as a set of simultaneous equations on the right.](https://docs-assets.developer.apple.com/published/69300343f1dc42dcd7acfcfc706d8fcf/simultaneous-solution_2x.png)

For an example of solving a linear system, see [`Finding an interpolating polynomial using the Vandermonde method`](finding-an-interpolating-polynomial-using-the-vandermonde-method.md).

LAPACK includes routines for solving systems of linear equations as . This sample code project includes wrapper functions that simplify calling the LAPACK routines, for example, by encapsulating multiple-step workflows into a single function call.

Run the sample code app to see the results of each routine solve different example systems.

##### Determine the Properties of the Coefficient Matrix

LAPACK provides different solving routines depending on the properties of the coefficient matrix, :

- Is the coefficient matrix ? A symmetric matrix is one that’s equal to its transpose, that is, a matrix that’s identical when swapping its row and column indices. A symmetric matrix is necessarily square. The following is an example of a symmetric matrix:

![Matrix that consists of five rows and five columns of numbers. The numbers in the first row are the same as those in the first column. The numbers in the second row are the same as in the second column, and so forth.](https://docs-assets.developer.apple.com/published/8498d08aa4d6b3a6583912b7c01af25f/symmetric_2x.png)

- Is the coefficient matrix ? A matrix is positive definite if all of its [`eigenvalues`](https://developer.apple.comhttps://mathworld.wolfram.com/Eigenvalue.html) are positive. Confirm whether a matrix is positive definite by calling `spotrf_(_:_:_:_:_:)` to try a [`Cholesky factorization`](https://developer.apple.comhttps://mathworld.wolfram.com/CholeskyDecomposition.html). If the factorization fails and returns a positive value, the matrix isn’t positive definite. This sample code project includes the function `isPositiveDefinite(_:dimension:)` to determine whether a matrix is positive definite.
- Is the coefficient matrix ? A banded matrix has all of its nonzero entries on its main diagonal and an arbitrary number of superdiagonals (above the main diagonal) and subdiagonals (below the main diagonal). The following is an example of a nonsymmetric, banded matrix with two superdiagonals and one subdiagonal:

![Matrix that consists of five rows and five columns of numbers representing a nonsymmetric, banded matrix.](https://docs-assets.developer.apple.com/published/ede7683431cd98ad48bbd5eb8dcb9b84/banded_2x.png)

- Is the coefficient matrix ? A tridiagonal matrix has all of its nonzero entries on its main diagonal, its first superdiagonal, and its first subdiagonal. The following is an example of a nonsymmetric, tridiagonal matrix:

![Matrix that consists of five rows and five columns of numbers representing a nonsymmetric, tridiagonal matrix.](https://docs-assets.developer.apple.com/published/25db5cb6bfb99506fe3be7fc15c62f1e/tridiagonal_2x.png)

If the coefficient matrix is , that is, most of the entries in the coefficient matrix are zero, Accelerate provides the [`Sparse Solvers`](sparse-solvers-library.md) library to help solve such systems.

##### Select Lapack Variants for Data Types

The LAPACK routines in this sample code project are all for real, single-precision matrices. All of the routines are available in single- and double-precision for real and complex values. The first character of a routine name defines the type of data the routine works on. For example:

- `sgels_(_:_:_:_:_:_:_:_:_:_:_:)` — single-precision, real values
- `dgels_(_:_:_:_:_:_:_:_:_:_:_:)` — double-precision, real values
- `cgels_(_:_:_:_:_:_:_:_:_:_:_:)` — single-precision, complex values
- `zgels_(_:_:_:_:_:_:_:_:_:_:_:)` — double-precision, complex values

For complex matrices, the LAPACK routine variant for real symmetric matrices requires [`Hermitian matrices`](https://developer.apple.comhttps://mathworld.wolfram.com/HermitianMatrix.html). For example, the `cptsv_()` routine computes the solution to  for a complex single-precision, Hermitian, tridiagonal coefficient matrix; and `sptsv_()`  computes the solution for a real single-precision, symmetric, tridiagonal coefficient matrix.

The routines in this sample code project are suitable for solving full rank systems, that is, they have a unique and exact solution.

##### Define Values in Column Major Layout

The LAPACK routines in this article require the matrix data in column-major layout, which means specifying all the terms in the first column, then all of the terms in the second column, the third column, and so on. For example, if there are two columns with three row values each, the routine specifies the three row values for column one, then the three row values for column two, as the following example illustrates:

![Matrix that consists of three rows and two columns of numbers. The first column has the values 80, 180, and 160. The second column has the values 800, 1800, and 1600.](https://docs-assets.developer.apple.com/published/8c68168076bb6a624cacf25e0244de25/b-matrix_2x.png)

```swift
let bValues: [Float] = [80, 180, 160,
                        800, 1800, 1600]
```

The routines return the result as column-major, for example, an array that contains `[10.0, 20.0, 30.0, 100.0, 200.0, 300.0]` represents the following matrix:

![Matrix that consists of three rows and two columns of numbers. The first column has the values 10, 20, and 30. The second column has the values 100, 200, and 300.](https://docs-assets.developer.apple.com/published/47571c2f8f2b00d47144af88680b049f/x-matrix_2x.png)

##### Select the Solving Routine for the Coefficient Matrix Type

This sample code project provides Swift wrapper functions to each single-precision LAPACK solving routine. Select the routine that most closely matches the coefficient matrix for the highest performance. The following shows the Swift wrapper functions and the underlying LAPACK routines to solve systems with different coefficient matrices:

- Symmetric - Positive definite - Tridiagonal - Swift wrapper function: `symmetric_positiveDefinite_tridiagonal()`
- Underlying LAPACK routine: `sptsv_()`
- Other banded - Swift wrapper function: `symmetric_positiveDefinite_banded()`
- Underlying LAPACK routine: `spbsv_()`
- General - Swift wrapper function: `symmetric_positiveDefinite_general()`
- Underlying LAPACK routine: `sposv_()`
- Indefinite - General - Swift wrapper function: `symmetric_indefinite_general()`
- Underlying LAPACK routine:  `ssysv_()`
- Nonsymmetric - Square - Tridiagonal - Swift wrapper function: nonsymmetric_tridiagonal()
- Underlying LAPACK routine: `sgtsv_()`
- Other banded - Swift wrapper function: `nonsymmetric_banded()`
- Underlying LAPACK routine: `sgbsv_()`
- General - Swift wrapper function: `nonsymmetric_general()`
- Underlying LAPACK routine: `sgesv_()`
- Nonsquare - QR factorization - Swift wrapper function: `nonsymmetric_nonsquare()`
- Underlying LAPACK routine: `sgels_()`
- Cholesky factorization - Swift wrapper function: `leastSquares_nonsquare()`
- Underlying LAPACK routines: `sposv_()` and `ssysv_()`

##### Solve for a Nonsquare Matrix Using Qr Factorization

A system of linear equations with a nonsquare coefficient matrix is either:

- Overdetermined — there are more equations than unknowns, that is, the coefficient matrix has more rows than columns. In this case, the system may not have a solution.
- Underdetermined — there are more unknowns than equations, that is, the coefficient matrix has more columns than rows. In this case, the system may have infinitely many solutions.

In these cases, the solution is either not exact (unless the overdetermined system is actually consistent) or not unique. In the case where LAPACK is unable to solve the system, the Swift wrapper functions return `nil`.

The Swift wrapper function `nonsymmetric_nonsquare(a:dimension:b:rightHandSideCount:)` wraps the LAPACK routine `sgels_(_:_:_:_:_:_:_:_:_:_:_:)`. This routine takes one of two approaches, depending on the system:

- When the coefficient matrix, , has more rows than columns (overdetermined), the routine minimizes the error in  by solving the least squares problem . The following image shows the graph of an overdetermined system with two unknowns and three equations.  `nonsymmetric_nonsquare(a:dimension:b:rightHandSideCount:)`  returns `[1.4615387, 0.7692307, -1.1766968]`, indicating the  in  equals  `[1.4615387, 0.7692307]`, and the sum of the residuals squared (that is, `r0² + r1² + r2²` equals `-1.1766968²`). Selecting any other point in the triangle of the three intercepts yields a larger sum of residuals squared.

![A line chart that contains three lines with the slope intercepts of y equals minus x plus 2, y equals 2 x minus 4, and y equals x plus 0. The three lines form a triangle and a marked point within the triangle represents the result of minimizing A x minus b.](https://docs-assets.developer.apple.com/published/72252210a95ac80542d30efd87939c01/accelerate-solving-systems-linear-equations-1_2x.png)

![A series of equations that show the slope intercepts as A x equals b with the constants on the right.](https://docs-assets.developer.apple.com/published/a039e3f8aa8ae0d40d3c2e551d5a9d8c/overdetermined_graph_2x.png)

- When the coefficient matrix, , has more columns than rows (underdetermined), the routine finds the smallest  that solves the equation  such that .  The following image shows the graph of , which is the set of solutions to the illustrated system. The closest point on the line to the origin is at x = -0.5, y = 0.5.

![A line chart that contains a single line with the slope intercept of y equals x plus 1, and a marked point that’s nearest to the chart origin.](https://docs-assets.developer.apple.com/published/af70e4c4158f2a05455e6ea788685ca5/accelerate-solving-systems-linear-equations-2_2x.png)

![A series of equations that show the slope intercept as A x equals b with the constants on the right.](https://docs-assets.developer.apple.com/published/cb4c316fe2cbbb2e486d9e0111c4c46f/underdetermined_graph_2x.png)

The `sgels_(_:_:_:_:_:_:_:_:_:_:_:)` routine uses [`QR factorization`](https://developer.apple.comhttps://mathworld.wolfram.com/QRDecomposition.html) for overdetermined systems, and [`LQ factorization`](https://developer.apple.comhttps://mathworld.wolfram.com/LQDecomposition.html) for underdetermined systems.

The following is an example of an underdetermined system with a coefficient matrix that’s nonsquare:

![Mathematical formula that describes the matrix equation, A x equals b. A three-by-five matrix multiplied by a five-element column matrix equals a three-element column matrix.](https://docs-assets.developer.apple.com/published/a7776fb1e351a04e88a923cee761dd60/nonsymmetric-nonsquare_2x.png)

The following code calls `nonsymmetric_nonsquare(a:dimension:b:rightHandSideCount:)` to compute the values of :

```swift
let aValues: [Float] = [1, 6, 11,
                        2, 7, 12,
                        3, 8, 13,
                        4, 9, 14,
                        5, 10, 15]

let dimension = (m: 3, n: 5)

/// The _b_ in _Ax = b_.
let bValues: [Float] = [355, 930, 1505]

/// Call `nonsymmetric_nonsquare` to compute the _x_ in _Ax = b_.
let x = nonsymmetric_nonsquare(a: aValues,
                               dimension: dimension,
                               b: bValues,
                               rightHandSideCount: 1)

/// Calculate _b_ using the computed _x_.
if let x = x {
    let b = matrixVectorMultiply(matrix: aValues,
                                 dimension: dimension,
                                 vector: x)
    
    /// Prints _b_ in _Ax = b_ using the computed _x_: `~[355, 930, 1505]`.
    print("\nnonsymmetric_nonsquare: ([355, 930, 1505]) b =", b)
}
```

##### Solve for a Nonsquare Matrix Using Cholesky Factorization

Where speed is more important than numerical accuracy, the sample code project provides an alternative to `sgels_(_:_:_:_:_:_:_:_:_:_:_:)`. The `leastSquares_nonsquare(a:dimension:b:)` function exploits the fact that the  in  equals the  in . This technique creates the square coefficient matrix  and solves with either `symmetric_positiveDefinite_general(a:dimension:b:rightHandSideCount:)` or `symmetric_indefinite_general(a:dimension:b:rightHandSideCount:)`.

The `leastSquares_nonsquare(a:dimension:b:)` function uses the same problem as   `nonsymmetric_nonsquare(a:dimension:b:rightHandSideCount:)`, but uses [`Cholesky factorization`](https://developer.apple.comhttps://mathworld.wolfram.com/CholeskyDecomposition.html) when  is positive definite.

The following is an example of an overdetermined system with a coefficient matrix that’s nonsquare:

![Mathematical formula that describes the matrix equation, A x equals b. A four-by-three matrix multiplied by a three-element column matrix equals a four-element column matrix.](https://docs-assets.developer.apple.com/published/52d10fb92472d7fd1d5a0fb1516aa0d7/leastsquares-nonsquare_2x.png)

The following code calls `leastSquares_nonsquare(a:dimension:b:)` to compute the values of :

```swift
let aValues: [Float] = [1, 4, 7, 10,
                        2, 5, 8, 11,
                        3, 6, 9, 12]
let dimension = (m: 4, n: 3)
let bValues: [Float] = [194, 455, 716, 977]

/// Call `leastSquares_nonsquare` to compute the _x_ in _Ax = b_.
let x = leastSquares_nonsquare(a: aValues,
                               dimension: dimension,
                               b: bValues)

/// Calculate _b_ using the computed _x_.
if let x = x {
    let b = matrixVectorMultiply(matrix: aValues,
                                 dimension: dimension,
                                 vector: Array(x[0..<3]))
    
    /// Prints _b_ in _Ax = b_ using the computed _x_: `~[194, 455, 716, 977]`.
    print("\nleastSquares_nonsquare: b =", b)
}
```

##### Solve for a Rank Deficient Matrix

Systems with a symmetric matrix that’s not full rank, , don’t have a single unique solution. For example, the following two multiplications contain different  matrices, but yield the same result in :

![Two stacked mathematical formulas that describe the matrix equation, A x equals b. Each formula is a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix. In both cases, matrices A and b contain the same values, but matrix x has different values.](https://docs-assets.developer.apple.com/published/c47fc65670c3f829ef110c2a4f48b5fe/symmetric-indefinite-general_2x.png)

In this case, passing matrix  to its most suitable function, `symmetric_indefinite_general(a:dimension:b:rightHandSideCount:)`, returns an error indicating that the routine can’t compute the solution.

One option to deal with rank-deficiency is to instead solve a nearby problem of full rank by adding a small epsilon value to the matrix to regularize it. The following code adds such an epsilon to diagonal elements in matrix :

```swift
var aValues: [Float] = [1, 2, 1,
                        2, 1, 2,
                        1, 2, 1]

let dimension = 3
let epsilon = sqrt(Float.ulpOfOne)
for i in 0 ..< dimension {
    aValues[i * dimension + i] += epsilon
}

let bValues: [Float] = [80, 100, 80]

/// Call `symmetric_indefinite_general` to compute the _x_ in _Ax = b_.
let x = symmetric_indefinite_general(a: aValues,
                                     dimension: dimension,
                                     b: bValues,
                                     rightHandSideCount: 1)

/// Calculate _b_ using the computed _x_.
if let x = x {
    let b = matrixVectorMultiply(matrix: aValues,
                                 dimension: (m: dimension, n: dimension),
                                 vector: x)
    
    /// Prints _b_ in _Ax = b_ using the computed _x_: `~[80, 100, 80]`.
    print("\nRank-Deficient: b =", b)
}
```

On return,  contains the values `[0.0, 20.0, 40.0]`:

![Mathematical formula that describes the matrix equation, A x equals b. A three-by-three matrix multiplied by a three-element column matrix equals a three-element column matrix.](https://docs-assets.developer.apple.com/published/887543dac14de56a68c5cbb375e750dc/symmetric-indefinite-general-2_2x.png)

## See Also

- [Finding an interpolating polynomial using the Vandermonde method](finding-an-interpolating-polynomial-using-the-vandermonde-method.md)
  Use LAPACK to solve a linear system and find an interpolating polynomial to construct new points between a series of known data points.
- [Compressing an image using linear algebra](compressing-an-image-using-linear-algebra.md)
  Reduce the storage size of an image using singular value decomposition (SVD).
- [BLAS](blas-library.md)
  Perform common linear algebra operations with Apple’s implementation of the Basic Linear Algebra Subprograms (BLAS).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/solving-systems-of-linear-equations-with-lapack)*
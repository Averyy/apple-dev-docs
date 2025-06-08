# Creating sparse matrices

**Framework**: Accelerate

Create sparse matrices for factorization and solving systems.

#### Overview

In the Accelerate framework, the Sparse Solvers library stores sparse matrices using the compressed sparse column (CSC) format. CSC stores a matrix as a series of column vectors that specify the nonzero entries as `(row-index, value)` pairs and omit the zero entries.

The Sparse Solvers library provides routines to convert matrices from other formats to CSC. For more information, see [`Conversion from Other Formats`](conversion-from-other-formats.md).

The Sparse Solvers library supports unsymmetric and symmetric sparse matrices, each of which can also be block matrices.

- An  contains either [`Double`](https://developer.apple.com/documentation/Swift/Double) or [`Float`](https://developer.apple.com/documentation/Swift/Float) values with no symmetry between its lower-left and upper-right triangles.
- A  is symmetrical along the diagonal from its upper-left to lower-right corners. In other words, a symmetric matrix is equal to its transpose ().
- A  can be either unsymmetric or symmetric, and consists of sections called blocks. The blocks along the diagonal of a symmetric block matrix must, themselves, be symmetrical.

##### Create an Unsymmetric Matrix

In this example of an unsymmetric sparse matrix, empty cells represent zeros:

![A four-by-three unsymmetric sparse matrix that has three empty cells.](https://docs-assets.developer.apple.com/published/6c926d4c19dd7fa9f223bc45a7f92bf9/media-2904623%402x.png)

The first step to create a matrix is to define two arrays that store the row indices and corresponding values.

In addition to the `(row-index, value)` pairs, create a third array that specifies where each column starts. This array requires an additional, final entry that defines the final column’s length.

In the following example, the zeroth item in the `values` array starts column 0, the third starts column 1, and the seventh starts column 2:

The two structural arrays, `rowIndices` and `columnStarts`, create a [`SparseMatrixStructure`](sparsematrixstructure.md) instance that describes the matrix’s structure. The initializer requires an attributes object, and the default parameters of a [`SparseAttributes_t`](sparseattributes_t.md) instance specify an unsymmetric matrix.

The following code uses the `structure` and `values` items to create a [`SparseMatrix_Double`](sparsematrix_double.md) instance:

##### Create a Symmetric Matrix

In this example of a symmetric sparse matrix, empty cells represent zeros:

![A four-by-four symmetric sparse matrix that has four empty cells.](https://docs-assets.developer.apple.com/published/1f91a6441c387c4dea8abe1dcb9b98c6/media-2904624%402x.png)

Because it’s symmetric, the values in the upper triangle of the matrix are redundant, so exclude them from the data that you pass to the [`SparseMatrix_Double`](sparsematrix_double.md) initializer.  The example below shows the excluded values in gray:

![A four-by-four symmetric sparse matrix that has four empty cells and four values that appear in a lighter color](https://docs-assets.developer.apple.com/published/45b572fb419aff0d83548d95df749ffb/media-2904626%402x.png)

As with the unsymmetric example, the `rowIndices` array specifies the row in the matrix that contains the corresponding item in `values`, and the `columnStarts` array specifies where each column starts in the `rowIndices` array.

In the following example, the [`attributes`](sparsematrixstructure/attributes.md) parameter specifies that the matrix is symmetric and the items in the values array derive from the lower triangle:

Create the [`SparseMatrix_Double`](sparsematrix_double.md) instance using the structure from the code example above and the values from the lower triangle of the matrix.

##### Create a Block Matrix

You can create block sparse matrices  that is, a matrix that consists of blocks that contain multiple values — by defining a [`blockSize`](sparsematrixstructure/blocksize.md) greater than 1. The block size is the length of the side of the square block.

Block matrices can be symmetric or unsymmetric. This example shows an unsymmetric sparse matrix with a block size of 3:

![A nine-by-nine unsymmetric sparse matrix that has three rows of three blocks each.](https://docs-assets.developer.apple.com/published/86cb9416846dc85258d052af8904517a/media-2904625%402x.png)

The following example shows the code to create a sparse matrix with the structure and values above. The [`SparseMatrixStructure`](sparsematrixstructure.md) specifies a block size of 3. The values for each block concatenate in column-major order.

When you create a symmetric matrix with a block size greater than 1, the blocks along the matrix’s diagonal must also be symmetric.

## See Also

- [Solving systems using direct methods](solving-systems-using-direct-methods.md)
  Use direct methods to solve systems of equations where the coefficient matrix is sparse.
- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)
  Use separate coordinate format arrays to create sparse matrices.
- [Sparse Solvers](sparse-solvers-library.md)
  Solve systems of equations where the coefficient matrix is sparse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/creating-sparse-matrices)*
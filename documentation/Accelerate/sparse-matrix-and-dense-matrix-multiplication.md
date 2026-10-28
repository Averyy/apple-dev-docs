# Sparse Matrix and Dense Matrix Multiplication

**Framework**: Accelerate  
**Role**: API Collection

Multiply sparse and dense matrices.

## Topics

### Multiplication functions
- [func SparseMultiply(SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiply%28_,_,_%29-8d9lh.md)
  Performs the multiply operation *Y* *= AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiply(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiply%28_,_,_%29-9kraw.md)
  Performs the multiply operation *Y* *= AX*_ _on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiply(Double, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiply%28_,_,_,_%29-73ruq.md)
  Performs the multiply operation *Y = alpha \* AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiply(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiply%28_,_,_,_%29-2qh3a.md)
  Performs the multiply operation *Y = alpha \* AX* on a sparse matrix of single-precision, floating-point values.
### Complex multiplication functions
- [func SparseMultiply(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiply%28_,_,_%29-1sjuk.md)
  Performs the multiplication `Y = AX` for complex double values.
- [func SparseMultiply(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_,_%29-85a24.md)
  Performs the multiplication `Y = AX` for complex float values.
- [SparseMultiply](./sparsemultiply-5bf3v.md)
  Performs the multiplication `Y = alpha * AX` for complex float values
- [SparseMultiply](./sparsemultiply-65jst.md)
  Performs the multiplication `Y = alpha * AX` for complex double values
### Multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiplyadd%28_,_,_%29-lgm5.md)
  Performs the multiply operation *Y += AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiplyadd%28_,_,_%29-8pgpq.md)
  Performs the multiply operation *Y += AX* on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiplyAdd(Double, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiplyadd%28_,_,_,_%29-86gfz.md)
  Performs the multiply operation *Y += alpha \* AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiplyadd%28_,_,_,_%29-n61k.md)
  Performs the multiply operation *Y += alpha \* AX* on a sparse matrix of single-precision, floating-point values.
### Complex multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiplyadd%28_,_,_%29-658zk.md)
  Performs `Y += AX` for complex double values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiplyadd%28_,_,_%29-4dpyu.md)
  Performs `Y += AX` for complex float values
- [SparseMultiplyAdd](./sparsemultiplyadd-4gs2p.md)
  Performs `Y += alpha * AX` for complex float values
- [SparseMultiplyAdd](./sparsemultiplyadd-7pu5c.md)
  Performs `Y += alpha * AX` for complex double values

## See Also

### Multiplying and transposing sparse matrices
- [Sparse Matrix and Dense Vector Multiplication](./sparse-matrix-and-dense-vector-multiplication.md)
  Multiply sparse matrices and dense vectors.
- [Transposition](./transposition.md)
  Transpose matrices, factorizations, and subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-matrix-and-dense-matrix-multiplication)*
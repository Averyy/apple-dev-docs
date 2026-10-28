# Subfactor Multiplication Functions

**Framework**: Accelerate  
**Role**: API Collection

Multiply subfactors by matrices and vectors.

## Topics

### Subfactor and dense matrix multiplication
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double)](./sparsemultiply%28_,_%29-88trz.md)
  Performs the multiply operation *Y* *= Subfactor \* X,* __in place on a dense matrix of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](./sparsemultiply%28_,_%29-3r4mf.md)
  Performs the multiply operation *Y*_ _*= Subfactor \* X*, in place on a dense matrix of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiply%28_,_,_%29-4nosz.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiply%28_,_,_%29-88stx.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_%29-34fp6.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](./sparsemultiply%28_,_%29-3dwed.md)
  Perform the multiply operation `y = Subfactor * x` for complex floatr values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_,_%29-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiply%28_,_,_%29-7q8gs.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.
### Subfactor and dense matrix multiplication with user-defined workspace
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-20xvs.md)
  Performs the multiply operation *Y* *= Subfactor \* X*, in place on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-6thvw.md)
  Performs the multiply operation *Y* *= Subfactor \* X*, in place on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-2osop.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of double-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-9v8hk.md)
  Performs the multiply operation *Y* *= Subfactor \* X* on a dense matrix of single-precision values and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-6strd.md)
  Perform the multiply operation `Y = Subfactor * X `for complex float values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-7mdi8.md)
  Perform the multiply operation `Y = Subfactor * X `for complex double values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-581zl.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
### Subfactor and dense vector multiplication
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double)](./sparsemultiply%28_,_%29-8ehhn.md)
  Performs the multiply operation *Y = Subfactor \* X*, in place on a vector of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float)](./sparsemultiply%28_,_%29-7l3sr.md)
  Performs the multiply operation *Y = Subfactor \* X*, in place on a vector of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double)](./sparsemultiply%28_,_,_%29-6abql.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float)](./sparsemultiply%28_,_,_%29-2h425.md)
  Performs the multiply operation *Y = Subfactor \** *X* on a vector of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiply%28_,_%29-3s0hu.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](./sparsemultiply%28_,_%29-9fn7j.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](./sparsemultiply%28_,_,_%29-4fwfv.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](./sparsemultiply%28_,_,_%29-58wuo.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_,_%29-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
### Subfactor and dense vector multiplication with user-defined workspace
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-9tahm.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values *X*, in place and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-4u1y3.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of single-precision values *X*, in place and without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-1ooyi.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values *X*, without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-3l60d.md)
  Performs the multiply operation *Y = Subfactor \* X* on a vector of double-precision values *X*, without any internal memory allocations.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-5etjg.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_%29-5kh07.md)
  Perform the multiply operation `y = Subfactor * x` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-4xr8.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-7xipz.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsemultiply%28_,_,_,_%29-9v0nu.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.

## See Also

### Subfactor Solve and Operation Functions
- [Subfactor Solve Functions](./subfactor-solve-functions.md)
  Solve systems with the equation *Subfactor \* X = B*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/subfactor-multiplication-functions)*
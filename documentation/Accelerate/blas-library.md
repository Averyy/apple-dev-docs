# BLAS

**Framework**: Accelerate

Perform common linear algebra operations with Apple’s implementation of the Basic Linear Algebra Subprograms (BLAS).

#### Overview

The vecLib framework contains nine C header files (not counting `vecLib.h`, which merely includes the others).

This document describes the functions declared in the header files `cblas.h` and `vblas.h`, which contain the interfaces for Apple’s implementation of the BLAS API.

Note that documentation describing the leading dimension as the first dimension of a matrix refers to column-major ordering. In row-major ordering, the leading dimension is the second dimension of a matrix.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Topics

### Specifying the threading model
- [struct BLAS](blas.md)
  An enumeration that acts as a namespace for Swift overlays to BLAS.
- [func BLASSetThreading(BLAS_THREADING) -> Int32](blassetthreading(_:).md)
  Sets the BLAS and LAPACK threading model.
- [func BLASGetThreading() -> BLAS_THREADING](blasgetthreading().md)
  Returns the current BLAS and LAPACK threading model.
- [struct BLAS_THREADING](blas_threading.md)
  Constants that describe the BLAS and LAPACK threading model.
### General functions
- [SetBLASParamErrorProc](setblasparamerrorproc.md)
  Sets an error handler function.
- [cblas_errprn](cblas_errprn.md)
  Prints an error message.
- [cblas_xerbla](cblas_xerbla.md)
  The default error handler for BLAS routines.
- [func cblas_icamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](cblas_icamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (single-precision complex).
- [func cblas_idamax(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> __LAPACK_int](cblas_idamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (double-precision).
- [func cblas_isamax(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> __LAPACK_int](cblas_isamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (single-precision).
- [func cblas_izamax(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> __LAPACK_int](cblas_izamax(_:_:_:).md)
  Returns the index of the element with the largest absolute value in a vector (double-precision complex).
### Sparse computation
- [Matrix and Vector Operations](matrix-and-vector-operations.md)
  Perform computations with matrices and vectors.
- [Pointwise Matrix Operations](pointwise-matrix-operations.md)
  Create, insert values into, and extract values from a pointwise sparse matrix.
- [Blockwise Matrix Operations](blockwise-matrix-operations.md)
  Create, insert values into, and extract values from a blockwise sparse matrix.
- [General Sparse Matrix Management Operations](general-sparse-matrix-management-operations.md)
  Manage and work with the properties of a sparse matrix.
- [Sparse Vector Utility Operations](sparse-vector-utility-operations.md)
  Create and work with sparse vector structures.
### Data types
- [typealias BLASParamErrorProc](blasparamerrorproc.md)
  A BLAS error handler callback type.
### Constants
- [struct CBLAS_ORDER](cblas_order.md)
- [struct CBLAS_TRANSPOSE](cblas_transpose.md)
- [struct CBLAS_UPLO](cblas_uplo.md)
- [struct CBLAS_DIAG](cblas_diag.md)
- [struct CBLAS_SIDE](cblas_side.md)
### Variables
- [var CblasColMajor: CBLAS_ORDER](cblascolmajor.md)
- [var CblasConjTrans: CBLAS_TRANSPOSE](cblasconjtrans.md)
- [var CblasLeft: CBLAS_SIDE](cblasleft.md)
- [var CblasLower: CBLAS_UPLO](cblaslower.md)
- [var CblasNoTrans: CBLAS_TRANSPOSE](cblasnotrans.md)
- [var CblasNonUnit: CBLAS_DIAG](cblasnonunit.md)
- [var CblasRight: CBLAS_SIDE](cblasright.md)
- [var CblasRowMajor: CBLAS_ORDER](cblasrowmajor.md)
- [var CblasTrans: CBLAS_TRANSPOSE](cblastrans.md)
- [var CblasUnit: CBLAS_DIAG](cblasunit.md)
- [var CblasUpper: CBLAS_UPLO](cblasupper.md)
- [var AtlasConj: CBLAS_TRANSPOSE](atlasconj.md)
### CATLAS and CBLAS vector functions
- [func catlas_caxpby(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](catlas_caxpby(_:_:_:_:_:_:_:).md)
  Computes the product of two vectors, scaling each one separately (single-precision complex).
- [func catlas_cset(__LAPACK_int, OpaquePointer, OpaquePointer, __LAPACK_int)](catlas_cset(_:_:_:_:).md)
  Modifies a vector (single-precision complex) in place, setting each element to a given value.
- [func catlas_daxpby(__LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](catlas_daxpby(_:_:_:_:_:_:_:).md)
  Computes the sum of two vectors, scaling each one separately (double-precision).
- [func catlas_dset(__LAPACK_int, Double, UnsafeMutablePointer<Double>, __LAPACK_int)](catlas_dset(_:_:_:_:).md)
  Modifies a vector (double-precision) in place, setting each element to a given value.
- [func catlas_saxpby(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](catlas_saxpby(_:_:_:_:_:_:_:).md)
  Computes the sum of two vectors, scaling each one separately (single-precision).
- [func catlas_sset(__LAPACK_int, Float, UnsafeMutablePointer<Float>, __LAPACK_int)](catlas_sset(_:_:_:_:).md)
  Modifies a vector (single-precision) in place, setting each element to a given value.
- [func catlas_zaxpby(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](catlas_zaxpby(_:_:_:_:_:_:_:).md)
  Computes the sum of two vectors, scaling each one separately (double-precision complex).
- [func catlas_zset(__LAPACK_int, OpaquePointer, OpaquePointer, __LAPACK_int)](catlas_zset(_:_:_:_:).md)
  Modifies a vector (double-precision complex) in place, setting each element to a given value.
- [func cblas_sdot(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_sdot(_:_:_:_:_:).md)
  Computes the dot product of two vectors (single-precision).
- [func cblas_sdsdot(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_sdsdot(_:_:_:_:_:_:).md)
  Computes the dot product of two single-precision vectors plus an initial single-precision value.
- [func cblas_cdotc_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_cdotc_sub(_:_:_:_:_:_:).md)
  Calculates the dot product of the complex conjugate of a single-precision complex vector with a second single-precision complex vector.
- [func cblas_cdotu_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_cdotu_sub(_:_:_:_:_:_:).md)
  Computes the dot product of two single-precision complex vectors.
- [func cblas_ddot(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](cblas_ddot(_:_:_:_:_:).md)
  Computes the dot product of two vectors (double-precision).
- [func cblas_dsdot(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Double](cblas_dsdot(_:_:_:_:_:).md)
  Computes the double-precision dot product of a pair of single-precision vectors.
- [func cblas_zdotc_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_zdotc_sub(_:_:_:_:_:_:).md)
  Calculates the dot product of the complex conjugate of a double-precision complex vector with a second double-precision complex vector.
- [func cblas_zdotu_sub(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer)](cblas_zdotu_sub(_:_:_:_:_:_:).md)
  Computes the dot product of two double-precision complex vectors.
### Single-precision float matrix functions
- [func cblas_sasum(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_sasum(_:_:_:).md)
  Computes the sum of the absolute values of elements in a vector (single-precision).
- [func cblas_saxpy(__LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_saxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (single-precision).
- [func cblas_scopy(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_scopy(_:_:_:_:_:).md)
  Copies a vector to another vector (single-precision).
- [func cblas_sgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (single precision).
- [func cblas_sgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (single-precision).
- [func cblas_sgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a single-precision matrix by a vector.
- [func cblas_sger(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sger(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (single precison).
- [func cblas_snrm2(__LAPACK_int, UnsafePointer<Float>?, __LAPACK_int) -> Float](cblas_snrm2(_:_:_:).md)
  Computes the L2 norm (Euclidian length) of a vector (single precision).
- [func cblas_srot(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, Float, Float)](cblas_srot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of vectors.
- [func cblas_srotg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](cblas_srotg(_:_:_:_:).md)
  Constructs a Givens rotation matrix.
- [func cblas_srotm(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafePointer<Float>)](cblas_srotm(_:_:_:_:_:_:).md)
  Applies a modified Givens transformation (single precision).
- [func cblas_srotmg(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, Float, UnsafeMutablePointer<Float>)](cblas_srotmg(_:_:_:_:_:).md)
  Generates a modified Givens rotation matrix.
- [func cblas_ssbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a symmetric band matrix, then multiplies by a vector, then adds a vector (single-precision).
- [func cblas_sscal(__LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (single-precision).
- [func cblas_sspmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sspmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed symmetric matrix, then multiplies by a vector, then scales and adds another vector (single precision).
- [func cblas_sspr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?)](cblas_sspr(_:_:_:_:_:_:_:).md)
  Rank one update: adds a packed symmetric matrix to the product of a scaling factor, a vector, and its transpose (single precision).
- [func cblas_sspr2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?)](cblas_sspr2(_:_:_:_:_:_:_:_:_:).md)
  Rank two update of a packed symmetric matrix using two vectors (single precision).
- [func cblas_sswap(__LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_sswap(_:_:_:_:_:).md)
  Exchanges the elements of two vectors (single precision).
- [func cblas_ssymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssymm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a symmetric matrix (single-precision).
- [func cblas_ssymv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssymv(_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a symmetric matrix, multiplies by a vector, then scales and adds another vector (single precision).
- [func cblas_ssyr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssyr(_:_:_:_:_:_:_:_:).md)
  Rank one update: adds a symmetric matrix to the product of a scaling factor, a vector, and its transpose (single precision).
- [func cblas_ssyr2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssyr2(_:_:_:_:_:_:_:_:_:_:).md)
  Rank two update of a symmetric matrix using two vectors (single precision).
- [func cblas_ssyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssyr2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a symmetric matrix (single precision).
- [func cblas_ssyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_ssyrk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a symmetric matrix by its transpose and adds a second matrix (single precision).
- [func cblas_stbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_stbmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular band matrix, then multiplies by a vector (single precision).
- [func cblas_stbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_stbsv(_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular banded system of equations.
- [func cblas_stpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_stpmv(_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector, then adds a vector (single precision).
- [func cblas_stpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_stpsv(_:_:_:_:_:_:_:_:).md)
  Solves a packed triangular system of equations.
- [func cblas_strmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_strmm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular matrix and multiplies it by a matrix.
- [func cblas_strmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_strmv(_:_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector.
- [func cblas_strsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_strsm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with multiple values for the right side.
- [func cblas_strsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>?, __LAPACK_int)](cblas_strsv(_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with a single value for the right side.
- [func appleblas_sgeadd(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, Float, UnsafePointer<Float>?, __LAPACK_int, UnsafeMutablePointer<Float>, __LAPACK_int)](appleblas_sgeadd(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
### Single-precision complex matrix functions
- [func cblas_caxpy(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_caxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (single-precision complex).
- [func cblas_ccopy(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ccopy(_:_:_:_:_:).md)
  Copies a vector to another vector (single-precision complex).
- [func cblas_cgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (single-precision complex).
- [func cblas_cgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (single-precision complex).
- [func cblas_cgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a vector (single-precision complex).
- [func cblas_cgerc(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cgerc(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the conjugate transpose of vector Y, then adds matrix A (single-precision complex).
- [func cblas_cgeru(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cgeru(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (single-precision complex).
- [func cblas_chbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a Hermitian band matrix, then multiplies by a vector, then adds a vector (single-precision complex).
- [func cblas_chemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chemm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two Hermitian matrices (single-precision complex), then adds a third (with scaling).
- [func cblas_chemv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chemv(_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales and multiplies a Hermitian matrix by a vector, then adds a second (scaled) vector.
- [func cblas_cher(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cher(_:_:_:_:_:_:_:_:).md)
  Hermitian rank 1 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of `X` to matrix `A`.
- [func cblas_cher2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cher2(_:_:_:_:_:_:_:_:_:_:).md)
  Hermitian rank 2 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of vector `Y` to the product of the conjugate of the scaling factor, vector `Y`, and the conjugate transpose of vector `X`, and adds the result to matrix `A`.
- [func cblas_cher2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](cblas_cher2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a complex Hermitian matrix (single-precision complex).
- [func cblas_cherk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](cblas_cherk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a Hermitian matrix by its transpose and adds a second matrix (single precision).
- [func cblas_chpmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_chpmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed hermitian matrix, multiplies it by a vector, and adds a scaled vector.
- [func cblas_chpr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Float, OpaquePointer?, __LAPACK_int, OpaquePointer?)](cblas_chpr(_:_:_:_:_:_:_:).md)
  Scales and multiplies a vector times its conjugate transpose, then adds a matrix.
- [func cblas_chpr2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?)](cblas_chpr2(_:_:_:_:_:_:_:_:_:).md)
  Multiplies a vector times the conjugate transpose of a second vector and vice-versa, sums the results, and adds a matrix.
- [func cblas_crotg(OpaquePointer, OpaquePointer, UnsafeMutablePointer<Float>, OpaquePointer)](cblas_crotg(_:_:_:_:).md)
  Constructs a complex Givens rotation.
- [func cblas_cscal(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_cscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (single-precision complex).
- [func cblas_csrot(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Float, Float)](cblas_csrot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of complex vectors.
- [func cblas_csscal(__LAPACK_int, Float, OpaquePointer?, __LAPACK_int)](cblas_csscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (single-precision complex).
- [func cblas_cswap(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_cswap(_:_:_:_:_:).md)
  Exchanges the elements of two vectors (single-precision complex).
- [func cblas_csymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_csymm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a symmetric matrix (single-precision complex).
- [func cblas_csyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_csyr2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a symmetric matrix (single-precision complex).
- [func cblas_csyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_csyrk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a symmetric matrix by its transpose and adds a second matrix (single-precision complex).
- [func cblas_ctbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ctbmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular band matrix, then multiplies by a vector (single-precision compex).
- [func cblas_ctbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ctbsv(_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular banded system of equations.
- [func cblas_ctpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, OpaquePointer?, __LAPACK_int)](cblas_ctpmv(_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector, then adds a vector (single-precision complex).
- [func cblas_ctpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, OpaquePointer?, __LAPACK_int)](cblas_ctpsv(_:_:_:_:_:_:_:_:).md)
  Solves a packed triangular system of equations.
- [func cblas_ctrmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ctrmm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular matrix and multiplies it by a matrix.
- [func cblas_ctrmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ctrmv(_:_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector.
- [func cblas_ctrsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ctrsm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with multiple values for the right side.
- [func cblas_ctrsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ctrsv(_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with a single value for the right side.
- [func cblas_scasum(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Float](cblas_scasum(_:_:_:).md)
  Computes the sum of the absolute values of real and imaginary parts of elements in a vector (single-precision complex).
- [func cblas_scnrm2(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Float](cblas_scnrm2(_:_:_:).md)
  Computes the unitary norm of a vector (single-precision complex).
### Double-precision float matrix functions
- [func cblas_dasum(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](cblas_dasum(_:_:_:).md)
  Computes the sum of the absolute values of elements in a vector (double-precision).
- [func cblas_daxpy(__LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_daxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (double-precision).
- [func cblas_dcopy(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dcopy(_:_:_:_:_:).md)
  Copies a vector to another vector (double-precision).
- [func cblas_dgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (double precision).
- [func cblas_dgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (double-precision).
- [func cblas_dgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a vector (double precision).
- [func cblas_dger(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dger(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (double precison).
- [func cblas_dnrm2(__LAPACK_int, UnsafePointer<Double>?, __LAPACK_int) -> Double](cblas_dnrm2(_:_:_:).md)
  Computes the L2 norm (Euclidian length) of a vector (double precision).
- [func cblas_drot(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, Double, Double)](cblas_drot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of vectors.
- [func cblas_drotg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>)](cblas_drotg(_:_:_:_:).md)
  Constructs a Givens rotation matrix.
- [func cblas_drotm(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafePointer<Double>)](cblas_drotm(_:_:_:_:_:_:).md)
  Applies a modified Givens transformation (single precision).
- [func cblas_drotmg(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, Double, UnsafeMutablePointer<Double>)](cblas_drotmg(_:_:_:_:_:).md)
  Generates a modified Givens rotation matrix.
- [func cblas_dsbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a symmetric band matrix, then multiplies by a vector, then adds a vector (double precision).
- [func cblas_dscal(__LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (double-precision).
- [func cblas_dspmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dspmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed symmetric matrix, then multiplies by a vector, then scales and adds another vector (double precision).
- [func cblas_dspr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?)](cblas_dspr(_:_:_:_:_:_:_:).md)
  Rank one update: adds a packed symmetric matrix to the product of a scaling factor, a vector, and its transpose (double precision).
- [func cblas_dspr2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?)](cblas_dspr2(_:_:_:_:_:_:_:_:_:).md)
  Rank two update of a packed symmetric matrix using two vectors (single precision).
- [func cblas_dswap(__LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dswap(_:_:_:_:_:).md)
  Exchanges the elements of two vectors (double precision).
- [func cblas_dsymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsymm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a symmetric matrix (double-precision).
- [func cblas_dsymv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsymv(_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a symmetric matrix, multiplies by a vector, then scales and adds another vector (single precision).
- [func cblas_dsyr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsyr(_:_:_:_:_:_:_:_:).md)
  Rank one update: adds a symmetric matrix to the product of a scaling factor, a vector, and its transpose (double precision).
- [func cblas_dsyr2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsyr2(_:_:_:_:_:_:_:_:_:_:).md)
  Rank two update of a symmetric matrix using two vectors (single precision).
- [func cblas_dsyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsyr2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a symmetric matrix (double precision).
- [func cblas_dsyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dsyrk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a symmetric matrix by its transpose and adds a second matrix (double precision).
- [func cblas_dtbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtbmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular band matrix, then multiplies by a vector (double precision).
- [func cblas_dtbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtbsv(_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular banded system of equations.
- [func cblas_dtpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Double>?, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtpmv(_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector, then adds a vector (double precision).
- [func cblas_dtpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Double>?, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtpsv(_:_:_:_:_:_:_:_:).md)
  Solves a packed triangular system of equations.
- [func cblas_dtrmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtrmm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular matrix and multiplies it by a matrix.
- [func cblas_dtrmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtrmv(_:_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector.
- [func cblas_dtrsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtrsm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with multiple values for the right side.
- [func cblas_dtrsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>?, __LAPACK_int)](cblas_dtrsv(_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with a single value for the right side.
- [func appleblas_dgeadd(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, Double, UnsafePointer<Double>?, __LAPACK_int, UnsafeMutablePointer<Double>, __LAPACK_int)](appleblas_dgeadd(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
### Double-precision complex matrix functions
- [func cblas_dzasum(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Double](cblas_dzasum(_:_:_:).md)
  Computes the sum of the absolute values of real and imaginary parts of elements in a vector (single-precision complex).
- [func cblas_dznrm2(__LAPACK_int, OpaquePointer?, __LAPACK_int) -> Double](cblas_dznrm2(_:_:_:).md)
  Computes the unitary norm of a vector (double-precision complex).
- [func cblas_zaxpy(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zaxpy(_:_:_:_:_:_:).md)
  Computes a constant times a vector plus a vector (double-precision complex).
- [func cblas_zcopy(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zcopy(_:_:_:_:_:).md)
  Copies a vector to another vector (double-precision complex).
- [func cblas_zdrot(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Double, Double)](cblas_zdrot(_:_:_:_:_:_:_:).md)
  Applies a Givens rotation matrix to a pair of complex vectors.
- [func cblas_zdscal(__LAPACK_int, Double, OpaquePointer?, __LAPACK_int)](cblas_zdscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (double-precision complex).
- [func cblas_zgbmv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zgbmv(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a general band matrix, then multiplies by a vector, then adds a vector (double-precision complex).
- [func cblas_zgemm(CBLAS_ORDER, CBLAS_TRANSPOSE, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zgemm(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two matrices (double-precision complex).
- [func cblas_zgemv(CBLAS_ORDER, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zgemv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a vector (double-precision complex).
- [func cblas_zgerc(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zgerc(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the conjugate transpose of vector Y, then adds matrix A (double-precision complex).
- [func cblas_zgeru(CBLAS_ORDER, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zgeru(_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies vector X by the transpose of vector Y, then adds matrix A (double-precision complex).
- [func cblas_zhbmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhbmv(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a Hermitian band matrix, then multiplies by a vector, then adds a vector (double-precision complex).
- [func cblas_zhemm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhemm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies two Hermitian matrices (double-precision complex).
- [func cblas_zhemv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhemv(_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales and multiplies a Hermitian matrix by a vector, then adds a second (scaled) vector.
- [func cblas_zher(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zher(_:_:_:_:_:_:_:_:).md)
  Adds the product of a scaling factor, vector `X`, and the conjugate transpose of `X` to matrix `A`.
- [func cblas_zher2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zher2(_:_:_:_:_:_:_:_:_:_:).md)
  Hermitian rank 2 update: adds the product of a scaling factor, vector `X`, and the conjugate transpose of vector `Y` to the product of the conjugate of the scaling factor, vector `Y`, and the conjugate transpose of vector `X`, and adds the result to matrix `A`.
- [func cblas_zher2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int)](cblas_zher2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a complex Hermitian matrix (double-precision complex).
- [func cblas_zherk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int)](cblas_zherk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a Hermitian matrix by its transpose and adds a second matrix (single precision).
- [func cblas_zhpmv(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zhpmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a packed hermitian matrix, multiplies it by a vector, and adds a scaled vector.
- [func cblas_zhpr(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, Double, OpaquePointer?, __LAPACK_int, OpaquePointer?)](cblas_zhpr(_:_:_:_:_:_:_:).md)
  Scales and multiplies a vector times its conjugate transpose, then adds a matrix.
- [func cblas_zhpr2(CBLAS_ORDER, CBLAS_UPLO, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?)](cblas_zhpr2(_:_:_:_:_:_:_:_:_:).md)
  Multiplies a vector times the conjugate transpose of a second vector and vice-versa, sums the results, and adds a matrix.
- [func cblas_zrotg(OpaquePointer, OpaquePointer, UnsafeMutablePointer<Double>, OpaquePointer)](cblas_zrotg(_:_:_:_:).md)
  Constructs a complex Givens rotation.
- [func cblas_zscal(__LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zscal(_:_:_:_:).md)
  Multiplies each element of a vector by a constant (double-precision complex).
- [func cblas_zswap(__LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_zswap(_:_:_:_:_:).md)
  Exchanges the elements of two vectors (double-precision complex).
- [func cblas_zsymm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zsymm(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiplies a matrix by a symmetric matrix (double-precision complex).
- [func cblas_zsyr2k(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zsyr2k(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Performs a rank-2k update of a symmetric matrix (double-precision complex).
- [func cblas_zsyrk(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int)](cblas_zsyrk(_:_:_:_:_:_:_:_:_:_:_:).md)
  Rank-k update—multiplies a symmetric matrix by its transpose and adds a second matrix (double-precision complex).
- [func cblas_ztbmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ztbmv(_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular band matrix, then multiplies by a vector (double-precision complex).
- [func cblas_ztbsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ztbsv(_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular banded system of equations.
- [func cblas_ztpmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, OpaquePointer?, __LAPACK_int)](cblas_ztpmv(_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector, then adds a vector (double-precision compex).
- [func cblas_ztpsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, OpaquePointer?, __LAPACK_int)](cblas_ztpsv(_:_:_:_:_:_:_:_:).md)
  Solves a packed triangular system of equations.
- [func cblas_ztrmm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ztrmm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Scales a triangular matrix and multiplies it by a matrix.
- [func cblas_ztrmv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ztrmv(_:_:_:_:_:_:_:_:_:).md)
  Multiplies a triangular matrix by a vector.
- [func cblas_ztrsm(CBLAS_ORDER, CBLAS_SIDE, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, __LAPACK_int, OpaquePointer, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ztrsm(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with multiple values for the right side.
- [func cblas_ztrsv(CBLAS_ORDER, CBLAS_UPLO, CBLAS_TRANSPOSE, CBLAS_DIAG, __LAPACK_int, OpaquePointer?, __LAPACK_int, OpaquePointer?, __LAPACK_int)](cblas_ztrsv(_:_:_:_:_:_:_:_:_:).md)
  Solves a triangular system of equations with a single value for the right side.
### LAPACK functions
- [LAPACK/BLAS Functions](lapack-functions.md)
  An updated BLAS interface supporting ILP64 is available.
- [func cgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](cgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](cgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, OpaquePointer, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](cgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func claqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, OpaquePointer, UnsafeMutablePointer<__LAPACK_int>)](claqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func claqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](claqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func crscl_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](crscl_(_:_:_:_:).md)
- [func dgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](dgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](dgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](dgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dlaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>)](dlaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func dlaqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](dlaqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](sgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](sgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](sgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func slaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>)](slaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func sgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](sgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func slaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>)](slaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func slaqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafeMutablePointer<Float>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](slaqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zgedmd_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](zgedmd_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zgedmdq_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafeMutablePointer<__LAPACK_int>, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>)](zgedmdq_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zgeqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, OpaquePointer, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](zgeqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zlaqp2rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, OpaquePointer, UnsafeMutablePointer<__LAPACK_int>)](zlaqp2rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zlaqp3rk_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<__LAPACK_int>, UnsafePointer<Double>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_bool>, UnsafeMutablePointer<__LAPACK_int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<__LAPACK_int>?, OpaquePointer?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, OpaquePointer?, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafeMutablePointer<__LAPACK_int>?, UnsafeMutablePointer<__LAPACK_int>)](zlaqp3rk_(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func zrscl_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](zrscl_(_:_:_:_:).md)
- [typealias sparse_matrix_double_complex](sparse_matrix_double_complex.md)
- [typealias sparse_matrix_float_complex](sparse_matrix_float_complex.md)
- [typealias vFloatPacked](vfloatpacked.md)

## See Also

- [Solving systems of linear equations with LAPACK](solving-systems-of-linear-equations-with-lapack.md)
  Select the optimal LAPACK routine to solve a system of linear equations.
- [Finding an interpolating polynomial using the Vandermonde method](finding-an-interpolating-polynomial-using-the-vandermonde-method.md)
  Use LAPACK to solve a linear system and find an interpolating polynomial to construct new points between a series of known data points.
- [Compressing an image using linear algebra](compressing-an-image-using-linear-algebra.md)
  Reduce the storage size of an image using singular value decomposition (SVD).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/blas-library)*
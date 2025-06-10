# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the specified factorization of a sparse matrix of single-precision values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseFactor(_ type: SparseFactorization_t, _ Matrix: SparseMatrix_Float) -> SparseOpaqueFactorization_Float
```

#### Return Value

A [`SparseOpaqueFactorization_Float`](sparseopaquefactorization_float.md) structure that represents the matrix factorization.

#### Discussion

Use this function to calculate the factorization of a sparse matrix to pass to the direct solve functions. The following figure shows a system of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix. ](https://docs-assets.developer.apple.com/published/0974a26754c699cdf34196f2c95365c3/media-3703881%402x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

```swift
/// Create the coefficient matrix _A_.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Float] =       [10, 20, 5, 50]

let A = SparseConvertFromCoordinate(3, 3,
                                    4, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)

/// Factorize _A_.
let factorization = SparseFactor(SparseFactorizationQR, A)

defer {
    SparseCleanup(A)
    SparseCleanup(factorization)
}

/// Create the right-hand-side vector, _b_.
var bValues: [Float] = [30.0, 35.0, 100.0]

bValues.withUnsafeMutableBufferPointer { bPtr in
    
    let xb = DenseVector_Float(count: 3,
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization, xb)
}
```

On return, `bValues` contains the values `[1.0, 2.0, 3.0]`.

You can use the symbolic factorization that this function returns for multiple numerical factorizations with different numerical values but the same nonzero structure.

## Parameters

- `type`: The type of factorization to perform.
- `Matrix`: The matrix to factorize.

## See Also

- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:)-8gl6j.md)
  Returns the specified factorization of a sparse matrix of double-precision values.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:_:_:)-88xmk.md)
  Returns the specified factorization of a sparse matrix of double-precision values using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Float](sparsefactor(_:_:_:_:)-8apyz.md)
  Returns the specified factorization of a sparse matrix of single-precision values using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-38shj)*
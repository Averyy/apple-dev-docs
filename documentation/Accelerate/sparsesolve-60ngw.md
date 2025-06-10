# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system  using the supplied single-precision factorization of , in place.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Float, _ xb: DenseVector_Float)
```

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. The following figure shows a system of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix.](https://docs-assets.developer.apple.com/published/0974a26754c699cdf34196f2c95365c3/media-3703891%402x.png)

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
var bValues: [Float] = [30, 35, 100]

/// Solve the system.
bValues.withUnsafeMutableBufferPointer { bPtr in
    let xb = DenseVector_Float(count: 3,
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization, xb)
}
```

On return, `bValues` contains the values `[1.0, 2.0, 3.0]`.

If the factorization is , the function returns the solution of minimum norm  for underdetermined systems.

If the factorization is , the function returns the least squares solution  for overdetermined systems.

If the factorization is [`SparseFactorizationCholeskyAtA`](sparsefactorizationcholeskyata.md), the factorization is of , and the solution that returns is for the system .

## Parameters

- `Factored`: The factored matrix to solve.
- `xb`: On input, the vector  . On return, the function overwrites with the vector  . If   has dimension  , this parameter must have length  , where  .

## See Also

- [func SparseSolve(SparseOpaqueFactorization_Double, DenseVector_Double)](sparsesolve(_:_:)-pofy.md)
  Solves the system  using the supplied double-precision factorization of .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-60ngw)*
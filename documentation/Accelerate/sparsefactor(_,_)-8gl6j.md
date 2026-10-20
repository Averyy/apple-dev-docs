# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the specified factorization of a sparse matrix of double-precision values.

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
func SparseFactor(_ type: SparseFactorization_t, _ Matrix: SparseMatrix_Double) -> SparseOpaqueFactorization_Double
```

```c
static SparseOpaqueFactorization_Double SparseFactor(SparseFactorization_t type, SparseMatrix_Double Matrix);
```

## Mentions

- [Solving systems using direct methods](./solving-systems-using-direct-methods.md)

#### Return Value

A [`SparseOpaqueFactorization_Double`](./sparseopaquefactorization_double.md) structure that represents the matrix factorization.

#### Discussion

Use this function to calculate the factorization of a sparse matrix to pass to the direct solve functions. The following figure shows a system of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703880@2x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

**Swift**:

```swift
// Create the coefficient matrix `A` from coordinate (COO) arrays.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Double] =      [10, 20, 5, 50]

let A = SparseConvertFromCoordinate(3, 3,
                                    4, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)

// Compute the factors of `A` using a QR decomposition.
let factorization = SparseFactor(SparseFactorizationQR, A)

defer {
    SparseCleanup(A)
    SparseCleanup(factorization)
}

// Create the right-hand-side vector `b` (also holds the solution on return).
var bValues = [30.0, 35.0, 100.0]

bValues.withUnsafeMutableBufferPointer { bPtr in
    
    let xb = DenseVector_Double(count: 3,
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization, xb)
}

print(bValues) // Prints "[1.0, 2.0, 3.0]".
```

**Objective-C**:

```objc
// Create the coefficient matrix `A` from coordinate (COO) arrays.
int rowIndices[]    = {0, 1, 1, 2};
int columnIndices[] = {2, 0, 2, 1};
double aValues[]    = {10, 20, 5, 50};

SparseMatrix_Double A = SparseConvertFromCoordinate(3, 3,
                                                    4, 1,
                                                    (SparseAttributes_t){0},
                                                    rowIndices, columnIndices,
                                                    aValues);

// Compute the factors of `A` using a QR decomposition.
SparseOpaqueFactorization_Double factorization = SparseFactor(SparseFactorizationQR, A);

// Create the right-hand-side vector `b` (also holds the solution on return).
double bValues[] = {30.0, 35.0, 100.0};

DenseVector_Double xb = {
    .count = 3,
    .data  = bValues
};

SparseSolve(factorization, xb);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", bValues[0], bValues[1], bValues[2]);

SparseCleanup(A);
SparseCleanup(factorization);
```

On return, `bValues` contains the values `[1.0, 2.0, 3.0]`.

You can use the symbolic factorization that this function returns for multiple numerical factorizations with different numerical values but the same nonzero structure.

## Parameters

- `type`: The type of factorization to perform.
- `Matrix`: The matrix to factorize.

## See Also

### Matrix factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Float) -> SparseOpaqueFactorization_Float](./sparsefactor%28_,_%29-38shj.md)
  Returns the specified factorization of a sparse matrix of single-precision values.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Double](./sparsefactor%28_,_,_,_%29-88xmk.md)
  Returns the specified factorization of a sparse matrix of double-precision values using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Float](./sparsefactor%28_,_,_,_%29-8apyz.md)
  Returns the specified factorization of a sparse matrix of single-precision values using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-8gl6j)*
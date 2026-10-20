# SparseFactor(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the specified factorization of a sparse matrix of single-precision values using the specified options.

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
func SparseFactor(_ type: SparseFactorization_t, _ Matrix: SparseMatrix_Float, _ options: SparseSymbolicFactorOptions, _ nfoptions: SparseNumericFactorOptions) -> SparseOpaqueFactorization_Float
```

```c
static SparseOpaqueFactorization_Float SparseFactor(SparseFactorization_t type, SparseMatrix_Float Matrix, SparseSymbolicFactorOptions sfoptions, SparseNumericFactorOptions nfoptions);
```

#### Return Value

A [`SparseOpaqueFactorization_Float`](./sparseopaquefactorization_float.md) structure that represents the matrix factorization.

#### Discussion

Use this function to calculate the factorization of a sparse matrix to pass to the direct solve functions. The following figure shows a system of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703882@2x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

**Swift**:

```swift
// Create the coefficient matrix `A` from coordinate (COO) arrays.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Float] =       [10, 20, 5, 50]

let A = SparseConvertFromCoordinate(3, 3,
                                    4, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)

// Compute the factors of `A` using a QR decomposition with symbolic and numeric options.
let symbolicOptions = SparseSymbolicFactorOptions(
    control: SparseDefaultControl,
    orderMethod: SparseOrderDefault,
    order: nil,
    ignoreRowsAndColumns: nil,
    malloc: { malloc($0) },
    free: { free($0) },
    reportError: nil)
let numericOptions = SparseNumericFactorOptions()
let factorization = SparseFactor(SparseFactorizationQR, A,
                                 symbolicOptions,
                                 numericOptions)

defer {
    SparseCleanup(A)
    SparseCleanup(factorization)
}

// Create the right-hand-side vector `b` (also holds the solution on return).
var bValues: [Float] = [30.0, 35.0, 100.0]

bValues.withUnsafeMutableBufferPointer { bPtr in
    
    let xb = DenseVector_Float(count: 3,
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
float aValues[]     = {10, 20, 5, 50};

SparseMatrix_Float A = SparseConvertFromCoordinate(3, 3,
                                                   4, 1,
                                                   (SparseAttributes_t){0},
                                                   rowIndices, columnIndices,
                                                   aValues);

// Compute the factors of `A` using a QR decomposition with symbolic and numeric options.
SparseSymbolicFactorOptions symbolicOptions = {
    .control              = SparseDefaultControl,
    .orderMethod          = SparseOrderDefault,
    .order                = NULL,
    .ignoreRowsAndColumns = NULL,
    .malloc               = malloc,
    .free                 = free,
    .reportError          = NULL
};
SparseNumericFactorOptions numericOptions = (SparseNumericFactorOptions){0};
SparseOpaqueFactorization_Float factorization = SparseFactor(SparseFactorizationQR, A,
                                                             symbolicOptions,
                                                             numericOptions);

// Create the right-hand-side vector `b` (also holds the solution on return).
float bValues[] = {30.0f, 35.0f, 100.0f};
DenseVector_Float xb = { .count = 3, .data = bValues };
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
- `options`: The symbolic factor options, such as the ordering algorithm to use.
- `nfoptions`: The numeric factor options, such as the scaling method to use.

## See Also

### Matrix factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double) -> SparseOpaqueFactorization_Double](./sparsefactor%28_,_%29-8gl6j.md)
  Returns the specified factorization of a sparse matrix of double-precision values.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Float) -> SparseOpaqueFactorization_Float](./sparsefactor%28_,_%29-38shj.md)
  Returns the specified factorization of a sparse matrix of single-precision values.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Double](./sparsefactor%28_,_,_,_%29-88xmk.md)
  Returns the specified factorization of a sparse matrix of double-precision values using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:_:_:)-8apyz)*
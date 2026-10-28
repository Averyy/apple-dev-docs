# SparseFactor(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the factorization of a sparse matrix of single-precision values that corresponds to the supplied symbolic factorization using specified options.

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
func SparseFactor(_ SymbolicFactor: SparseOpaqueSymbolicFactorization, _ Matrix: SparseMatrix_Float, _ nfoptions: SparseNumericFactorOptions) -> SparseOpaqueFactorization_Float
```

```c
static SparseOpaqueFactorization_Float SparseFactor(SparseOpaqueSymbolicFactorization SymbolicFactor, SparseMatrix_Float Matrix, SparseNumericFactorOptions nfoptions);
```

## Return Value

A [`SparseOpaqueFactorization_Float`](./sparseopaquefactorization_float.md) structure that represents the matrix factorization.

## Discussion

Use this function to solve a system of linear equations using a symbolic factorization that [`SparseFactor(_:_:)`](./sparsefactor%28_,_%29-3697o.md) creates.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as two matrix equations, A x equals B. Each matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703903@2x.png)

The following code solves these two systems by calling [`SparseFactor(_:_:)`](./sparsefactor%28_,_%29-58oq8.md) and [`SparseFactor(_:_:)`](./sparsefactor%28_,_%29-1p6im.md):

**Swift**:

```swift
// Define the sparsity pattern of matrices `A0` and `A1`.
let rowIndices: [Int32] =    [ 0, 1, 1, 2]
let columnIndices: [Int32] = [ 2, 0, 2, 1]

// Create the single-precision coefficient matrix `A0` from coordinate (COO) arrays.
let a0Values: [Float] = [10, 20, 5, 50]
let A0 = SparseConvertFromCoordinate(3, 3,
                                     4, 1,
                                     SparseAttributes_t(),
                                     rowIndices, columnIndices,
                                     a0Values)

// Create the double-precision coefficient matrix `A1` from coordinate (COO) arrays.
let a1Values: [Double] = [5, 10, 2.5, 25]
let A1 = SparseConvertFromCoordinate(3, 3,
                                     4, 1,
                                     SparseAttributes_t(),
                                     rowIndices, columnIndices,
                                     a1Values)

// Compute the symbolic factorization from the structure of either coefficient matrix.
let structure = A0.structure
let symbolicFactorization = SparseFactor(SparseFactorizationQR,
                                         structure)

// Compute the factors of `A0` using the symbolic factorization.
let factorization0 = SparseFactor(symbolicFactorization, A0)

// Solve `A0 · x = b0` in place.
var b0Values: [Float] = [30, 35, 100]
b0Values.withUnsafeMutableBufferPointer { bPtr in
    let xb = DenseVector_Float(count: 3,
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization0, xb)
}

// Compute the factors of `A1` using the symbolic factorization.
let factorization1 = SparseFactor(symbolicFactorization, A1)

// Solve `A1 · x = b1` in place.
var b1Values: [Double] = [60, 70, 200]
b1Values.withUnsafeMutableBufferPointer { bPtr in
    let xb = DenseVector_Double(count: 3,
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization1, xb)
}

print(b0Values) // Prints "[1.0, 2.0, 3.0]".
print(b1Values) // Prints "[4.0, 8.0, 12.0]".
SparseCleanup(A0)
SparseCleanup(A1)
SparseCleanup(factorization0)
SparseCleanup(factorization1)
```

**Objective-C**:

```objc
// Define the sparsity pattern of matrices `A0` and `A1`.
int rowIndices[]    = {0, 1, 1, 2};
int columnIndices[] = {2, 0, 2, 1};

// Create the single-precision coefficient matrix `A0` from coordinate (COO) arrays.
float a0Values[] = {10, 20, 5, 50};
SparseMatrix_Float A0 = SparseConvertFromCoordinate(3, 3,
                                                    4, 1,
                                                    (SparseAttributes_t){0},
                                                    rowIndices, columnIndices,
                                                    a0Values);

// Create the double-precision coefficient matrix `A1` from coordinate (COO) arrays.
double a1Values[] = {5, 10, 2.5, 25};
SparseMatrix_Double A1 = SparseConvertFromCoordinate(3, 3,
                                                     4, 1,
                                                     (SparseAttributes_t){0},
                                                     rowIndices, columnIndices,
                                                     a1Values);

// Compute the symbolic factorization from the structure of either coefficient matrix.
SparseOpaqueSymbolicFactorization symbolicFactorization = SparseFactor(SparseFactorizationQR,
                                                                       A0.structure);

// Compute the factors of `A0` using the symbolic factorization with numeric options.
SparseNumericFactorOptions nfoptions = (SparseNumericFactorOptions){0};
SparseOpaqueFactorization_Float factorization0 = SparseFactor(symbolicFactorization, A0,
                                                              nfoptions);

// Solve `A0 · x = b0` in place.
float b0Values[] = {30, 35, 100};
DenseVector_Float xb0 = { .count = 3, .data = b0Values };
SparseSolve(factorization0, xb0);

// Compute the factors of `A1` using the symbolic factorization.
SparseOpaqueFactorization_Double factorization1 = SparseFactor(symbolicFactorization, A1);

// Solve `A1 · x = b1` in place.
double b1Values[] = {60, 70, 200};
DenseVector_Double xb1 = { .count = 3, .data = b1Values };
SparseSolve(factorization1, xb1);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", b0Values[0], b0Values[1], b0Values[2]);
// Prints "[4, 8, 12]".
printf("[%g, %g, %g]\n", b1Values[0], b1Values[1], b1Values[2]);

SparseCleanup(A0);
SparseCleanup(A1);
SparseCleanup(factorization0);
SparseCleanup(factorization1);
```

On return, `b0Values` contains the values `[1.0, 2.0, 3.0]`, and `b1Values` contains the values `[4.0, 8.0, 12.0]`.

## Parameters

- `SymbolicFactor`: A symbolic factorization that returns by calling [`SparseFactor(_:_:_:_:_:)`](./sparsefactor%28_,_,_,_,_%29-8afz.md).
- `Matrix`: The matrix to factorize.
- `nfoptions`: The numeric factor options, such as pivoting parameters.

## See Also

### Related Documentation
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructure) -> SparseOpaqueSymbolicFactorization](./sparsefactor%28_,_%29-3697o.md)
  Returns a symbolic factorization of the requested type for a specified sparsity structure.
### Matrix factorizations using precalculated symbolic factorization
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Double) -> SparseOpaqueFactorization_Double](./sparsefactor%28_,_%29-58oq8.md)
  Returns the factorization of a sparse matrix of double-precision values that corresponds to the supplied symbolic factorization.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Float) -> SparseOpaqueFactorization_Float](./sparsefactor%28_,_%29-1p6im.md)
  Returns the factorization of a sparse matrix of single-precision values that corresponds to the supplied symbolic factorization.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Double, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Double](./sparsefactor%28_,_,_%29-3ddg.md)
  Returns the factorization of a sparse matrix of double-precision values that corresponds to the supplied symbolic factorization using specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:_:)-797fl)*
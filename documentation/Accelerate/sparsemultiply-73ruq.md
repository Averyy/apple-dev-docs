# SparseMultiply(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation *Y = alpha * AX* on a sparse matrix of double-precision, floating-point values.

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
func SparseMultiply(_ alpha: Double, _ A: SparseMatrix_Double, _ X: DenseMatrix_Double, _ Y: DenseMatrix_Double)
```

#### Discussion

Use this function to multiply a scalar value by a sparse matrix, and then by a dense matrix. The following equation is an example of a scalar-matrix-matrix multiplication where the first matrix is sparse:

![A mathematical formula that describes the matrix multiplication, Y equals alpha times A X. A scalar value multiplied by a four-by-four matrix multiplied by a four-by-two matrix equals a four-by-two matrix.](/images/com.apple.accelerate/media-3703074@2x.png)

Call [`SparseMultiply(_:_:_:_:)`](sparsemultiply(_:_:_:_:)-73ruq.md)to calculate the result.

**Swift**:

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data = [1.0, 4.0, 13.0, 16.0]

// The sparse matrix `A` in `Y = alpha * AX`.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

// The values for `X` in `Y = alpha * AX`.
var xValues = [10.0, -1.0, -1.0, 10.0,
               100.0, -1.0, -1.0, 100.0]

let alpha = 2.0

// The values for `Y` in `Y = alpha * AX`.
let yValues = [Double](unsafeUninitializedCapacity: xValues.count) {
    resultBuffer, count in
    
    xValues.withUnsafeMutableBufferPointer { denseMatrixPtr in
        // The dense matrix `X` in `Y = alpha * AX`.
        let X = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: denseMatrixPtr.baseAddress!)
        
        // The dense matrix `Y` in `Y = alpha * AX`.
        let Y = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: resultBuffer.baseAddress!)
        
        SparseMultiply(alpha, A, X, Y)
    }
    
    count = xValues.count
}

print(yValues) // Prints "[280.0, 0.0, 0.0, 400.0, 2800.0, 0.0, 0.0, 4000.0]".
```

**Objective-C**:

```objc
// Build the sparse matrix `A` from COO arrays.
int rowIndices[]    = {0, 3, 0, 3};
int columnIndices[] = {0, 0, 3, 3};
double aValues[]    = {1.0, 4.0, 13.0, 16.0};

SparseMatrix_Double A = SparseConvertFromCoordinate(4, 4,
                                                    4, 1,
                                                    (SparseAttributes_t){0},
                                                    rowIndices, columnIndices,
                                                    aValues);

// The dense matrix `X` in `Y = alpha * AX`.
double xValues[] = {10.0, -1.0, -1.0, 10.0,
                    100.0, -1.0, -1.0, 100.0};

double alpha = 2.0;

// The dense matrix `Y` in `Y = alpha * AX` (output buffer).
double yValues[8] = {0};

DenseMatrix_Double X = {
    .rowCount     = 4,
    .columnCount  = 2,
    .columnStride = 4,
    .attributes   = (SparseAttributes_t){0},
    .data         = xValues
};

DenseMatrix_Double Y = {
    .rowCount     = 4,
    .columnCount  = 2,
    .columnStride = 4,
    .attributes   = (SparseAttributes_t){0},
    .data         = yValues
};

SparseMultiply(alpha, A, X, Y);

// Prints "[280, 0, 0, 400, 2800, 0, 0, 4000]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
      yValues[0], yValues[1], yValues[2], yValues[3],
      yValues[4], yValues[5], yValues[6], yValues[7]);

SparseCleanup(A);
```

## Parameters

- `alpha`: The scalar value *alpha* in *Y = alpha * AX*.
- `A`: The sparse matrix *A* in *Y* *= AX*.
- `X`: The dense matrix *X* in *Y* *= AX*.
- `Y`: The dense matrix *Y* in *Y* *= AX*.

## See Also

- [func SparseMultiply(SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiply(_:_:_:)-8d9lh.md)
  Performs the multiply operation *Y* *= AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiply(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiply(_:_:_:)-9kraw.md)
  Performs the multiply operation *Y* *= AX*_ _on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiply(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiply(_:_:_:_:)-2qh3a.md)
  Performs the multiply operation *Y = alpha * AX* on a sparse matrix of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:_:)-73ruq)*
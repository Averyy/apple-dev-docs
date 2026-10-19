# SparseMultiplyAdd(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation *Y += AX* on a sparse matrix of single-precision, floating-point values.

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
func SparseMultiplyAdd(_ A: SparseMatrix_Float, _ X: DenseMatrix_Float, _ Y: DenseMatrix_Float)
```

#### Discussion

Use this function to multiply a sparse matrix by a dense matrix and accumulate the result. The following equation is an example of a matrix-matrix multiplication where the first matrix is sparse:

![A mathematical formula that describes the matrix multiplication, Y plus-equals A X. A four-by-two matrix added to a four-by-four matrix multiplied by a four-by-two matrix equals a four-by-two matrix.](/images/com.apple.accelerate/media-3703077@2x.png)

Call [`SparseMultiplyAdd(_:_:_:_:)`](sparsemultiplyadd(_:_:_:_:)-86gfz.md) to calculate the result.

**Swift**:

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data: [Float] = [1.0, 4.0, 13.0, 16.0]

// The sparse matrix `A` in `Y+=AX`.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

// The values for `X` in `Y+=AX`.
var xValues: [Float] = [10.0, -1.0, -1.0, 10.0,
               100.0, -1.0, -1.0, 100.0]

// The values for `Y` in `Y+=AX`.
var yValues = [Float](repeating: 1,
                       count: xValues.count)

yValues.withUnsafeMutableBufferPointer { yValuesPtr in
    xValues.withUnsafeMutableBufferPointer { denseMatrixPtr in
        // The dense matrix `X` in `Y+=AX`.
        let X = DenseMatrix_Float(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: denseMatrixPtr.baseAddress!)
        
        // The dense matrix `Y` in `Y+=AX`.
        let Y = DenseMatrix_Float(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: yValuesPtr.baseAddress!)
        
        SparseMultiplyAdd(A, X, Y)
    }
}

print(yValues) // Prints "[141.0, 1.0, 1.0, 201.0, 1401.0, 1.0, 1.0, 2001.0]".
```

**Objective-C**:

```objc
// Build the sparse matrix `A` (Float, 4 by 4, 4 nonzeros).
int rowIndices[]    = {0, 3, 0, 3};
int columnIndices[] = {0, 0, 3, 3};
float data[]        = {1.0f, 4.0f, 13.0f, 16.0f};

SparseMatrix_Float A = SparseConvertFromCoordinate(4, 4,
                                                   4, 1,
                                                   (SparseAttributes_t){0},
                                                   rowIndices, columnIndices,
                                                   data);

// The values for `X` in `Y+=AX` (4 by 2 column-major: `col0` then `col1`).
float xValues[] = {10.0f, -1.0f, -1.0f, 10.0f,
                   100.0f, -1.0f, -1.0f, 100.0f};

// The values for `Y` in `Y+=AX` (initial values, all ones).
float yValues[] = {1.0f, 1.0f, 1.0f, 1.0f,
                   1.0f, 1.0f, 1.0f, 1.0f};

DenseMatrix_Float X = {
    .rowCount     = 4,
    .columnCount  = 2,
    .columnStride = 4,
    .attributes   = (SparseAttributes_t){0},
    .data         = xValues
};

DenseMatrix_Float Y = {
    .rowCount     = 4,
    .columnCount  = 2,
    .columnStride = 4,
    .attributes   = (SparseAttributes_t){0},
    .data         = yValues
};

SparseMultiplyAdd(A, X, Y);

// Prints "[ 141, 1, 1, 201, 1401, 1, 1, 2001 ]".
printf("[ %g, %g, %g, %g, %g, %g, %g, %g ]\n",
      yValues[0], yValues[1], yValues[2], yValues[3],
      yValues[4], yValues[5], yValues[6], yValues[7]);

SparseCleanup(A);
```

## Parameters

- `A`: The sparse matrix *A* in *Y* *+= AX*.
- `X`: The dense matrix *X* in *Y* *+= AX*.
- `Y`: The dense matrix *Y* in *Y* *+= AX*.

## See Also

- [func SparseMultiplyAdd(SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiplyadd(_:_:_:)-lgm5.md)
  Performs the multiply operation *Y += AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(Double, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiplyadd(_:_:_:_:)-86gfz.md)
  Performs the multiply operation *Y += alpha * AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiplyadd(_:_:_:_:)-n61k.md)
  Performs the multiply operation *Y += alpha * AX* on a sparse matrix of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:)-8pgpq)*
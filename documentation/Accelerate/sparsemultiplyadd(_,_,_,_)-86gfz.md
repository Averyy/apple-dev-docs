# SparseMultiplyAdd(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiply operation *Y += alpha \* AX* on a sparse matrix of double-precision, floating-point values.

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
func SparseMultiplyAdd(_ alpha: Double, _ A: SparseMatrix_Double, _ X: DenseMatrix_Double, _ Y: DenseMatrix_Double)
```

```c
static void SparseMultiplyAdd(double alpha, SparseMatrix_Double A, DenseMatrix_Double X, DenseMatrix_Double Y);
```

## Discussion

Use this function to multiply a scalar value by a sparse matrix, then by a dense matrix, and accumulate the result. The following equation is an example of a matrix-matrix multiplication where the first matrix is sparse:

![A mathematical formula that describes the matrix multiplication, Y plus-equals alpha times A X. A four-by-two matrix added to a scalar value multiplied by a four-by-four matrix multiplied by a four-by-two matrix equals a four-by-two matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703078@2x.png)

Call [`SparseMultiplyAdd(_:_:_:_:)`](./sparsemultiplyadd%28_,_,_,_%29-3oa6n.md) to calculate the result.

**Swift**:

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data = [1.0, 4.0, 13.0, 16.0]

// The sparse matrix `A` in `Y+=alpha*AX`.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

// The values for `X` in `Y+=alpha*AX`.
var xValues = [10.0, -1.0, -1.0, 10.0,
               100.0, -1.0, -1.0, 100.0]

// The values for `Y` in `Y+=alpha*AX`.
var yValues = [Double](repeating: 1,
                       count: xValues.count)

let alpha = 2.0

yValues.withUnsafeMutableBufferPointer { yValuesPtr in
    xValues.withUnsafeMutableBufferPointer { denseMatrixPtr in
        // The dense matrix `X` in `Y+=alpha*AX`.
        let X = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: denseMatrixPtr.baseAddress!)
        
        // The dense matrix `Y` in `Y+=alpha*AX`.
        let Y = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: yValuesPtr.baseAddress!)
        
        SparseMultiplyAdd(alpha, A, X, Y)
    }
}

print(yValues) // Prints "[281.0, 1.0, 1.0, 401.0, 2801.0, 1.0, 1.0, 4001.0]".
```

**Objective-C**:

```objc
// Build the sparse matrix `A` (Double, 4 by 4, 4 nonzeros).
int rowIndices[]    = {0, 3, 0, 3};
int columnIndices[] = {0, 0, 3, 3};
double data[]       = {1.0, 4.0, 13.0, 16.0};

SparseMatrix_Double A = SparseConvertFromCoordinate(4, 4,
                                                    4, 1,
                                                    (SparseAttributes_t){0},
                                                    rowIndices, columnIndices,
                                                    data);

// The values for `X` in `Y+=alpha*AX` (4x2 column-major).
double xValues[] = {10.0, -1.0, -1.0, 10.0,
                    100.0, -1.0, -1.0, 100.0};

// The values for `Y` in `Y+=alpha*AX` (initial values, all ones).
double yValues[] = {1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0};

double alpha = 2.0;

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

SparseMultiplyAdd(alpha, A, X, Y);

// Prints "[ 281, 1, 1, 401, 2801, 1, 1, 4001 ]".
printf("[ %g, %g, %g, %g, %g, %g, %g, %g ]\n",
      yValues[0], yValues[1], yValues[2], yValues[3],
      yValues[4], yValues[5], yValues[6], yValues[7]);

SparseCleanup(A);
```

## Parameters

- `alpha`: The scalar value *alpha* in *Y += alpha \* AX*.
- `A`: The sparse matrix *A* in *Y* *+= AX*.
- `X`: The dense matrix *X* in *Y* *+= AX*.
- `Y`: The dense matrix *Y* in *Y* *+= AX*.

## See Also

### Multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiplyadd%28_,_,_%29-lgm5.md)
  Performs the multiply operation *Y += AX* on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiplyadd%28_,_,_%29-8pgpq.md)
  Performs the multiply operation *Y += AX* on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiplyAdd(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiplyadd%28_,_,_,_%29-n61k.md)
  Performs the multiply operation *Y += alpha \* AX* on a sparse matrix of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:_:)-86gfz)*
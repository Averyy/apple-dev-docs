# SparseMultiplyAdd(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation  on a sparse matrix of single-precision, floating-point values.

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
func SparseMultiplyAdd(_ alpha: Float, _ A: SparseMatrix_Float, _ X: DenseMatrix_Float, _ Y: DenseMatrix_Float)
```

#### Discussion

Use this function to multiply a scalar value by a sparse matrix, then by a dense matrix, and accumulate the result. The following equation is an example of a matrix-matrix multiplication where the first matrix is sparse:

![A mathematical formula that describes the matrix multiplication, Y plus-equals alpha times A X. A four-by-two matrix added to a scalar value multiplied by a four-by-four matrix multiplied by a four-by-two matrix equals a four-by-two matrix.](https://docs-assets.developer.apple.com/published/4fa2f6ea2f3d3796488891c3737aa224/media-3703072%402x.png)

Call [`SparseMultiplyAdd(_:_:_:_:)`](sparsemultiplyadd(_:_:_:_:)-3oa6n.md) to calculate the result.

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data: [Float] = [1.0, 4.0, 13.0, 16.0]

/// The _A_ in _Y += alpha * AX_.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

/// The values for _X_ in _Y += alpha * AX_.
var xValues: [Float] = [10.0, -1.0, -1.0, 10.0,
                        100.0, -1.0, -1.0, 100.0]

/// The values for _Y_ in _Y += alpha * AX_.
var yValues = [Float](repeating: 1,
                      count: xValues.count)

let alpha: Float = 2.0

yValues.withUnsafeMutableBufferPointer { yValuesPtr in
    xValues.withUnsafeMutableBufferPointer { denseMatrixPtr in
        /// The _X_ in _Y += alpha * AX_.
        let X = DenseMatrix_Float(rowCount: 4,
                                  columnCount: 2,
                                  columnStride: 4,
                                  attributes: SparseAttributes_t(),
                                  data: denseMatrixPtr.baseAddress!)
        
        /// The _Y_ in _Y += alpha * AX_.
        let Y = DenseMatrix_Float(rowCount: 4,
                                  columnCount: 2,
                                  columnStride: 4,
                                  attributes: SparseAttributes_t(),
                                  data: yValuesPtr.baseAddress!)
        
        SparseMultiplyAdd(alpha, A, X, Y)
    }
}

// On return, `yValues` contains:
//      `[ 281.0, 1.0, 1.0,  401.0,
//        2801.0, 1.0, 1.0, 4001.0]`
```

## Parameters

- `alpha`: The scalar value   in  .
- `A`: The sparse matrix   in    .
- `X`: The dense matrix   in    .
- `Y`: The dense matrix   in    .

## See Also

- [func SparseMultiplyAdd(SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiplyadd(_:_:_:)-lgm5.md)
  Performs the multiply operation  on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiplyadd(_:_:_:)-8pgpq.md)
  Performs the multiply operation  on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiplyAdd(Double, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiplyadd(_:_:_:_:)-86gfz.md)
  Performs the multiply operation  on a sparse matrix of double-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:_:)-n61k)*
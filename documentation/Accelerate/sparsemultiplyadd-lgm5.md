# SparseMultiplyAdd(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation  on a sparse matrix of double-precision, floating-point values.

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
func SparseMultiplyAdd(_ A: SparseMatrix_Double, _ X: DenseMatrix_Double, _ Y: DenseMatrix_Double)
```

#### Discussion

Use this function to multiply a sparse matrix by a dense matrix and accumulate the result. The following equation is an example of a matrix-matrix multiplication where the first matrix is sparse:

![A mathematical formula that describes the matrix multiplication, Y plus-equals A X. A four-by-two matrix added to a four-by-four matrix multiplied by a four-by-two matrix equals a four-by-two matrix.](https://docs-assets.developer.apple.com/published/e029142a5f614d3389db33aca356c7f8/media-3703073%402x.png)

Call [`SparseMultiplyAdd(_:_:_:_:)`](sparsemultiplyadd(_:_:_:_:)-86gfz.md) to calculate the result.

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data = [1.0, 4.0, 13.0, 16.0]

/// The _A_ in _Y+=AX_.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

/// The values for _X_ in _Y+=AX_.
var xValues = [10.0, -1.0, -1.0, 10.0,
               100.0, -1.0, -1.0, 100.0]

/// The values for _Y_ in _Y+=AX_.
var yValues = [Double](repeating: 1,
                       count: xValues.count)

yValues.withUnsafeMutableBufferPointer { yValuesPtr in
    xValues.withUnsafeMutableBufferPointer { denseMatrixPtr in
        /// The _X_ in _Y+=AX_.
        let X = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: denseMatrixPtr.baseAddress!)
        
        /// The _Y_ in _Y+=AX_.
        let Y = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: yValuesPtr.baseAddress!)
        
        SparseMultiplyAdd(A, X, Y)
    }
}

// On return, `yValues` contains:
//      `[ 141.0, 1.0, 1.0,  201.0,
//        1401.0, 1.0, 1.0, 2001.0]`
```

## Parameters

- `A`: The sparse matrix   in    .
- `X`: The dense matrix   in    .
- `Y`: The dense matrix   in    .

## See Also

- [func SparseMultiplyAdd(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiplyadd(_:_:_:)-8pgpq.md)
  Performs the multiply operation  on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiplyAdd(Double, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiplyadd(_:_:_:_:)-86gfz.md)
  Performs the multiply operation  on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiplyAdd(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiplyadd(_:_:_:_:)-n61k.md)
  Performs the multiply operation  on a sparse matrix of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:)-lgm5)*
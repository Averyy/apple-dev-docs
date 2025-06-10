# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation   on a sparse matrix of double-precision, floating-point values.

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
func SparseMultiply(_ A: SparseMatrix_Double, _ X: DenseMatrix_Double, _ Y: DenseMatrix_Double)
```

#### Discussion

Use this function to multiply a sparse matrix by a dense matrix. The following equation is an example of a matrix-matrix multiplication where the first matrix is sparse:

![A mathematical formula that describes the matrix multiplication, Y equals A X. A four-by-four matrix multiplied by a four-by-two matrix equals a four-by-two matrix.](https://docs-assets.developer.apple.com/published/4c75eafee05a235819455ecad61e1951/media-3703079%402x.png)

Call [`SparseMultiply(_:_:_:)`](sparsemultiply(_:_:_:)-8d9lh.md) to calculate the result.

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data = [1.0, 4.0, 13.0, 16.0]

/// The _A_ in _Y=AX_.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

/// The values for _X_ in _Y=AX_.
var xValues = [10.0, -1.0, -1.0, 10.0,
               100.0, -1.0, -1.0, 100.0]

/// The values for _Y_ in _Y=AX_.
let yValues = [Double](unsafeUninitializedCapacity: xValues.count) {
    resultBuffer, count in
    
    xValues.withUnsafeMutableBufferPointer { denseMatrixPtr in
        /// The _X_ in _Y=AX_.
        let X = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: denseMatrixPtr.baseAddress!)
        
        /// The _Y_ in _Y=AX_.
        let Y = DenseMatrix_Double(rowCount: 4,
                                   columnCount: 2,
                                   columnStride: 4,
                                   attributes: SparseAttributes_t(),
                                   data: resultBuffer.baseAddress!)
        
        SparseMultiply(A, X, Y)
    }
    
    count = xValues.count
}

// On return, `yValues` contains:
//      `[ 140.0, 0.0, 0.0,  200.0,
//        1400.0, 0.0, 0.0, 2000.0]`
```

## Parameters

- `A`: The sparse matrix   in    .
- `X`: The dense matrix   in    .
- `Y`: The dense matrix   in    .

## See Also

- [func SparseMultiply(SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiply(_:_:_:)-9kraw.md)
  Performs the multiply operation  _ _on a sparse matrix of single-precision, floating-point values.
- [func SparseMultiply(Double, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsemultiply(_:_:_:_:)-73ruq.md)
  Performs the multiply operation  on a sparse matrix of double-precision, floating-point values.
- [func SparseMultiply(Float, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsemultiply(_:_:_:_:)-2qh3a.md)
  Performs the multiply operation  on a sparse matrix of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-8d9lh)*
# SparseMultiplyAdd(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation  on a vector of single-precision, floating-point values.

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
func SparseMultiplyAdd(_ alpha: Float, _ A: SparseMatrix_Float, _ x: DenseVector_Float, _ y: DenseVector_Float)
```

#### Discussion

Use this function to multiply a scalar by a sparse matrix, then by a dense vector, and accumulate the result. The following equation is an example of a matrix-vector multiplication where the matrix is sparse:

![A mathematical formula that describes the matrix multiplication, y plus-equals alpha times A x. A four-element column matrix added to a scalar value multiplied by a four-by-four matrix multiplied by a four-element column matrix equals a four-element column matrix.](https://docs-assets.developer.apple.com/published/906f157e112f16ab854420c9df492c37/media-3703087%402x.png)

Call [`SparseMultiplyAdd(_:_:_:_:)`](sparsemultiplyadd(_:_:_:_:)-3oa6n.md) to calculate the result.

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data: [Float] = [1.0, 4.0, 13.0, 16.0]

/// The _A_ in _y+=Ax_.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

/// The values for _x_ in _y+=Ax_.
var xValues: [Float] = [10.0, -1.0, -1.0, 10.0]

var yValues: [Float] = [1.0, 1.0, 1.0, 1.0]

let alpha: Float = 2.0

/// The values for _y_ in _y+=Ax_.
yValues.withUnsafeMutableBufferPointer { yValuesPtr in
    
    xValues.withUnsafeMutableBufferPointer { xValuesPtr in
        /// The _x_ in _y+=Ax_.
        let x = DenseVector_Float(count: 4,
                                  data: xValuesPtr.baseAddress!)
        
        /// The _y_ in _y+=Ax_.
        let y = DenseVector_Float(count: 4,
                                  data: yValuesPtr.baseAddress!)
        
        SparseMultiplyAdd(alpha, A, x, y)
    }
}

/// On return, `yValues` contains:
///      `[ 281.0, 1.0, 1.0, 401.0 ]`
```

## Parameters

- `alpha`: The scalar value   in    .
- `A`: The sparse matrix   in    .
- `x`: The dense vector   in    .
- `y`: The dense vector   in    .

## See Also

- [func SparseMultiplyAdd(SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](sparsemultiplyadd(_:_:_:)-7iuo9.md)
  Performs the multiply operation  on a vector of double-precision, floating-point values.
- [func SparseMultiplyAdd(SparseMatrix_Float, DenseVector_Float, DenseVector_Float)](sparsemultiplyadd(_:_:_:)-ineu.md)
  Performs the multiply operation  on a vector of double-precision, floating-point values.
- [func SparseMultiplyAdd(Double, SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](sparsemultiplyadd(_:_:_:_:)-3oa6n.md)
  Performs the multiply operation  on a vector of double-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:_:)-8n6xy)*
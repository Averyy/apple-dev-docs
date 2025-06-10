# SparseMultiply(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs the multiply operation   on a vector of single-precision, floating-point values.

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
func SparseMultiply(_ alpha: Float, _ A: SparseMatrix_Float, _ x: DenseVector_Float, _ y: DenseVector_Float)
```

#### Discussion

Use this function to multiply a scalar by a sparse matrix, and then by a dense vector. The following equation is an example of a scalar-matrix-vector multiplication where the matrix is sparse:

![A mathematical formula that describes the matrix multiplication, y equals alpha times A x. A scalar value multiplied by a four-by-four matrix multiplied by a four-element column matrix equals a four-element column matrix.](https://docs-assets.developer.apple.com/published/15715d20812b25e9a1a02140fdc1f085/media-3703089%402x.png)

Call [`SparseMultiply(_:_:_:_:)`](sparsemultiply(_:_:_:_:)-76o5l.md) to calculate the result.

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data: [Float] = [1.0, 4.0, 13.0, 16.0]

/// The _A_ in _y = alpha * Ax_.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

/// The values for _x_ in _y = alpha * Ax_.
var xValues: [Float] = [10.0, -1.0, -1.0, 10.0]

let alpha: Float = 2.0

/// The values for _y_ in _y = alpha * Ax_.
let yValues = [Float](unsafeUninitializedCapacity: xValues.count) {
    resultBuffer, count in
    
    xValues.withUnsafeMutableBufferPointer { xValuesPtr in
        /// The _x_ in _y = alpha * Ax_.
        let x = DenseVector_Float(count: 4, 
                                  data: xValuesPtr.baseAddress!)
        
        /// The _y_ in _y = alpha * Ax_.
        let y = DenseVector_Float(count: 4,
                                  data: resultBuffer.baseAddress!)
        
        SparseMultiply(alpha, A, x, y)
    }
    
    count = xValues.count
}

/// On return, `yValues` contains:
///      `[ 280.0, 0.0, 0.0,  400.0 ]`
```

## Parameters

- `alpha`: The scalar value   in    .
- `A`: The sparse matrix   in    .
- `x`: The dense vector   in    .
- `y`: The dense vector   in    .

## See Also

- [func SparseMultiply(SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](sparsemultiply(_:_:_:)-9d57s.md)
  Performs the multiplication  on a vector of double-precision, floating-point values.
- [func SparseMultiply(SparseMatrix_Float, DenseVector_Float, DenseVector_Float)](sparsemultiply(_:_:_:)-4hrs4.md)
  Performs the multiplication  on a vector of single-precision, floating-point values.
- [func SparseMultiply(Double, SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](sparsemultiply(_:_:_:_:)-76o5l.md)
  Performs the multiply operation   on a vector of double-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:_:)-8yzgo)*
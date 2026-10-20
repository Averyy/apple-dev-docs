# SparseMultiplyAdd(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiply operation *y += alpha * Ax* on a vector of single-precision, floating-point values.

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

```c
static void SparseMultiplyAdd(float alpha, SparseMatrix_Float A, DenseVector_Float x, DenseVector_Float y);
```

#### Discussion

Use this function to multiply a scalar by a sparse matrix, then by a dense vector, and accumulate the result. The following equation is an example of a matrix-vector multiplication where the matrix is sparse:

![A mathematical formula that describes the matrix multiplication, y plus-equals alpha times A x. A four-element column matrix added to a scalar value multiplied by a four-by-four matrix multiplied by a four-element column matrix equals a four-element column matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703087@2x.png)

Call [`SparseMultiplyAdd(_:_:_:_:)`](./sparsemultiplyadd%28_,_,_,_%29-3oa6n.md) to calculate the result.

**Swift**:

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data: [Float] = [1.0, 4.0, 13.0, 16.0]

// The sparse matrix `A` in `y+=alpha*Ax`.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

// The values for `x` in `y+=alpha*Ax`.
var xValues: [Float] = [10.0, -1.0, -1.0, 10.0]

var yValues: [Float] = [1.0, 1.0, 1.0, 1.0]

let alpha: Float = 2.0

// The values for `y` in `y+=alpha*Ax`.
yValues.withUnsafeMutableBufferPointer { yValuesPtr in
    
    xValues.withUnsafeMutableBufferPointer { xValuesPtr in
        // The dense vector `x` in `y+=alpha*Ax`.
        let x = DenseVector_Float(count: 4,
                                  data: xValuesPtr.baseAddress!)
        
        // The dense vector `y` in `y+=alpha*Ax`.
        let y = DenseVector_Float(count: 4,
                                  data: yValuesPtr.baseAddress!)
        
        SparseMultiplyAdd(alpha, A, x, y)
    }
}

print(yValues) // Prints "[281.0, 1.0, 1.0, 401.0]".
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

// The values for `x` in `y+=alpha*Ax`.
float xValues[] = {10.0f, -1.0f, -1.0f, 10.0f};

// The values for `y` in `y+=alpha*Ax`.
float yValues[] = {1.0f, 1.0f, 1.0f, 1.0f};

float alpha = 2.0f;

DenseVector_Float x = {
    .count = 4,
    .data  = xValues
};

DenseVector_Float y = {
    .count = 4,
    .data  = yValues
};

SparseMultiplyAdd(alpha, A, x, y);

// Prints "[ 281, 1, 1, 401 ]".
printf("[ %g, %g, %g, %g ]\n",
      yValues[0], yValues[1], yValues[2], yValues[3]);

SparseCleanup(A);
```

## Parameters

- `alpha`: The scalar value *alpha* in *y* *+= alpha * Ax*.
- `A`: The sparse matrix *A* in *y* *+= Ax*.
- `x`: The dense vector *x* in *y* *+= Ax*.
- `y`: The dense vector *y* in *y* *+= Ax*.

## See Also

### Multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](./sparsemultiplyadd%28_,_,_%29-7iuo9.md)
  Performs the multiply operation *y += Ax* on a vector of double-precision, floating-point values.
- [func SparseMultiplyAdd(SparseMatrix_Float, DenseVector_Float, DenseVector_Float)](./sparsemultiplyadd%28_,_,_%29-ineu.md)
  Performs the multiply operation *y += Ax* on a vector of double-precision, floating-point values.
- [func SparseMultiplyAdd(Double, SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](./sparsemultiplyadd%28_,_,_,_%29-3oa6n.md)
  Performs the multiply operation *y += alpha * Ax* on a vector of double-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:_:)-8n6xy)*
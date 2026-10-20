# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiplication *y = Ax* on a vector of double-precision, floating-point values.

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
func SparseMultiply(_ A: SparseMatrix_Double, _ x: DenseVector_Double, _ y: DenseVector_Double)
```

```c
static void SparseMultiply(SparseMatrix_Double A, DenseVector_Double x, DenseVector_Double y);
```

#### Discussion

Use this function to multiply a sparse matrix by a dense vector. The following equation is an example of a matrix-vector multiplication where the matrix is sparse:

![A mathematical formula that describes the matrix multiplication, y equals A x. A four-by-four matrix multiplied by a four-element column matrix equals a four-element column matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703085@2x.png)

Call [`SparseMultiply(_:_:_:)`](./sparsemultiply%28_,_,_%29-9d57s.md) to calculate the result.

**Swift**:

```swift
let rowCount = Int32(4)
let columnCount = Int32(4)
let blockCount = 4
let blockSize = UInt8(1)
let rowIndices: [Int32] = [0, 3, 0, 3]
let columnIndices: [Int32] = [0, 0, 3, 3]
let data = [1.0, 4.0, 13.0, 16.0]

// The sparse matrix `A` in `y=Ax`.
let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    blockCount, blockSize,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    data)
defer {
    SparseCleanup(A)
}

// The values for `x` in `y=Ax`.
var xValues = [10.0, -1.0, -1.0, 10.0]

// The values for `y` in `y=Ax`.
let yValues = [Double](unsafeUninitializedCapacity: xValues.count) {
    resultBuffer, count in
    
    xValues.withUnsafeMutableBufferPointer { xValuesPtr in
        // The dense vector `x` in `y=Ax`.
        let x = DenseVector_Double(count: 4, 
                                   data: xValuesPtr.baseAddress!)
        
        // The dense vector `y` in `y=Ax`.
        let y = DenseVector_Double(count: 4,
                                   data: resultBuffer.baseAddress!)
        
        SparseMultiply(A, x, y)
    }
    
    count = xValues.count
}

print(yValues) // Prints "[140.0, 0.0, 0.0, 200.0]".
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

// The dense vector `x` in `y=Ax`.
double xValues[] = {10.0, -1.0, -1.0, 10.0};

// The dense vector `y` in `y=Ax` (output buffer).
double yValues[4] = {0};

DenseVector_Double x = { .count = 4, .data = xValues };
DenseVector_Double y = { .count = 4, .data = yValues };

SparseMultiply(A, x, y);

// Prints "[140, 0, 0, 200]".
printf("[%g, %g, %g, %g]\n",
      yValues[0], yValues[1], yValues[2], yValues[3]);

SparseCleanup(A);
```

## Parameters

- `A`: The sparse matrix *A* in *y* *= Ax*.
- `x`: The dense vector *x* in *y* *= Ax*.
- `y`: The dense vector *y* in *y* *= Ax*.

## See Also

### Multiplication functions
- [func SparseMultiply(SparseMatrix_Float, DenseVector_Float, DenseVector_Float)](./sparsemultiply%28_,_,_%29-4hrs4.md)
  Performs the multiplication *y = Ax* on a vector of single-precision, floating-point values.
- [func SparseMultiply(Double, SparseMatrix_Double, DenseVector_Double, DenseVector_Double)](./sparsemultiply%28_,_,_,_%29-76o5l.md)
  Performs the multiply operation *y* *= alpha * Ax* on a vector of double-precision, floating-point values.
- [func SparseMultiply(Float, SparseMatrix_Float, DenseVector_Float, DenseVector_Float)](./sparsemultiply%28_,_,_,_%29-8yzgo.md)
  Performs the multiply operation *y* *= alpha * Ax* on a vector of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-9d57s)*
# data

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The array of contiguous values in the nonzero blocks of the matrix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var data: UnsafeMutablePointer<Double>
```

```c
double * data;
```

#### Discussion

The matrix stores each block in column-major order. The number of elements in [`data`](./data.md) must be equal to [`blockSize`](../sparsematrixstructure/blocksize.md) x [`blockSize`](../sparsematrixstructure/blocksize.md) x the number of nonzero blocks in the matrix.

## See Also

### Inspecting a Matrix’s Structure and Data
- [var structure: SparseMatrixStructure](./structure.md)
  The sparsity structure of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrix_double/data)*
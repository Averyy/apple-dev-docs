# init(structure:data:)

**Framework**: Accelerate  
**Kind**: init

Creates a sparse matrix with the specified structure that contains double-precision values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(structure: SparseMatrixStructure, data: UnsafeMutablePointer<Double>)
```

## Parameters

- `structure`: The sparsity structure of the matrix.
- `data`: The array of contiguous values in the nonzero blocks of the matrix. The matrix stores each block in column-major order. The number of elements in   must be equal to   x   x the number of nonzero blocks in the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrix_double/init(structure:data:))*
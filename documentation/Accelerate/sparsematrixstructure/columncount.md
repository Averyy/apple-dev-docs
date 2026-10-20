# columnCount

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of columns in the matrix.

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
var columnCount: Int32
```

```c
int columnCount;
```

## See Also

### Inspecting the properties of a sparse matrix description
- [var attributes: SparseAttributes_t](./attributes.md)
  The attributes of the matrix, such as whether it’s symmetrical or triangular.
- [var blockSize: UInt8](./blocksize.md)
  The block size of the matrix.
- [var columnStarts: UnsafeMutablePointer<Int>](./columnstarts.md)
  The starting index for each column in the row indices array.
- [var rowCount: Int32](./rowcount.md)
  The number of rows in the matrix.
- [var rowIndices: UnsafeMutablePointer<Int32>](./rowindices.md)
  The row indices of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrixstructure/columncount)*
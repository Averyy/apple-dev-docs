# SparseConvertFromCoordinate(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Convert from coordinate format arrays to a  matrix of complex double values, dropping out-of-range entries and summing duplicates.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseConvertFromCoordinate(_ rowCount: Int32, _ columnCount: Int32, _ blockCount: Int, _ blockSize: UInt8, _ attributes: SparseAttributesComplex_t, _ row: UnsafePointer<Int32>, _ column: UnsafePointer<Int32>, _ data: OpaquePointer, _ storage: UnsafeMutableRawPointer, _ workspace: UnsafeMutableRawPointer) -> SparseMatrix_Complex_Double
```

#### Return Value

A new `SparseMatrix_Complex_Double` object, using the memory you provided in the `storage` parameter.

#### Discussion

For symmetric (Hermitian) matrices, entries are accepted in either triangle (if they are in the “wrong” triangle as specified by attributes.triangle, they are transposed, and if an entry is already present, are treated as duplicates and summed). For triangular matrices, entries in the “wrong” triangle as specified by attributes.triangle are treated as out-of-range and dropped.

Define `storage` as a block of memory of size at least:

```None
  48 + (columnCount+1)*sizeof(long) + blockCount*sizeof(int)
    + blockCount*blockSize*blockSize*sizeof(float) * 2
```

The returned structures `.structure.columnStarts`, `.structure.rowIndices`, and `.data` will point into this storage. You are responsible for managing the allocation and cleanup of this memory.

## Parameters

- `rowCount`: (Input) Number of rows in structure.
- `columnCount`: (Input) Number of columns in structure.
- `blockCount`: (Input) Number of blocks in matrix.
- `blockSize`: (Input) Block size for data storage on both input and   output.
- `attributes`: (Input) Attributes of matrix to create. The matrix will   be forced to conform to the specified attributes by copying or dropping   elements as needed.
- `row`: (Input) Row indices of matrix structure.
- `column`: (Input) Column indices of matrix structure.
- `data`: (Input) The contents of the structurally non-zero (block)   matrix elements.
- `storage`: (Output) The output storage.
- `workspace`: (Scratch) Workspace of size  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-6ocm1)*
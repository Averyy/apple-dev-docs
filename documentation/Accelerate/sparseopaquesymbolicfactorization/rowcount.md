# rowCount

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of rows.

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
var rowCount: Int32
```

```c
int rowCount;
```

## See Also

### Inspecting a Factorization’s Structure
- [var attributes: SparseAttributes_t](./attributes.md)
  The attributes of the factorization.
- [struct SparseAttributes_t](../sparseattributes_t.md)
  A structure that represents the attributes of a matrix.
- [var blockSize: UInt8](./blocksize.md)
  The block size.
- [var columnCount: Int32](./columncount.md)
  The number of columns.
- [var workspaceSize_Double: Int](./workspacesize_double.md)
  Size, in bytes, of workspace required to perform numerical factorization in doubles.
- [var workspaceSize_Float: Int](./workspacesize_float.md)
  Size, in bytes, of workspace required to perform numerical factorization in floats.
- [var factorSize_Double: Int](./factorsize_double.md)
  Minimum size, in bytes, required to store numerical factors in doubles.
- [var factorSize_Float: Int](./factorsize_float.md)
  Minimum size, in bytes, required to store numerical factors in float.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesymbolicfactorization/rowcount)*
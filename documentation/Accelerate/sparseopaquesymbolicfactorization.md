# SparseOpaqueSymbolicFactorization

**Framework**: Accelerate  
**Kind**: struct

A semi-opaque type that represents symbolic matrix factorization.

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
struct SparseOpaqueSymbolicFactorization
```

#### Overview

Represents a symbolic matrix factorization (that is, the pattern of the factors without the values). A single symbolic factorization may be the basis for multiple numerical factorizations of matrices with the same pattern but different nonzero values.

Use the [`SparseCleanup(_:)`](sparsecleanup(_:)-6jpd8.md) function to free resources that these objects hold. The system reference-counts the internal factorize pointer, so it’s safe to destroy this object even if numeric factorizations exist that still depend on it.

## Topics

### Creating an Opaque Symbolic Factorization
- [init()](sparseopaquesymbolicfactorization/init.md)
- [init(status: SparseStatus_t, rowCount: Int32, columnCount: Int32, attributes: SparseAttributes_t, blockSize: UInt8, type: SparseFactorization_t, factorization: UnsafeMutableRawPointer?, workspaceSize_Float: Int, workspaceSize_Double: Int, factorSize_Float: Int, factorSize_Double: Int)](sparseopaquesymbolicfactorization/init(status:rowcount:columncount:attributes:blocksize:type:factorization:workspacesize_float:workspacesize_double:factorsize_float:factorsize_double:).md)
  Creates an opaque symbolic factorization.
### Instance Properties
- [var status: SparseStatus_t](sparseopaquesymbolicfactorization/status.md)
  The status of the factorization.
- [struct SparseStatus_t](sparsestatus_t.md)
  Constants that describe the status of a factorization.
- [var type: SparseFactorization_t](sparseopaquesymbolicfactorization/type.md)
  The factorization type.
- [var factorization: UnsafeMutableRawPointer?](sparseopaquesymbolicfactorization/factorization.md)
  A pointer to a private internal representation of the symbolic factor.
- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.
### Inspecting a Factorization’s Structure
- [var attributes: SparseAttributes_t](sparseopaquesymbolicfactorization/attributes.md)
  The attributes of the factorization.
- [struct SparseAttributes_t](sparseattributes_t.md)
  A structure that represents the attributes of a matrix.
- [var blockSize: UInt8](sparseopaquesymbolicfactorization/blocksize.md)
  The block size.
- [var columnCount: Int32](sparseopaquesymbolicfactorization/columncount.md)
  The number of columns.
- [var rowCount: Int32](sparseopaquesymbolicfactorization/rowcount.md)
  The number of rows.
- [var workspaceSize_Double: Int](sparseopaquesymbolicfactorization/workspacesize_double.md)
  Size, in bytes, of workspace required to perform numerical factorization in doubles.
- [var workspaceSize_Float: Int](sparseopaquesymbolicfactorization/workspacesize_float.md)
  Size, in bytes, of workspace required to perform numerical factorization in floats.
- [var factorSize_Double: Int](sparseopaquesymbolicfactorization/factorsize_double.md)
  Minimum size, in bytes, required to store numerical factors in doubles.
- [var factorSize_Float: Int](sparseopaquesymbolicfactorization/factorsize_float.md)
  Minimum size, in bytes, required to store numerical factors in float.

## See Also

- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.
- [struct SparseSymbolicFactorOptions](sparsesymbolicfactoroptions.md)
  A structure that contains options that affect the symbolic stage of a sparse factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesymbolicfactorization)*
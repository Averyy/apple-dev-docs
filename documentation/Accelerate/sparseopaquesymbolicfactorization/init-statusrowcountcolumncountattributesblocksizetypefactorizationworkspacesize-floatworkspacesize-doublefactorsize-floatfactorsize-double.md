# init(status:rowCount:columnCount:attributes:blockSize:type:factorization:workspaceSize_Float:workspaceSize_Double:factorSize_Float:factorSize_Double:)

**Framework**: Accelerate  
**Kind**: init

Creates an opaque symbolic factorization.

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
init(status: SparseStatus_t, rowCount: Int32, columnCount: Int32, attributes: SparseAttributes_t, blockSize: UInt8, type: SparseFactorization_t, factorization: UnsafeMutableRawPointer?, workspaceSize_Float: Int, workspaceSize_Double: Int, factorSize_Float: Int, factorSize_Double: Int)
```

#### Return Value

A new opaque symbolic factorization.

## Parameters

- `status`: The status of the factorization.
- `rowCount`: The number of rows.
- `columnCount`: The number of columns.
- `attributes`: The attributes of the factorization.
- `blockSize`: The block size.
- `type`: The factorization type.
- `factorization`: A pointer to a private internal representation of the symbolic factor.
- `workspaceSize_Float`: The size in bytes of workspace necessary to perform numerical factorization in [`Float`](https://developer.apple.com/documentation/Swift/Float).
- `workspaceSize_Double`: The size in bytes of workspace necessary to perform numerical factorization in [`Double`](https://developer.apple.com/documentation/Swift/Double).
- `factorSize_Float`: The minimum size in bytes necessary to store numerical factors in [`Float`](https://developer.apple.com/documentation/Swift/Float).
- `factorSize_Double`: The minimum size in bytes necessary to store numerical factors in [`Double`](https://developer.apple.com/documentation/Swift/Double).

## See Also

- [init()](sparseopaquesymbolicfactorization/init.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesymbolicfactorization/init(status:rowcount:columncount:attributes:blocksize:type:factorization:workspacesize_float:workspacesize_double:factorsize_float:factorsize_double:))*
# symbolicFactorization

**Framework**: Accelerate  
**Kind**: property

A semi-opaque type representing symbolic matrix factorization.

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
var symbolicFactorization: SparseOpaqueSymbolicFactorization
```

#### Discussion

Represents a symbolic matrix factorization (i.e. the pattern of the factors without the values). A single symbolic factorization may be the basis for multiple numerical factorizations of matrices with the same pattern but different values non-zero values.

```None
        Use the `SparseCleanup` function to free resources held by these
        objects. The internal factorization pointer is refence counted,
        so it is safe to destroy this object even if numeric
        factorizations exist that still depend on it.
```

- **`status`**: Indicates status of factorization object.
- **`type`**: Type fo factorization this represents.
- **`rowCount`**: Copy of field from `SparseMatrixStructure` passed to `SparseFactor` call used to construct this symbolic factorization.
- **`columnCount`**: Copy of field from `SparseMatrixStructure` passed to `SparseFactor` call used to construct this symbolic factorization.
- **`attributes`**: Copy of field from `SparseMatrixStructure` passed to `SparseFactor` call used to construct this symbolic factorization.
- **`blockSize`**: Copy of field from `SparseMatrixStructure` passed to `SparseFactor` call used to construct this symbolic factorization.
- **`factorization`**: Pointer to private internal representation of symbolic factor.
- **`workspaceSize_Float`**: Size, in bytes, of workspace required to perform numerical factorization in float. Double the size when used in complex float.
- **`workspaceSize_Double`**: Size, in bytes, of workspace required to perform numerical factorization in double. Double the size when used in complex double.
- **`factorSize_Float`**: Minimum size, in bytes, required to store numerical factors in float. If numerical pivoting requires a pivot to be delayed, the actual size required may be larger. Double the size when used in complex float.
- **`factorSize_Double`**: Minimum size, in bytes, required to store numerical factors in double. If numerical pivoting requires a pivot to be delayed, the actual size required may be larger. Double the size when used in complex double.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_complex_double/symbolicfactorization)*
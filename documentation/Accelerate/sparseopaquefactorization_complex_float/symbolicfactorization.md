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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_complex_float/symbolicfactorization)*
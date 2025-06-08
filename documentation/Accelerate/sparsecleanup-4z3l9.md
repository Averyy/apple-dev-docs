# SparseCleanup(_:)

**Framework**: Accelerate  
**Kind**: func

Release a Sparse matrix’s references to any memory allocated by the Sparse library.

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
func SparseCleanup(_ toFree: SparseMatrix_Complex_Float)
```

#### Discussion

Reports an error if the matrix was not allocated by Sparse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecleanup(_:)-4z3l9)*
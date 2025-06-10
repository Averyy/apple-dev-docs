# apply

**Framework**: Accelerate  
**Kind**: property

A function that calculates , where  is the preconditioner.

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
var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void
```

#### Discussion

The function has some approximation to .

## See Also

- [var mem: UnsafeMutableRawPointer](sparseopaquepreconditioner_float/mem.md)
  The unaltered memory pointer that passes as the first parameter of the apply function.
- [var type: SparsePreconditioner_t](sparseopaquepreconditioner_float/type.md)
  The preconditioner type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_float/apply)*
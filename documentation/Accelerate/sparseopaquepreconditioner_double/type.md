# type

**Framework**: Accelerate  
**Kind**: property

The preconditioner type.

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
var type: SparsePreconditioner_t
```

## See Also

- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void](sparseopaquepreconditioner_double/apply.md)
  A function that calculates , where  is the preconditioner.
- [var mem: UnsafeMutableRawPointer](sparseopaquepreconditioner_double/mem.md)
  The unaltered memory pointer that passes as the first parameter of the apply function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_double/type)*
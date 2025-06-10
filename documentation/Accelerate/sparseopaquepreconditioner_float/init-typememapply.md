# init(type:mem:apply:)

**Framework**: Accelerate  
**Kind**: init

Creates a new single-precision preconditioner.

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
init(type: SparsePreconditioner_t, mem: UnsafeMutableRawPointer, apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void)
```

## Parameters

- `type`: The preconditioner type.
- `mem`: The unaltered memory pointer that passes as the first parameter of the   function.
- `apply`: A function that calculates  , where   is the preconditioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_float/init(type:mem:apply:))*
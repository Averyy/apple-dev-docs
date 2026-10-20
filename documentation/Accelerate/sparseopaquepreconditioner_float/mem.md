# mem

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The unaltered memory pointer that passes as the first parameter of the apply function.

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
var mem: UnsafeMutableRawPointer
```

```c
void * mem;
```

## See Also

### Inspecting Preconditioner Properties
- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void](./apply.md)
  A function that calculates *Y = PX*, where *P* is the preconditioner.
- [var type: SparsePreconditioner_t](./type.md)
  The preconditioner type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_float/mem)*
# apply

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A function that calculates *Y = PX*, where *P* is the preconditioner.

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
var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void
```

```c
void (*)(void *, enum CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) apply;
```

## Discussion

The function has some approximation to *A⁻¹*.

## See Also

### Inspecting Preconditioner Properties
- [var mem: UnsafeMutableRawPointer](./mem.md)
  The unaltered memory pointer that passes as the first parameter of the apply function.
- [var type: SparsePreconditioner_t](./type.md)
  The preconditioner type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_float/apply)*
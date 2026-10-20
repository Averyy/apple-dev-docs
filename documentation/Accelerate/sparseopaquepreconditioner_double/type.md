# type

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The preconditioner type.

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
var type: SparsePreconditioner_t
```

```c
SparsePreconditioner_t type;
```

## See Also

### Inspecting Preconditioner Properties
- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void](./apply.md)
  A function that calculates *Y = PX*, where *P* is the preconditioner.
- [var mem: UnsafeMutableRawPointer](./mem.md)
  The unaltered memory pointer that passes as the first parameter of the apply function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_double/type)*
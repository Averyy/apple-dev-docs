# SparseOpaquePreconditioner_Float

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that represents a single-precision preconditioner.

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
struct SparseOpaquePreconditioner_Float
```

```c
typedef struct { ... } SparseOpaquePreconditioner_Float;
```

## Topics

### Creating a Preconditioner
- [init(type: SparsePreconditioner_t, mem: UnsafeMutableRawPointer, apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void)](./sparseopaquepreconditioner_float/init%28type,mem,apply%29.md)
  Creates a new single-precision preconditioner.
### Inspecting Preconditioner Properties
- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void](./sparseopaquepreconditioner_float/apply.md)
  A function that calculates *Y = PX*, where *P* is the preconditioner.
- [var mem: UnsafeMutableRawPointer](./sparseopaquepreconditioner_float/mem.md)
  The unaltered memory pointer that passes as the first parameter of the apply function.
- [var type: SparsePreconditioner_t](./sparseopaquepreconditioner_float/type.md)
  The preconditioner type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Creating preconditioners
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Double) -> SparseOpaquePreconditioner_Double](./sparsecreatepreconditioner%28_,_%29-4ysww.md)
  Creates a preconditioner for the specified matrix of double-precision values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Float) -> SparseOpaquePreconditioner_Float](./sparsecreatepreconditioner%28_,_%29-59ql5.md)
  Creates a preconditioner for the specified matrix of single-precision values.
- [struct SparseOpaquePreconditioner_Double](./sparseopaquepreconditioner_double.md)
  A structure that represents a double-precision preconditioner.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](./sparsecreatepreconditioner%28_,_%29-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float](./sparsecreatepreconditioner%28_,_%29-95u9p.md)
  Create a preconditioner for the given matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_float)*
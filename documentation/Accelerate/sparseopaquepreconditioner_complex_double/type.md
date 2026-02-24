# type

**Framework**: Accelerate  
**Kind**: property

Types of preconditioner.

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

#### Discussion

- **`SparsePreconditionerNone`**: No preconditioner, used to flag an empty type as required.
- **`SparsePreconditionerUser`**: User-defined preconditioner.
- **`SparsePreconditionerDiagonal`**: Diagonal (Jacobi) preconditioner `D_ii = 1.0 / A_ii`. Zero entries on the diagonal of `A` are replaced with `1.0`.
- **`SparsePreconditionerDiagScaling`**: Diagonal scaling preconditioner `D_ii = 1.0 / || A_i ||_2`, where `A_i` is `i`-th column of `A`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_complex_double/type)*
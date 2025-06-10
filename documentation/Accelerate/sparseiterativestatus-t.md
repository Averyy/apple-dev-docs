# SparseIterativeStatus_t

**Framework**: Accelerate  
**Kind**: struct

Constants that define the status of the iterative solve.

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
struct SparseIterativeStatus_t
```

## Topics

### Constants
- [var SparseIterativeConverged: SparseIterativeStatus_t](sparseiterativeconverged.md)
  A status that indicates the convergence of all solutions.
- [var SparseIterativeIllConditioned: SparseIterativeStatus_t](sparseiterativeillconditioned.md)
  A status that indicates the operation determines the problem is sufficiently ill-conditioned that convergence is unlikely.
- [var SparseIterativeInternalError: SparseIterativeStatus_t](sparseiterativeinternalerror.md)
  A status that indicates an internal failure.
- [var SparseIterativeMaxIterations: SparseIterativeStatus_t](sparseiterativemaxiterations.md)
  A status that indicates a failure to converge one or more solutions in the maximum number of iterations.
- [var SparseIterativeParameterError: SparseIterativeStatus_t](sparseiterativeparametererror.md)
  A status that indicates an error with one or more parameters.
### Raw Values
- [init(Int32)](sparseiterativestatus_t/init(_:).md)
- [init(rawValue: Int32)](sparseiterativestatus_t/init(rawvalue:).md)
- [var rawValue: Int32](sparseiterativestatus_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterativestatus_t)*
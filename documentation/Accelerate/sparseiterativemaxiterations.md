# SparseIterativeMaxIterations

**Framework**: Accelerate  
**Kind**: var

A status that indicates a failure to converge one or more solutions in the maximum number of iterations.

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
var SparseIterativeMaxIterations: SparseIterativeStatus_t { get }
```

## See Also

- [var SparseIterativeConverged: SparseIterativeStatus_t](sparseiterativeconverged.md)
  A status that indicates the convergence of all solutions.
- [var SparseIterativeIllConditioned: SparseIterativeStatus_t](sparseiterativeillconditioned.md)
  A status that indicates the operation determines the problem is sufficiently ill-conditioned that convergence is unlikely.
- [var SparseIterativeInternalError: SparseIterativeStatus_t](sparseiterativeinternalerror.md)
  A status that indicates an internal failure.
- [var SparseIterativeParameterError: SparseIterativeStatus_t](sparseiterativeparametererror.md)
  A status that indicates an error with one or more parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterativemaxiterations)*
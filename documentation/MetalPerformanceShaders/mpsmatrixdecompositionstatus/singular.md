# MPSMatrixDecompositionStatus.singular

**Framework**: Metal Performance Shaders  
**Kind**: case

A status indicating the resulting decomposition is not suitable for use in a subsequent system solve.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case singular
```

## See Also

- [MPSMatrixDecompositionStatus.failure](mpsmatrixdecompositionstatus/failure.md)
  A status indicating the decomposition was not able to be completed.
- [MPSMatrixDecompositionStatus.nonPositiveDefinite](mpsmatrixdecompositionstatus/nonpositivedefinite.md)
  A status indicating a non-positive-definite pivot value was calculated.
- [MPSMatrixDecompositionStatus.success](mpsmatrixdecompositionstatus/success.md)
  A status indicating the decomposition was performed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositionstatus/singular)*
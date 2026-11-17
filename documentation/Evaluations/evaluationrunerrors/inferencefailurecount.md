# inferenceFailureCount

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

The number of rows whose subject failed to be produced; a sample run more than once counts once per failed run.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
var inferenceFailureCount: Int
```

## See Also

### Counting failures
- [var evaluatorFailureCount: Int](./evaluatorfailurecount.md)
  The total number of evaluator invocations that threw.
- [var failingEvaluatorTypes: Set<String>](./failingevaluatortypes.md)
  The set of evaluator type names that threw at least once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors/inferencefailurecount)*
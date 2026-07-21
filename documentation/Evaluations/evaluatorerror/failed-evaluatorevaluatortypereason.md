# EvaluatorError.failed(evaluator:evaluatorType:reason:)

**Framework**: Evaluations  
**Kind**: case

The evaluator threw.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case failed(evaluator: (any EvaluatorProtocol)?, evaluatorType: String, reason: String)
```

## Parameters

- `evaluator`: The failing evaluator instance — the same one from the evaluation’s `evaluators` — so a recorded failure can be mapped back to its source.
- `evaluatorType`: The failing evaluator’s concrete type name.
- `reason`: The thrown error’s `localizedDescription`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorerror/failed(evaluator:evaluatortype:reason:))*
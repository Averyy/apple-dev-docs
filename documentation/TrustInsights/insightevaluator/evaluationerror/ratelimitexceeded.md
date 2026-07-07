# InsightEvaluator.EvaluationError.rateLimitExceeded

**Framework**: Trust Insights  
**Kind**: case

An error that indicates the framework has received too many requests.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case rateLimitExceeded
```

#### Discussion

This may be due too many evaluation requests either for the app on the particular device or for the app across all devices.

## See Also

- [InsightEvaluator.EvaluationError.contextInvalid(_:)](insightevaluator/evaluationerror/contextinvalid(_:).md)
  An error that indicates the framework couldn’t produce an evaluation for the provided context.
- [InsightEvaluator.EvaluationError.denied](insightevaluator/evaluationerror/denied.md)
  An error that indicates evaluations are unavailable due to a person’s options.
- [InsightEvaluator.EvaluationError.localError](insightevaluator/evaluationerror/localerror.md)
  An error that indicates the framework couldn’t complete the evaluation.
- [InsightEvaluator.EvaluationError.notAvailable](insightevaluator/evaluationerror/notavailable.md)
  An error that indicates evaluations are not available on this device.
- [InsightEvaluator.EvaluationError.serverError](insightevaluator/evaluationerror/servererror.md)
  An error that indicates the framework couldn’t complete the evaluation due to server or network issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/evaluationerror/ratelimitexceeded)*
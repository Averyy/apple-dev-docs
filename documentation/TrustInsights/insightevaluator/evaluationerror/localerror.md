# InsightEvaluator.EvaluationError.localError

**Framework**: Trust Insights  
**Kind**: case

An error that indicates the framework couldn’t complete the evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case localError
```

#### Discussion

A retry may succeed.

## See Also

- [InsightEvaluator.EvaluationError.contextInvalid(_:)](insightevaluator/evaluationerror/contextinvalid(_:).md)
  An error that indicates the framework couldn’t produce an evaluation for the provided context.
- [InsightEvaluator.EvaluationError.denied](insightevaluator/evaluationerror/denied.md)
  An error that indicates evaluations are unavailable due to a person’s options.
- [InsightEvaluator.EvaluationError.evaluationResultSignatureInvalid](insightevaluator/evaluationerror/evaluationresultsignatureinvalid.md)
  An error that indicates the payload signature for the evaluation result from the server was invalid.
- [InsightEvaluator.EvaluationError.notAvailable](insightevaluator/evaluationerror/notavailable.md)
  An error that indicates evaluations are not available on this device.
- [InsightEvaluator.EvaluationError.rateLimitExceeded](insightevaluator/evaluationerror/ratelimitexceeded.md)
  An error that indicates the framework has received too many requests.
- [InsightEvaluator.EvaluationError.serverError](insightevaluator/evaluationerror/servererror.md)
  An error that indicates the framework couldn’t complete the evaluation due to server or network issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/evaluationerror/localerror)*
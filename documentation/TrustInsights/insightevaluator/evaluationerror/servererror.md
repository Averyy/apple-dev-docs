# InsightEvaluator.EvaluationError.serverError

**Framework**: Trust Insights  
**Kind**: case  
**Role**: Case

An error that indicates the framework couldn’t complete the evaluation due to server or network issues.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case serverError
```

## Discussion

It may be possible to retry the request.

## See Also

### Evaluation errors
- [InsightEvaluator.EvaluationError.contextInvalid(_:)](./contextinvalid%28_%29.md)
  An error that indicates the framework couldn’t produce an evaluation for the provided context.
- [InsightEvaluator.EvaluationError.denied](./denied.md)
  An error that indicates evaluations are unavailable due to a person’s options.
- [InsightEvaluator.EvaluationError.localError](./localerror.md)
  An error that indicates the framework couldn’t complete the evaluation.
- [InsightEvaluator.EvaluationError.notAvailable](./notavailable.md)
  An error that indicates evaluations are not available on this device.
- [InsightEvaluator.EvaluationError.rateLimitExceeded](./ratelimitexceeded.md)
  An error that indicates the framework has received too many requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/evaluationerror/servererror)*
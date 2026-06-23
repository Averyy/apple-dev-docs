# InsightEvaluator.EvaluationError

**Framework**: Trust Insights  
**Kind**: enum

Errors the framework can return if there are errors processing an evaluation request.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@nonexhaustive enum EvaluationError
```

## Topics

### Evaluation errors
- [InsightEvaluator.EvaluationError.contextInvalid(_:)](insightevaluator/evaluationerror/contextinvalid(_:).md)
  An error that indicates the framework couldn’t produce an evaluation for the provided context.
- [InsightEvaluator.EvaluationError.denied](insightevaluator/evaluationerror/denied.md)
  An error that indicates evaluations are unavailable due to a person’s options.
- [InsightEvaluator.EvaluationError.evaluationResultSignatureInvalid](insightevaluator/evaluationerror/evaluationresultsignatureinvalid.md)
  An error that indicates the payload signature for the evaluation result from the server was invalid.
- [InsightEvaluator.EvaluationError.localError](insightevaluator/evaluationerror/localerror.md)
  An error that indicates the framework couldn’t complete the evaluation.
- [InsightEvaluator.EvaluationError.notAvailable](insightevaluator/evaluationerror/notavailable.md)
  An error that indicates evaluations are not available on this device.
- [InsightEvaluator.EvaluationError.rateLimitExceeded](insightevaluator/evaluationerror/ratelimitexceeded.md)
  An error that indicates the framework has received too many requests.
- [InsightEvaluator.EvaluationError.serverError](insightevaluator/evaluationerror/servererror.md)
  An error that indicates the framework couldn’t complete the evaluation due to server or network issues.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [InsightEvaluator.InsightContext](insightevaluator/insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequest](insightevaluator/insightrequest.md)
  A structure you use to make a request for a specific insight.
- [InsightEvaluator.InsightRequestProtocol](insightevaluator/insightrequestprotocol.md)
  A protocol that insight evaluation types conform to.
- [InsightEvaluator.ModelVersion](insightevaluator/modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](insightevaluator/operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/evaluationerror)*
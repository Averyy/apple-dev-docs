# InsightEvaluator

**Framework**: TrustInsights  
**Kind**: class

A class that defines data and methods the framework uses to perform evaluations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final class InsightEvaluator
```

## Topics

### Creating an evaluator
- [init()](insightevaluator/init.md)
  Creates a new insight evaluator object you use to request insights.
### Requesting and checking authorization status
- [func authorizationStatus<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](insightevaluator/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether a person permitted the app to request evaluations for the given context.
- [func requestAuthorization<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](insightevaluator/requestauthorization(for:).md)
  Requests authorization from a person to generate evaluations.
- [func requestEvaluation<each I>(context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluation<repeat (each I).InsightType>](insightevaluator/requestevaluation(context:).md)
  Requests the evaluation of insights.
- [InsightEvaluator.AuthorizationStatus](insightevaluator/authorizationstatus.md)
  Values that indicate the status of the app’s authorization to request evaluations.
### Requesting an evaluation
- [InsightEvaluator.InsightContext](insightevaluator/insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequest](insightevaluator/insightrequest.md)
  A structure you use to make a request for a specific insight.
- [InsightEvaluator.InsightRequestProtocol](insightevaluator/insightrequestprotocol.md)
  A protocol that insight evaluation types conform to.
- [InsightEvaluator.EvaluationError](insightevaluator/evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](insightevaluator/modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](insightevaluator/operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestEvaluation<each I>(context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluation<repeat (each I).InsightType>](insightevaluator/requestevaluation(context:).md)
  Requests the evaluation of insights.
- [class InsightEvaluation](insightevaluation.md)
  The insight result that an evaluation request returns.
- [protocol TrustInsight](trustinsight.md)
  A protocol that describes the trust insight model and the associated evaluation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator)*
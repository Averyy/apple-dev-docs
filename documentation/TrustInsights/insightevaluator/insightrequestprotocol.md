# InsightEvaluator.InsightRequestProtocol

**Framework**: Trust Insights  
**Kind**: protocol

A protocol that insight evaluation types conform to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
protocol InsightRequestProtocol : Sendable
```

## Topics

### Associated Types
- [associatedtype InsightType : TrustInsight](insightevaluator/insightrequestprotocol/insighttype.md)
  An associated type that represents an insight.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [InsightEvaluator.InsightRequest](insightevaluator/insightrequest.md)

## See Also

- [InsightEvaluator.InsightContext](insightevaluator/insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequest](insightevaluator/insightrequest.md)
  A structure you use to make a request for a specific insight.
- [InsightEvaluator.EvaluationError](insightevaluator/evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](insightevaluator/modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](insightevaluator/operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightrequestprotocol)*
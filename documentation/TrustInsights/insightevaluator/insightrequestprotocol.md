# InsightEvaluator.InsightRequestProtocol

**Framework**: Trust Insights  
**Kind**: protocol  
**Role**: Protocol

A protocol that insight evaluation types conform to.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
protocol InsightRequestProtocol : Sendable
```

## Topics

### Associated Types
- [associatedtype InsightType : TrustInsight](./insightrequestprotocol/insighttype.md)
  An associated type that represents an insight.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [InsightEvaluator.InsightRequest](./insightrequest.md)

## See Also

### Requesting an evaluation
- [InsightEvaluator.InsightContext](./insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequest](./insightrequest.md)
  A structure you use to make a request for a specific insight.
- [InsightEvaluator.EvaluationError](./evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](./modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](./operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightrequestprotocol)*
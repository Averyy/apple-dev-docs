# InsightEvaluator.InsightContext

**Framework**: Trust Insights  
**Kind**: struct

A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct InsightContext<each InsightRequest> where repeat each InsightRequest : InsightEvaluator.InsightRequestProtocol
```

## Topics

### Creating an insight context
- [init(operationCategory: InsightEvaluator.OperationCategory, requestedEvaluations: (repeat each InsightRequest))](insightevaluator/insightcontext/init(operationcategory:requestedevaluations:).md)
  Creates the context with which to request insights.
### insight context properties
- [var operationCategory: InsightEvaluator.OperationCategory](insightevaluator/insightcontext/operationcategory.md)
  The type of operation you’re requesting the evaluation for.
- [var requestID: String?](insightevaluator/insightcontext/requestid.md)
  An optional identifier you can use to tie an assessment to a specific transaction.
- [let requestedInsight: (repeat each InsightRequest)](insightevaluator/insightcontext/requestedinsight.md)
  The insight you’re requesting.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightcontext)*
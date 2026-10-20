# InsightEvaluator.InsightContext

**Framework**: Trust Insights  
**Kind**: struct  
**Role**: Structure

A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct InsightContext<each InsightRequest> where repeat each InsightRequest : InsightEvaluator.InsightRequestProtocol
```

## Topics

### Creating an insight context
- [init(operationCategory: InsightEvaluator.OperationCategory, requestedEvaluations: (repeat each InsightRequest))](./insightcontext/init%28operationcategory,requestedevaluations%29.md)
  Creates the context with which to request insights.
### insight context properties
- [var operationCategory: InsightEvaluator.OperationCategory](./insightcontext/operationcategory.md)
  The type of operation you’re requesting the evaluation for.
- [var requestID: String?](./insightcontext/requestid.md)
  An optional identifier you can use to tie an assessment to a specific transaction.
- [let requestedInsight: (repeat each InsightRequest)](./insightcontext/requestedinsight.md)
  The insight you’re requesting.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting an evaluation
- [InsightEvaluator.InsightRequest](./insightrequest.md)
  A structure you use to make a request for a specific insight.
- [InsightEvaluator.InsightRequestProtocol](./insightrequestprotocol.md)
  A protocol that insight evaluation types conform to.
- [InsightEvaluator.EvaluationError](./evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](./modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](./operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightcontext)*
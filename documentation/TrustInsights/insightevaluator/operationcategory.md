# InsightEvaluator.OperationCategory

**Framework**: TrustInsights  
**Kind**: enum

Values that represent the types of operation it’s possible to request evaluations for.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@nonexhaustive enum OperationCategory
```

#### Discussion

Selecting the most relevant category is important for usage transparency information and may also have an affect on the behavior of the evaluation and affect the [`InsightEvaluation`](insightevaluation.md) values.

The framework may display a message based on this in the transparency logs showing app usage of Insights.

## Topics

### Enumeration Cases - generated
- [InsightEvaluator.OperationCategory.account](insightevaluator/operationcategory/account.md)
  A value that indicates an account operation including registration, login, or the modification of account details.
- [InsightEvaluator.OperationCategory.communication](insightevaluator/operationcategory/communication.md)
  A value that indicates a communication operation.
- [InsightEvaluator.OperationCategory.other](insightevaluator/operationcategory/other.md)
  A value that represents action types that don’t fall into other available categories.
- [InsightEvaluator.OperationCategory.payment](insightevaluator/operationcategory/payment.md)
  A value that indicates some form of payment or purchase.
- [InsightEvaluator.OperationCategory.resourceUse](insightevaluator/operationcategory/resourceuse.md)
  A value that indicates the use of some resource.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/operationcategory)*
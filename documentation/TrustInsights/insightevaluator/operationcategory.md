# InsightEvaluator.OperationCategory

**Framework**: Trust Insights  
**Kind**: enum  
**Role**: Enumeration

Values that represent the types of operation it’s possible to request evaluations for.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@nonexhaustive enum OperationCategory
```

## Discussion

Selecting the most relevant category is important for usage transparency information and may also have an affect on the behavior of the evaluation and affect the [`InsightEvaluation`](../insightevaluation.md) values.

The framework may display a message based on this in the transparency logs showing app usage of Insights.

## Topics

### Enumeration Cases - generated
- [InsightEvaluator.OperationCategory.account](./operationcategory/account.md)
  A value that indicates an account operation including registration, login, or the modification of account details.
- [InsightEvaluator.OperationCategory.communication](./operationcategory/communication.md)
  A value that indicates a communication operation.
- [InsightEvaluator.OperationCategory.other](./operationcategory/other.md)
  A value that represents action types that don’t fall into other available categories.
- [InsightEvaluator.OperationCategory.payment](./operationcategory/payment.md)
  A value that indicates some form of payment or purchase.
- [InsightEvaluator.OperationCategory.resourceUse](./operationcategory/resourceuse.md)
  A value that indicates the use of some resource.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting an evaluation
- [InsightEvaluator.InsightContext](./insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequest](./insightrequest.md)
  A structure you use to make a request for a specific insight.
- [InsightEvaluator.InsightRequestProtocol](./insightrequestprotocol.md)
  A protocol that insight evaluation types conform to.
- [InsightEvaluator.EvaluationError](./evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](./modelversion.md)
  Values that define the required model version of the insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/operationcategory)*
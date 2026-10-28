# InsightEvaluator.ModelVersion

**Framework**: Trust Insights  
**Kind**: enum  
**Role**: Enumeration

Values that define the required model version of the insight.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@nonexhaustive enum ModelVersion
```

## Discussion

Normally, [`InsightEvaluator.ModelVersion.current`](./modelversion/current.md) is the correct choice; only request specific older versions if there’s a particular need to either run an older version in parallel with the latest version or regulatory requirements require you to use a specific version.

See the documentation for information about available models and policies regarding availability of specific models.

## Topics

### Enumeration Cases - generated
- [InsightEvaluator.ModelVersion.current](./modelversion/current.md)
  A value that defines the latest version and includes adjustments as fraud patterns change.
- [InsightEvaluator.ModelVersion.specific(versionNumber:)](./modelversion/specific%28versionnumber%29.md)
  A value that defines a specific model version intended to be run in parallel with the latest version.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
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
- [InsightEvaluator.OperationCategory](./operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/modelversion)*
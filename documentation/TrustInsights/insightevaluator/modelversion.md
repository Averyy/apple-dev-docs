# InsightEvaluator.ModelVersion

**Framework**: Trust Insights  
**Kind**: enum

Values that define the required model version of the insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@nonexhaustive enum ModelVersion
```

#### Discussion

Normally, [`InsightEvaluator.ModelVersion.current`](insightevaluator/modelversion/current.md) is the correct choice; only request specific older versions if there’s a particular need to either run an older version in parallel with the latest version or regulatory requirements require you to use a specific version.

See the documentation for information about available models and policies regarding availability of specific models.

## Topics

### Enumeration Cases - generated
- [InsightEvaluator.ModelVersion.current](insightevaluator/modelversion/current.md)
  A value that defines the latest version and includes adjustments as fraud patterns change.
- [InsightEvaluator.ModelVersion.specific(versionNumber:)](insightevaluator/modelversion/specific(versionnumber:).md)
  A value that defines a specific model version intended to be run in parallel with the latest version.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
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
- [InsightEvaluator.OperationCategory](insightevaluator/operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/modelversion)*
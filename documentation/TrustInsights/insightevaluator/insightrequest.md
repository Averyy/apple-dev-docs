# InsightEvaluator.InsightRequest

**Framework**: Trust Insights  
**Kind**: struct

A structure you use to make a request for a specific insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct InsightRequest<InsightType> where InsightType : TrustInsight
```

#### Discussion

You can include one or more in the [`InsightEvaluator.InsightContext`](insightevaluator/insightcontext.md) for an evaluation request.

## Topics

### Creating an insight request
- [init(insightType: InsightType.Type, schema: InsightType.SchemaVersion, model: InsightEvaluator.ModelVersion)](insightevaluator/insightrequest/init(insighttype:schema:model:).md)
  Initializes a new insight request with the provided insight type, schema, and model versions.
### Insight request properties
- [var insightTypeIdentifier: String](insightevaluator/insightrequest/insighttypeidentifier.md)
  The identifier for the type of insight requested.
- [let modelVersion: InsightEvaluator.ModelVersion](insightevaluator/insightrequest/modelversion.md)
  The requested model version.
- [var schemaVersion: InsightType.SchemaVersion](insightevaluator/insightrequest/schemaversion.md)
  An integer that indicates the schema version the framework should use to perform the evaluation.
- [var schemaVersionNumber: Int](insightevaluator/insightrequest/schemaversionnumber.md)
  The requested schema version.

## Relationships

### Conforms To
- [InsightEvaluator.InsightRequestProtocol](insightevaluator/insightrequestprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [InsightEvaluator.InsightContext](insightevaluator/insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequestProtocol](insightevaluator/insightrequestprotocol.md)
  A protocol that insight evaluation types conform to.
- [InsightEvaluator.EvaluationError](insightevaluator/evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](insightevaluator/modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](insightevaluator/operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightrequest)*
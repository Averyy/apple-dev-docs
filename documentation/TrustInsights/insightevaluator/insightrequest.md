# InsightEvaluator.InsightRequest

**Framework**: Trust Insights  
**Kind**: struct  
**Role**: Structure

A structure you use to make a request for a specific insight.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct InsightRequest<InsightType> where InsightType : TrustInsight
```

## Discussion

You can include one or more in the [`InsightEvaluator.InsightContext`](./insightcontext.md) for an evaluation request.

## Topics

### Creating an insight request
- [init(insightType: InsightType.Type, schema: InsightType.SchemaVersion, model: InsightEvaluator.ModelVersion)](./insightrequest/init%28insighttype,schema,model%29.md)
  Initializes a new insight request with the provided insight type, schema, and model versions.
### Insight request properties
- [var insightTypeIdentifier: String](./insightrequest/insighttypeidentifier.md)
  The identifier for the type of insight requested.
- [let modelVersion: InsightEvaluator.ModelVersion](./insightrequest/modelversion.md)
  The requested model version.
- [var schemaVersion: InsightType.SchemaVersion](./insightrequest/schemaversion.md)
  An integer that indicates the schema version the framework should use to perform the evaluation.
- [var schemaVersionNumber: Int](./insightrequest/schemaversionnumber.md)
  The requested schema version.

## Relationships

### Conforms To
- [InsightEvaluator.InsightRequestProtocol](./insightrequestprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting an evaluation
- [InsightEvaluator.InsightContext](./insightcontext.md)
  A structure that provides details about the evaluations to request and provides information the framework requires for the evaluation to take place.
- [InsightEvaluator.InsightRequestProtocol](./insightrequestprotocol.md)
  A protocol that insight evaluation types conform to.
- [InsightEvaluator.EvaluationError](./evaluationerror.md)
  Errors the framework can return if there are errors processing an evaluation request.
- [InsightEvaluator.ModelVersion](./modelversion.md)
  Values that define the required model version of the insight.
- [InsightEvaluator.OperationCategory](./operationcategory.md)
  Values that represent the types of operation it’s possible to request evaluations for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightrequest)*
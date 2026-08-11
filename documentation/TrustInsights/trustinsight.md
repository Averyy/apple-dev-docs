# TrustInsight

**Framework**: Trust Insights  
**Kind**: protocol

A protocol that describes the trust insight model and the associated evaluation properties.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
protocol TrustInsight : Sendable
```

#### Discussion

Don’t instantiate this type directly, use one of its concrete insight types, such as  [`IsLikelyBeingCoachedInsight`](islikelybeingcoachedinsight.md) instead.

## Topics

### Associated Types - generated
- [associatedtype SchemaVersion : Sendable](trustinsight/schemaversion.md)
  A value that represents one of the available schema versions for the particular insight.
- [associatedtype Value](trustinsight/value.md)
  The result type for this particular insight which will typically be an enumeration value.
### Instance Properties - generated
- [var insightID: String](trustinsight/insightid.md)
  The insight ID.
- [var isUsingCurrentModel: Bool](trustinsight/isusingcurrentmodel.md)
  A Boolean value that indicates whether the framework created the insight with the newest available model version.
- [var modelVersion: String?](trustinsight/modelversion.md)
  The model version the framework used for this insight.
- [var newestModelVersion: String?](trustinsight/newestmodelversion.md)
  The newest model that’s available to request.
- [var outcome: Result<Self.Value, InsightError>](trustinsight/outcome.md)
  The result value from a request for this insight.
### Type Properties - generated
- [static var typeIdentifier: String](trustinsight/typeidentifier.md)
  The identifier string for the type of insight this represents.
### Type Methods - generated
- [static func request(schema: Self.SchemaVersion, modelVersion: InsightEvaluator.ModelVersion) -> InsightEvaluator.InsightRequest<Self>](trustinsight/request(schema:modelversion:).md)
  Creates an insight request for the given insight type.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [IsLikelyBeingCoachedInsight](islikelybeingcoachedinsight.md)

## See Also

- [class InsightEvaluator](insightevaluator.md)
  A class that defines data and methods the framework uses to perform evaluations.
- [func requestEvaluation<each I>(context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluation<repeat (each I).InsightType>](insightevaluator/requestevaluation(context:).md)
  Requests the evaluation of insights.
- [class InsightEvaluation](insightevaluation.md)
  The insight result that an evaluation request returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight)*
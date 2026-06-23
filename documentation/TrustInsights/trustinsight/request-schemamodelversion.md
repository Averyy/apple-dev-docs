# request(schema:modelVersion:)

**Framework**: Trust Insights  
**Kind**: method

Creates an insight request for the given insight type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static func request(schema: Self.SchemaVersion, modelVersion: InsightEvaluator.ModelVersion = .current) -> InsightEvaluator.InsightRequest<Self>
```

#### Return Value

An [`InsightEvaluator.InsightRequest`](insightevaluator/insightrequest.md) to incorporate into an [`InsightEvaluator.InsightContext`](insightevaluator/insightcontext.md) that you can use to make an evaluation request.

## Parameters

- `schema`: The required [`SchemaVersion`](trustinsight/schemaversion.md).
- `modelVersion`: The required [`InsightEvaluator.ModelVersion`](insightevaluator/modelversion.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight/request(schema:modelversion:))*
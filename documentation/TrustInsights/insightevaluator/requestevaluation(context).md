# requestEvaluation(context:)

**Framework**: Trust Insights  
**Kind**: method  
**Role**: Instance Method

Requests the evaluation of insights.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
final nonisolated(nonsending) func requestEvaluation<each I>(context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluation<repeat (each I).InsightType> where repeat each I : InsightEvaluator.InsightRequestProtocol
```

#### Return Value

The [`InsightEvaluation`](../insightevaluation.md) that contains the results of the evaluation.

#### Discussion

> **Throws**: An [`InsightEvaluator.EvaluationError`](./evaluationerror.md) if the framework fails to produce an evaluation.

#### Discussion

> **Note**: The evaluation process includes processing both on device and on Apple’s servers and can take several seconds to perform an evaluation.

To use the Trust Insights framework in your app, add the `com.apple.developer.trustinsights.base` entitlement to your apps capabilities in Xcode. For more information, see  [`Trust Insights`](../../BundleResources/entitlements/com.apple.developer.trustinsights.base.md).

## Parameters

- `context`: An [`InsightEvaluator.InsightContext`](./insightcontext.md) object that describes details evaluation request.

## See Also

### Requesting an evaluation
- [class InsightEvaluator](../insightevaluator.md)
  A class that defines data and methods the framework uses to perform evaluations.
- [class InsightEvaluation](../insightevaluation.md)
  The insight result that an evaluation request returns.
- [protocol TrustInsight](../trustinsight.md)
  A protocol that describes the trust insight model and the associated evaluation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/requestevaluation(context:))*
# requestID

**Framework**: Trust Insights  
**Kind**: property

An app defined identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var requestID: String? { get }
```

#### Discussion

Provide this as the [`requestID`](insightevaluator/insightcontext/requestid.md) in the [`InsightEvaluator.InsightContext`](insightevaluator/insightcontext.md) for the evaluation request

If provided in the [`InsightEvaluator.InsightContext`](insightevaluator/insightcontext.md) this is non-`nil` and should match the value included in the context for the request. Any mismatch indicates that your app shouldn’t trust the payload and may have been injected by an attacker in some way.

An app can also use this ID to link requests or as a wider app specific ID for the active operation.

## See Also

- [let additionalInfo: [String : String]](insightevaluation/additionalinfo.md)
  Additional information about the evaluation.
- [let generationTimestamp: Date](insightevaluation/generationtimestamp.md)
  The timestamp that indicates when the framework created the on-device portion of the assessment, in UTC.
- [let insight: (repeat each InsightResult)](insightevaluation/insight.md)
  Result values and errors for the requested insights.
- [let serverTimestamp: Date](insightevaluation/servertimestamp.md)
  The server-side timestamp that indicates when the server processed the evaluation, in UTC.
- [let signedPayload: Data](insightevaluation/signedpayload.md)
  A signed data object that contains details about the insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/requestid)*
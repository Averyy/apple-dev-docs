# insight

**Framework**: TrustInsights  
**Kind**: property

Result values and errors for the requested insights.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final let insight: (repeat each InsightResult)
```

## See Also

- [let additionalInfo: [String : String]](insightevaluation/additionalinfo.md)
  Additional information about the evaluation.
- [let generationTimestamp: Date](insightevaluation/generationtimestamp.md)
  The timestamp that indicates when the framework created the on-device portion of the assessment, in UTC.
- [var requestID: String?](insightevaluation/requestid.md)
  An app defined identifier.
- [let serverTimestamp: Date](insightevaluation/servertimestamp.md)
  The server-side timestamp that indicates when the server processed the evaluation, in UTC.
- [let signedPayload: Data](insightevaluation/signedpayload.md)
  A signed data object that contains details about the insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/insight)*
# additionalInfo

**Framework**: Trust Insights  
**Kind**: property

Additional information about the evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final let additionalInfo: [String : String]
```

## See Also

- [let generationTimestamp: Date](insightevaluation/generationtimestamp.md)
  The timestamp that indicates when the framework created the on-device portion of the assessment, in UTC.
- [let insight: (repeat each InsightResult)](insightevaluation/insight.md)
  Result values and errors for the requested insights.
- [var requestID: String?](insightevaluation/requestid.md)
  An app defined identifier.
- [let serverTimestamp: Date](insightevaluation/servertimestamp.md)
  The server-side timestamp that indicates when the server processed the evaluation, in UTC.
- [let signedPayload: Data](insightevaluation/signedpayload.md)
  A signed data object that contains details about the insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/additionalinfo)*
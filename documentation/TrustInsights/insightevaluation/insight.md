# insight

**Framework**: Trust Insights  
**Kind**: property  
**Role**: Instance Property

Result values and errors for the requested insights.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
final let insight: (repeat each InsightResult)
```

## See Also

### Evaluation properties
- [let additionalInfo: [String : String]](./additionalinfo.md)
  Additional information about the evaluation.
- [let generationTimestamp: Date](./generationtimestamp.md)
  The timestamp that indicates when the framework created the on-device portion of the assessment, in UTC.
- [var requestID: String?](./requestid.md)
  An app defined identifier.
- [let serverTimestamp: Date](./servertimestamp.md)
  The server-side timestamp that indicates when the server processed the evaluation, in UTC.
- [let signedPayload: Data](./signedpayload.md)
  A signed data object that contains details about the insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/insight)*
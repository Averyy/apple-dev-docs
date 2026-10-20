# serverTimestamp

**Framework**: Trust Insights  
**Kind**: property  
**Role**: Instance Property

The server-side timestamp that indicates when the server processed the evaluation, in UTC.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
final let serverTimestamp: Date
```

## See Also

### Evaluation properties
- [let additionalInfo: [String : String]](./additionalinfo.md)
  Additional information about the evaluation.
- [let generationTimestamp: Date](./generationtimestamp.md)
  The timestamp that indicates when the framework created the on-device portion of the assessment, in UTC.
- [let insight: (repeat each InsightResult)](./insight.md)
  Result values and errors for the requested insights.
- [var requestID: String?](./requestid.md)
  An app defined identifier.
- [let signedPayload: Data](./signedpayload.md)
  A signed data object that contains details about the insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/servertimestamp)*
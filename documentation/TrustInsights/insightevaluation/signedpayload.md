# signedPayload

**Framework**: Trust Insights  
**Kind**: property

A signed data object that contains details about the insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final let signedPayload: Data
```

#### Discussion

This data is a signed data object that represents Trust Insights Data. Trust Insights Data is the data package that contains assessments of the legitimacy of end user activity that Trust Insights returns.

The data is in the CBOR Object Signing and Encryption ([`CBOR`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc8152)) format for server side validation and processing.

## See Also

- [let additionalInfo: [String : String]](insightevaluation/additionalinfo.md)
  Additional information about the evaluation.
- [let generationTimestamp: Date](insightevaluation/generationtimestamp.md)
  The timestamp that indicates when the framework created the on-device portion of the assessment, in UTC.
- [let insight: (repeat each InsightResult)](insightevaluation/insight.md)
  Result values and errors for the requested insights.
- [var requestID: String?](insightevaluation/requestid.md)
  An app defined identifier.
- [let serverTimestamp: Date](insightevaluation/servertimestamp.md)
  The server-side timestamp that indicates when the server processed the evaluation, in UTC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/signedpayload)*
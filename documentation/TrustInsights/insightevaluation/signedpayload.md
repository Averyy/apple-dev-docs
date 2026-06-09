# signedPayload

**Framework**: TrustInsights  
**Kind**: property

A signed data object that contains details about the insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final let signedPayload: Data
```

#### Discussion

This data is a signed data object that represents Trust Insights Data, which is the data package of assessments relating to the legitimacy of end user activity passed through the Trust Insights APIs.

The data is in the CBOR Object Signing and Encryption ([`CBOR`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc8152)) format. It’s intended for server side validation and processing. For information on validating the payload signature and unpacking the data see: doc:decoding-the-data.

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
# InsightEvaluation

**Framework**: Trust Insights  
**Kind**: class

The insight result that an evaluation request returns.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class InsightEvaluation<each InsightResult> where repeat each InsightResult : TrustInsight
```

#### Discussion

This is the object that [`requestEvaluation(context:)`](insightevaluator/requestevaluation(context:).md)method returns. It includes the insight result, metadata about the ID and server timestamps you can use to track and match requests, as well as a signed payload which contains additional information about the evaluation.

There are two ways to access the information in the `signedPayload`. The most secure approach is to send the [`signedPayload`](insightevaluation/signedpayload.md) to a server that’s making the access decision where the your service can validate the signature and read the results directly. The alternative, when making and on device decision, is to read from the [`insight`](insightevaluation/insight.md) property and incorporate that summary result into decision logic within your app.

However your decide to process the result, your app needs to call [`reportConsumption(_:insightsUsed:)`](insightevaluation/reportconsumption(_:insightsused:).md) to indicate how the app made use of the insights.

## Topics

### Evaluation properties
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
- [let signedPayload: Data](insightevaluation/signedpayload.md)
  A signed data object that contains details about the insight.
### Providing feedback on insights
- [func reportConsumption(InsightEvaluationConsumptionStatus, insightIDsUsed: [String])](insightevaluation/reportconsumption(_:insightidsused:).md)
  Reports the consumption status, and optionally provides one or more associated insight identifiers.
- [func reportConsumption(InsightEvaluationConsumptionStatus, insightsUsed: [any TrustInsight])](insightevaluation/reportconsumption(_:insightsused:).md)
  Reports the consumption status, and optionally provide one or more associated insights.
### Instance Properties
- [var eventID: String](insightevaluation/eventid.md)
  Identifier for this evaluation result that can be recorded with other transaction records so that in the event that fraud or abuse is later discovered associated with the transaction it can be reported to Apple as Offline feedback via Apple Business Register

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class InsightEvaluator](insightevaluator.md)
  A class that defines data and methods the framework uses to perform evaluations.
- [func requestEvaluation<each I>(context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluation<repeat (each I).InsightType>](insightevaluator/requestevaluation(context:).md)
  Requests the evaluation of insights.
- [protocol TrustInsight](trustinsight.md)
  A protocol that describes the trust insight model and the associated evaluation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation)*
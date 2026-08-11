# reportConsumption(_:insightIDsUsed:)

**Framework**: Trust Insights  
**Kind**: method

Reports the consumption status, and optionally provides one or more associated insight identifiers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final func reportConsumption(_ status: InsightEvaluationConsumptionStatus, insightIDsUsed: [String])
```

#### Discussion

Before releasing an [`InsightEvaluation`](insightevaluation.md), call this to report how your app used the results. The system may present this value in transparency reporting and also helps with model improvement.

> ❗ **Important**: Failure to call this method to report how your app used the insight before releasing an [`InsightEvaluation`](insightevaluation.md) may result in rate limiting or revocation of you access to the service.

## Parameters

- `status`: A label indicating how the application context consumed the provided insights.
- `insightIDsUsed`: The insight IDs that the app used in making the decision. These values are optional.

## See Also

- [func reportConsumption(InsightEvaluationConsumptionStatus, insightsUsed: [any TrustInsight])](insightevaluation/reportconsumption(_:insightsused:).md)
  Reports the consumption status, and optionally provide one or more associated insights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/reportconsumption(_:insightidsused:))*
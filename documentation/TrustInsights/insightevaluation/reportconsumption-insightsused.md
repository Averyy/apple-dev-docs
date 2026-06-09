# reportConsumption(_:insightsUsed:)

**Framework**: TrustInsights  
**Kind**: method

Reports the consumption status, and optionally provide one or more associated insights.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final func reportConsumption(_ status: InsightEvaluationConsumptionStatus, insightsUsed: [any TrustInsight] = [])
```

#### Discussion

Before releasing an [`InsightEvaluation`](insightevaluation.md), call this to report how your app used the results. The system may present this value in transparency reporting and also helps with model improvement.

> ❗ **Important**: Failure to call this method to report how your app used the insight before releasing an [`InsightEvaluation`](insightevaluation.md) may result in rate limiting or revocation of you access to the service.

## Parameters

- `status`: A label that indicates how the app consumed the provided insights.
- `insightsUsed`: An array of specific[`TrustInsight`](trustinsight.md)  objects, that your app used in making a decision. These values are optional.

## See Also

- [func reportConsumption(InsightEvaluationConsumptionStatus, insightIDsUsed: [String])](insightevaluation/reportconsumption(_:insightidsused:).md)
  Reports the consumption status, and optionally provides one or more associated insight identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluation/reportconsumption(_:insightsused:))*
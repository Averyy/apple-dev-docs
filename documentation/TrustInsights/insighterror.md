# InsightError

**Framework**: Trust Insights  
**Kind**: enum

Error values the framework returns for specific insights within the overall evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@nonexhaustive enum InsightError
```

## Topics

### Insight errors
- [InsightError.insightEvaluationFailed](insighterror/insightevaluationfailed.md)
  An error that indicates that there was a failure in generating the insight.
- [InsightError.insightUnavailable](insighterror/insightunavailable.md)
  An error that indicate the requested insight isn’t available.
- [InsightError.insightVersionIncompatible](insighterror/insightversionincompatible.md)
  An error that indicates that the version you requested isn’t available on this device and OS combination.
- [InsightError.insightVersionUnavailable](insighterror/insightversionunavailable.md)
  An error that indicates that the insight version you requested isn’t available.
- [InsightError.rateLimitError](insighterror/ratelimiterror.md)
  An error that indicates that the app has reached the rate limit for the particular insight type.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum InsightEvaluationConsumptionStatus](insightevaluationconsumptionstatus.md)
  Values describing the usage of insight evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insighterror)*
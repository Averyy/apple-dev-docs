# InsightError.insightEvaluationFailed

**Framework**: Trust Insights  
**Kind**: case

An error that indicates that there was a failure in generating the insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case insightEvaluationFailed
```

#### Discussion

A retry may succeed.

## See Also

- [InsightError.insightUnavailable](insighterror/insightunavailable.md)
  An error that indicate the requested insight isn’t available.
- [InsightError.insightVersionIncompatible](insighterror/insightversionincompatible.md)
  An error that indicates that the version you requested isn’t available on this device and OS combination.
- [InsightError.insightVersionUnavailable](insighterror/insightversionunavailable.md)
  An error that indicates that the insight version you requested isn’t available.
- [InsightError.rateLimitError](insighterror/ratelimiterror.md)
  An error that indicates that the app has reached the rate limit for the particular insight type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insighterror/insightevaluationfailed)*
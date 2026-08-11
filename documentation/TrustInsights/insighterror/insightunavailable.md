# InsightError.insightUnavailable

**Framework**: Trust Insights  
**Kind**: case

An error that indicate the requested insight isn’t available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
case insightUnavailable
```

#### Discussion

The insight was potentially withdrawn or no longer supported on the active OS.

## See Also

- [InsightError.insightEvaluationFailed](insighterror/insightevaluationfailed.md)
  An error that indicates that there was a failure in generating the insight.
- [InsightError.insightVersionIncompatible](insighterror/insightversionincompatible.md)
  An error that indicates that the version you requested isn’t available on this device and OS combination.
- [InsightError.insightVersionUnavailable](insighterror/insightversionunavailable.md)
  An error that indicates that the insight version you requested isn’t available.
- [InsightError.rateLimitError](insighterror/ratelimiterror.md)
  An error that indicates that the app has reached the rate limit for the particular insight type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insighterror/insightunavailable)*
# InsightError.insightVersionUnavailable

**Framework**: TrustInsights  
**Kind**: case

An error that indicates that the insight version you requested isn’t available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case insightVersionUnavailable
```

#### Discussion

The insight version was potentially withdrawn, or no longer supported on the active OS.

## See Also

- [InsightError.insightEvaluationFailed](insighterror/insightevaluationfailed.md)
  An error that indicates that there was a failure in generating the insight.
- [InsightError.insightUnavailable](insighterror/insightunavailable.md)
  An error that indicate the requested insight isn’t available.
- [InsightError.insightVersionIncompatible](insighterror/insightversionincompatible.md)
  An error that indicates that the version you requested isn’t available on this device and OS combination.
- [InsightError.rateLimitError](insighterror/ratelimiterror.md)
  An error that indicates that the app has reached the rate limit for the particular insight type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insighterror/insightversionunavailable)*
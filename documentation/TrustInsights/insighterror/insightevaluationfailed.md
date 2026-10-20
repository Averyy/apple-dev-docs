# InsightError.insightEvaluationFailed

**Framework**: Trust Insights  
**Kind**: case  
**Role**: Case

An error that indicates that there was a failure in generating the insight.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case insightEvaluationFailed
```

#### Discussion

A retry may succeed.

## See Also

### Insight errors
- [InsightError.insightUnavailable](./insightunavailable.md)
  An error that indicate the requested insight isn’t available.
- [InsightError.insightVersionIncompatible](./insightversionincompatible.md)
  An error that indicates that the version you requested isn’t available on this device and OS combination.
- [InsightError.insightVersionUnavailable](./insightversionunavailable.md)
  An error that indicates that the insight version you requested isn’t available.
- [InsightError.rateLimitError](./ratelimiterror.md)
  An error that indicates that the app has reached the rate limit for the particular insight type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insighterror/insightevaluationfailed)*
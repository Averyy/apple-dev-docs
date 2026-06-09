# requestAuthorization(for:)

**Framework**: TrustInsights  
**Kind**: method

Requests authorization from a person to generate evaluations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final nonisolated(nonsending) func requestAuthorization<each I>(for context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus where repeat each I : InsightEvaluator.InsightRequestProtocol
```

#### Return Value

The [`InsightEvaluator.AuthorizationStatus`](insightevaluator/authorizationstatus.md) after a person has made their decision.

#### Discussion

The method doesn’t return until the UI interaction is complete and a person has made a selection as to whether to allow access to insights.

If access is already available, it returns immediately.

## Parameters

- `context`: The [`InsightEvaluator.InsightContext`](insightevaluator/insightcontext.md) to request authorization for.

## See Also

- [func authorizationStatus<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](insightevaluator/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether a person permitted the app to request evaluations for the given context.
- [InsightEvaluator.AuthorizationStatus](insightevaluator/authorizationstatus.md)
  Values that indicate the status of the app’s authorization to request evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/requestauthorization(for:))*
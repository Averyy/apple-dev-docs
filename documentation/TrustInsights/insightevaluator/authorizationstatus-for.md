# authorizationStatus(for:)

**Framework**: Trust Insights  
**Kind**: method

Returns an authorization status that indicates whether a person permitted the app to request evaluations for the given context.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final nonisolated(nonsending) func authorizationStatus<each I>(for context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus where repeat each I : InsightEvaluator.InsightRequestProtocol
```

#### Return Value

An [`InsightEvaluator.AuthorizationStatus`](insightevaluator/authorizationstatus.md) that indicates whether someone authorized the app to request evaluations.

#### Discussion

> **Note**: Errors in cases where there is a system failure.

## Parameters

- `context`: The [`InsightEvaluator.InsightContext`](insightevaluator/insightcontext.md) to request evaluations for.

## See Also

- [func requestAuthorization<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](insightevaluator/requestauthorization(for:).md)
  Requests authorization from a person to generate evaluations.
- [InsightEvaluator.AuthorizationStatus](insightevaluator/authorizationstatus.md)
  Values that indicate the status of the app’s authorization to request evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus(for:))*
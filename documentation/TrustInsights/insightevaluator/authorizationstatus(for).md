# authorizationStatus(for:)

**Framework**: Trust Insights  
**Kind**: method  
**Role**: Instance Method

Returns an authorization status that indicates whether a person permitted the app to request evaluations for the given context.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
final nonisolated(nonsending) func authorizationStatus<each I>(for context: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus where repeat each I : InsightEvaluator.InsightRequestProtocol
```

## Return Value

An [`InsightEvaluator.AuthorizationStatus`](./authorizationstatus.md) that indicates whether someone authorized the app to request evaluations.

## Discussion

> **Throws**: Errors in cases where there is a system failure.

## Parameters

- `context`: The [`InsightEvaluator.InsightContext`](./insightcontext.md) to request evaluations for.

## See Also

### Obtaining permission or checking authorization to perform evaluations
- [func requestAuthorization<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](./requestauthorization%28for%29.md)
  Requests authorization from a person to generate evaluations.
- [InsightEvaluator.AuthorizationStatus](./authorizationstatus.md)
  Values that indicate the status of the app’s authorization to request evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus(for:))*
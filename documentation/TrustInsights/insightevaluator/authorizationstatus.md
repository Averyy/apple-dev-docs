# InsightEvaluator.AuthorizationStatus

**Framework**: TrustInsights  
**Kind**: enum

Values that indicate the status of the app’s authorization to request evaluations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@nonexhaustive enum AuthorizationStatus
```

## Topics

### Authorization status values
- [InsightEvaluator.AuthorizationStatus.authorized](insightevaluator/authorizationstatus/authorized.md)
  A value that indicates a person has authorized this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.denied](insightevaluator/authorizationstatus/denied.md)
  A value that indicates a person denied permission to use the framework.
- [InsightEvaluator.AuthorizationStatus.deniedRequestable](insightevaluator/authorizationstatus/deniedrequestable.md)
  A value that indicates a person has previously denied authorization to use the framework, but the app can present a request again at a later time.
- [InsightEvaluator.AuthorizationStatus.notDetermined](insightevaluator/authorizationstatus/notdetermined.md)
  A person hasn’t yet consented to allow this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.unavailable](insightevaluator/authorizationstatus/unavailable.md)
  A value that indicates insights aren’t available on the current device.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func requestAuthorization<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](insightevaluator/requestauthorization(for:).md)
  Requests authorization from a person to generate evaluations.
- [func authorizationStatus<each I>(for: InsightEvaluator.InsightContext<repeat each I>) async throws -> InsightEvaluator.AuthorizationStatus](insightevaluator/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether a person permitted the app to request evaluations for the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus)*
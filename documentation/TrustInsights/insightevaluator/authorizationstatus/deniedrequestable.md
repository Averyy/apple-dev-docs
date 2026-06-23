# InsightEvaluator.AuthorizationStatus.deniedRequestable

**Framework**: Trust Insights  
**Kind**: case

A value that indicates a person has previously denied authorization to use the framework, but the app can present a request again at a later time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case deniedRequestable
```

#### Discussion

/// Provide explanation of the benefits of allowing insights before calling [`requestAuthorization(for:)`](insightevaluator/requestauthorization(for:).md).

## See Also

- [InsightEvaluator.AuthorizationStatus.authorized](insightevaluator/authorizationstatus/authorized.md)
  A value that indicates a person has authorized this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.denied](insightevaluator/authorizationstatus/denied.md)
  A value that indicates a person denied permission to use the framework.
- [InsightEvaluator.AuthorizationStatus.notDetermined](insightevaluator/authorizationstatus/notdetermined.md)
  A person hasn’t yet consented to allow this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.unavailable](insightevaluator/authorizationstatus/unavailable.md)
  A value that indicates insights aren’t available on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus/deniedrequestable)*
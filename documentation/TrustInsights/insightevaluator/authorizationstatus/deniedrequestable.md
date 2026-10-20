# InsightEvaluator.AuthorizationStatus.deniedRequestable

**Framework**: Trust Insights  
**Kind**: case  
**Role**: Case

A value that indicates a person has previously denied authorization to use the framework, but the app can present a request again at a later time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case deniedRequestable
```

#### Discussion

/// Provide explanation of the benefits of allowing insights before calling [`requestAuthorization(for:)`](../requestauthorization%28for%29.md).

## See Also

### Authorization status values
- [InsightEvaluator.AuthorizationStatus.authorized](./authorized.md)
  A value that indicates a person has authorized this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.denied](./denied.md)
  A value that indicates a person denied permission to use the framework.
- [InsightEvaluator.AuthorizationStatus.notDetermined](./notdetermined.md)
  A person hasn’t yet consented to allow this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.unavailable](./unavailable.md)
  A value that indicates insights aren’t available on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus/deniedrequestable)*
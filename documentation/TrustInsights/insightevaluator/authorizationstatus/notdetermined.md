# InsightEvaluator.AuthorizationStatus.notDetermined

**Framework**: Trust Insights  
**Kind**: case  
**Role**: Case

A person hasn’t yet consented to allow this app to request evaluations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case notDetermined
```

## Discussion

Request a person’s authorization by calling [`requestAuthorization(for:)`](../requestauthorization%28for%29.md).

## See Also

### Authorization status values
- [InsightEvaluator.AuthorizationStatus.authorized](./authorized.md)
  A value that indicates a person has authorized this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.denied](./denied.md)
  A value that indicates a person denied permission to use the framework.
- [InsightEvaluator.AuthorizationStatus.deniedRequestable](./deniedrequestable.md)
  A value that indicates a person has previously denied authorization to use the framework, but the app can present a request again at a later time.
- [InsightEvaluator.AuthorizationStatus.unavailable](./unavailable.md)
  A value that indicates insights aren’t available on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus/notdetermined)*
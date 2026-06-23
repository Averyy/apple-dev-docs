# InsightEvaluator.AuthorizationStatus.unavailable

**Framework**: Trust Insights  
**Kind**: case

A value that indicates insights aren’t available on the current device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case unavailable
```

#### Discussion

This may occur on unsupported devices (such as simulators), the app isn’t entitled to use the framework, or the framework isn’t available in a specific region.

## See Also

- [InsightEvaluator.AuthorizationStatus.authorized](insightevaluator/authorizationstatus/authorized.md)
  A value that indicates a person has authorized this app to request evaluations.
- [InsightEvaluator.AuthorizationStatus.denied](insightevaluator/authorizationstatus/denied.md)
  A value that indicates a person denied permission to use the framework.
- [InsightEvaluator.AuthorizationStatus.deniedRequestable](insightevaluator/authorizationstatus/deniedrequestable.md)
  A value that indicates a person has previously denied authorization to use the framework, but the app can present a request again at a later time.
- [InsightEvaluator.AuthorizationStatus.notDetermined](insightevaluator/authorizationstatus/notdetermined.md)
  A person hasn’t yet consented to allow this app to request evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus/unavailable)*
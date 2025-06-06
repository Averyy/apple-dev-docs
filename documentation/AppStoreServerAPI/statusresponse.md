# StatusResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains status information for all of a customer’s auto-renewable subscriptions in your app.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object StatusResponse
```

## Topics

### Response Objects and Data Types
- [object SubscriptionGroupIdentifierItem](subscriptiongroupidentifieritem.md)
  Information for auto-renewable subscriptions, including signed transaction information and signed renewal information, for one subscription group.
- [type environment](environment.md)
  The server environment, either sandbox or production.
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.

## See Also

- [Get All Subscription Statuses](get-all-subscription-statuses.md)
  Get the statuses for all of a customer’s auto-renewable subscriptions in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/statusresponse)*
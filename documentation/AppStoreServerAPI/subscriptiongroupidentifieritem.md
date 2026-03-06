# SubscriptionGroupIdentifierItem

**Framework**: App Store Server API  
**Kind**: dictionary

Information for auto-renewable subscriptions, including signed transaction information and signed renewal information, for one subscription group.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object SubscriptionGroupIdentifierItem
```

## Topics

### Object and Data Types
- [subscriptionGroupIdentifier](subscriptiongroupidentifieritem/subscriptiongroupidentifier.md)
- [object lastTransactionsItem](lasttransactionsitem.md)
  The most recent App Store-signed transaction information and App Store-signed renewal information for an auto-renewable subscription.

## Properties

- `subscriptionGroupIdentifier` (subscriptionGroupIdentifier): The subscription group identifier of the auto-renewable subscriptions in the `lastTransactions` array.
- `lastTransactions` ([lastTransactionsItem]): An array of the most recent App Store-signed transaction information and App Store-signed renewal information for all auto-renewable subscriptions in the subscription group.

## See Also

- [type environment](environment.md)
  The server environment, either sandbox or production.
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/subscriptiongroupidentifieritem)*
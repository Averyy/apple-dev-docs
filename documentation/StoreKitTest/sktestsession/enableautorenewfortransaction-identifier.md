# enableAutoRenewForTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

Enables auto-renewing for an auto-renewable subscription in the test environment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func enableAutoRenewForTransaction(identifier: Int) throws
```

#### Discussion

Call this method to enable the subscription to automatically renew in the testing environment. By default, all auto-renewable subscriptions have auto-renew enabled.

## Parameters

- `identifier`: The transaction   of the auto-renewable subscription.

## See Also

- [var timeRate: SKTestSession.TimeRate](sktestsession/timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [SKTestSession.TimeRate](sktestsession/timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](sktestsession/disableautorenewfortransaction(identifier:).md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func forceRenewalOfSubscription(productIdentifier: String) throws](sktestsession/forcerenewalofsubscription(productidentifier:).md)
  Ends the previous subscription period and begins the next period in the test environment.
- [func expireSubscription(productIdentifier: String) throws](sktestsession/expiresubscription(productidentifier:).md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/enableautorenewfortransaction(identifier:))*
# expireSubscription(productIdentifier:)

**Framework**: StoreKit Test  
**Kind**: method

Causes the identified auto-renewable subscription to expire immediately in the test environment.

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
func expireSubscription(productIdentifier: String) throws
```

#### Discussion

Use this method to test how your app handles expired subscriptions and revoking access to content or service. This method forces the subscription to expire. Specifically, the testing environment disables auto-renew and changes the subscription’s expiration date to the current system time.

You can also test subscription expiration by accelerating the time in the testing environment to speed up subscription renewal periods. See [`timeRate`](sktestsession/timerate-swift.property.md) for more information.

## Parameters

- `productIdentifier`: The   of the auto-renewable subscription to expire.

## See Also

- [var timeRate: SKTestSession.TimeRate](sktestsession/timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [SKTestSession.TimeRate](sktestsession/timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func enableAutoRenewForTransaction(identifier: Int) throws](sktestsession/enableautorenewfortransaction(identifier:).md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](sktestsession/disableautorenewfortransaction(identifier:).md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func forceRenewalOfSubscription(productIdentifier: String) throws](sktestsession/forcerenewalofsubscription(productidentifier:).md)
  Ends the previous subscription period and begins the next period in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/expiresubscription(productidentifier:))*
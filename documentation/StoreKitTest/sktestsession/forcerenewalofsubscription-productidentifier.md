# forceRenewalOfSubscription(productIdentifier:)

**Framework**: StoreKit Test  
**Kind**: method

Ends the previous subscription period and begins the next period in the test environment.

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
func forceRenewalOfSubscription(productIdentifier: String) throws
```

#### Discussion

Use this method to test how your code handles subscription renewals. When you call this method, the subscription expires at the time you call the method, and a new subscription period begins.

To force the subscription renewal, the testing environment changes the [`expirationDate`](https://developer.apple.com/documentation/StoreKit/Transaction/expirationDate) property on the [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) to the current system time. (If your app uses receipts, the receipt also shows this expiration date change). The testing environment also:

- Enables the subscription auto-renew state
- Removes a pending price increase, setting it to [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/PriceIncreaseStatus-swift.enum/noIncreasePending)

The testing environment doesn’t change the billing retry state with this call.

You can also test subscription renewals by accelerating the time in the testing environment to speed up subscription renewal periods. See [`timeRate`](sktestsession/timerate-swift.property.md) for more information.

## Parameters

- `productIdentifier`: The   of the auto-renewable subscription to renew.

## See Also

- [var timeRate: SKTestSession.TimeRate](sktestsession/timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [SKTestSession.TimeRate](sktestsession/timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func enableAutoRenewForTransaction(identifier: Int) throws](sktestsession/enableautorenewfortransaction(identifier:).md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](sktestsession/disableautorenewfortransaction(identifier:).md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func expireSubscription(productIdentifier: String) throws](sktestsession/expiresubscription(productidentifier:).md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/forcerenewalofsubscription(productidentifier:))*
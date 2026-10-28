# forceRenewalOfSubscription(productIdentifier:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) forceRenewalOfSubscriptionWithProductIdentifier:(NSString *) productIdentifier error:(NSError **) error;
```

## Discussion

Use this method to test how your code handles subscription renewals. When you call this method, the subscription expires at the time you call the method, and a new subscription period begins.

To force the subscription renewal, the testing environment changes the [`expirationDate`](../../StoreKit/transaction/expirationdate.md) property on the [`Transaction`](../../StoreKit/transaction.md) to the current system time. (If your app uses receipts, the receipt also shows this expiration date change). The testing environment also:

- Enables the subscription auto-renew state
- Removes a pending price increase, setting it to [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`](../../StoreKit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/noincreasepending.md)

The testing environment doesn’t change the billing retry state with this call.

You can also test subscription renewals by accelerating the time in the testing environment to speed up subscription renewal periods. See [`timeRate`](./timerate-swift.property.md) for more information.

## Parameters

- `productIdentifier`: The [`productIdentifier`](../sktesttransaction/productidentifier.md) of the auto-renewable subscription to renew.

## See Also

### Testing subscription renewals
- [var timeRate: SKTestSession.TimeRate](./timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [SKTestSession.TimeRate](./timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func enableAutoRenewForTransaction(identifier: Int) throws](./enableautorenewfortransaction%28identifier%29.md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](./disableautorenewfortransaction%28identifier%29.md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func expireSubscription(productIdentifier: String) throws](./expiresubscription%28productidentifier%29.md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/forcerenewalofsubscription(productidentifier:))*
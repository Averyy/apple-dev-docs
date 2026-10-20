# showPriceConsentIfNeeded()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Asks the system to display the price consent sheet if the user hasn’t yet responded to a subscription price increase.

**Availability**:
- iOS 13.4+ - Deprecated in 18.0
- iPadOS 13.4+ - Deprecated in 18.0
- Mac Catalyst 13.4+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use Message.messages and Message.display(in:).

## Declaration

```swift
func showPriceConsentIfNeeded()
```

```objc
- (void) showPriceConsentIfNeeded;
```

## Mentions

- [Handling Subscriptions Billing](../handling-subscriptions-billing.md)

#### Discussion

Call this method if the system called your delegate’s [`paymentQueueShouldShowPriceConsent(_:)`](../skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent%28_%29.md) method, and you chose to delay showing the price consent sheet.

This function displays the price consent sheet if both of the following are true:

- You’ve increased the price of the subscription in App Store Connect.
- The subscriber hasn’t yet responded to a price consent query.

Otherwise, this function has no effect.

> **Note**:  When you increase the price of a subscription, Apple informs affected subscribers through an email, push notification, and in-app price consent sheet and asks them to agree to the new price. If they don’t agree or take no action, their subscription expires at the end of their current billing cycle. For more information, see [Managing Prices](https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers) and [Manage pricing for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/devc9870599e).

In Mac apps built with Mac Catalyst, this function has no effect.

## See Also

### Related Documentation
- [func paymentQueueShouldShowPriceConsent(SKPaymentQueue) -> Bool](../skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent%28_%29.md)
  Asks the delegate whether to immediately display a price consent sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/showpriceconsentifneeded())*
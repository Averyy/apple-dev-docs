# offer

**Framework**: StoreKit  
**Kind**: property

The subscription offer that the customer redeems outside of your app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 16.4+
- macOS 15.0+

## Declaration

```swift
let offer: Product.SubscriptionOffer?
```

## Mentions

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)

#### Discussion

The system populates this value if the customer redeems a [`winBack`](product/subscriptionoffer/offertype/winback.md) offer type outside of your app. Add this offer to the purchase options. For more information and a code example, see the [`Handle win-back offers redeemed outside of your app`](supporting-win-back-offers-in-your-app#Handle-win-back-offers-redeemed-outside-of-your-app.md) section of  [`Supporting win-back offers in your app`](supporting-win-back-offers-in-your-app.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/purchaseintent/offer)*
# winBackOffers

**Framework**: StoreKit  
**Kind**: property

An array of available win-back offers for the auto-renewable subscription that you configured in App Store Connect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
let winBackOffers: [Product.SubscriptionOffer]
```

## Mentions

- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)

#### Discussion

This list of win-back offers doesn’t take customer eligibility into account, and includes the available offers you’ve configured for the subscription. The customer may not be eligible for all the win-back offers in this array. To get the win-back offers that the customer is eligible for, use [`eligibleWinBackOfferIDs`](product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.md) in the subscription renewal information.

For more information about win-back offers, see [`Supporting win-back offers in your app`](supporting-win-back-offers-in-your-app.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/winbackoffers)*
# winBackOffer

**Framework**: StoreKit  
**Kind**: property

A message the App Store sends when the customer is eligible for a win-back offer that you configure in App Store Connect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
static let winBackOffer: Message.Reason
```

## Mentions

- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
- [Testing win-back offers in the sandbox environment](testing-win-back-offers-in-the-sandbox-environment.md)
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)

#### Discussion

If the customer is eligible for a win-back offer, StoreKit displays the win-back offer message when the app launches. If your app customizes the way it displays win-back offers, you can suppress this message, as described in [`Message`](message.md).

For more information, see [`Merchandising win-back offers in your app`](merchandising-win-back-offers-in-your-app.md).

## See Also

- [static let billingIssue: Message.Reason](message/reason-swift.struct/billingissue.md)
  A message the App Store sends that informs people of a billing problem and enables them to update billing information.
- [static let generic: Message.Reason](message/reason-swift.struct/generic.md)
  A message the App Store sends for a generic reason.
- [static let priceIncreaseConsent: Message.Reason](message/reason-swift.struct/priceincreaseconsent.md)
  A message the App Store sends when you increase the price of an auto-renewable subscription and the price increase requires the customer’s consent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/message/reason-swift.struct/winbackoffer)*
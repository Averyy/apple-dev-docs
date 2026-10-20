# code

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

An offer code.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let code: Transaction.OfferType
```

## Mentions

- [Supporting offer codes in your app](../../supporting-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](../../supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

You create and define offer codes in App Store Connect. Offer codes are available for any Apple In-App Purchase product type.

For more information about offer codes, see [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

The raw value of the [`code`](./code.md) offer type is `3`.

## See Also

### Getting offer types
- [static let introductory: Transaction.OfferType](./introductory.md)
  An introductory offer for an auto-renewable subscription.
- [static let promotional: Transaction.OfferType](./promotional.md)
  A promotional offer for an auto-renewable subscription.
- [static var winBack: Transaction.OfferType](./winback.md)
  A win-back offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offertype-swift.struct/code)*
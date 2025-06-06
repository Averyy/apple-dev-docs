# offer

**Framework**: StoreKit  
**Kind**: property

A subscription offer that applies to the transaction at the next renewal period.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
let offer: Transaction.Offer?
```

#### Discussion

This value is populated if a customer redeems a subscription offer that applies to more than one subscription period.

This value is `nil` if there’s no subscription offer.

## See Also

- [Transaction.Offer](transaction/offer-swift.struct.md)
  The subscription offers that apply to a transaction.
- [let eligibleWinBackOfferIDs: [String]](product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.md)
  An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offer)*
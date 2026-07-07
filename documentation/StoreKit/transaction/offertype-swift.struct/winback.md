# winBack

**Framework**: StoreKit  
**Kind**: property

A win-back offer for an auto-renewable subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
static var winBack: Transaction.OfferType { get }
```

#### Discussion

For more information about win-back offers, see [`Set up win-back offers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers).

The raw value of the [`winBack`](transaction/offertype-swift.struct/winback.md) offer type is `4`.

## See Also

- [static let introductory: Transaction.OfferType](transaction/offertype-swift.struct/introductory.md)
  An introductory offer for an auto-renewable subscription.
- [static let promotional: Transaction.OfferType](transaction/offertype-swift.struct/promotional.md)
  A promotional offer for an auto-renewable subscription.
- [static let code: Transaction.OfferType](transaction/offertype-swift.struct/code.md)
  An offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offertype-swift.struct/winback)*
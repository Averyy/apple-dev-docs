# purchase

**Framework**: StoreKit  
**Kind**: property

A transaction reason that indicates a purchase is initiated by a customer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let purchase: Transaction.Reason
```

#### Discussion

The customer initiated the purchase, which may be for any in-app purchase type: consumable, non-consumable, non-renewing subscription, or auto-renewable subscription.

## See Also

- [static let renewal: Transaction.Reason](transaction/reason-swift.struct/renewal.md)
  A transaction reason that indicates the App Store server initiated a purchase transaction to renew an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/reason-swift.struct/purchase)*
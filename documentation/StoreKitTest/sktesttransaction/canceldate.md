# cancelDate

**Framework**: StoreKit Test  
**Kind**: property

The date when the system refunded the transaction.

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
var cancelDate: Date? { get }
```

#### Discussion

The [`cancelDate`](sktesttransaction/canceldate.md) is equivalent to the [`revocationDate`](https://developer.apple.com/documentation/StoreKit/Transaction/revocationDate) in [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction). The system sets the [`cancelDate`](sktesttransaction/canceldate.md) if it refunds or revokes the in-app purchase. Otherwise, the value is `nil`.

A subscription can have a `nil` [`cancelDate`](sktesttransaction/canceldate.md) and be inactive if its expiration date passed.

The system doesn’t set [`cancelDate`](sktesttransaction/canceldate.md) if the user turns off auto-renewing for the subscription. If the user upgrades the subscription, the system sets [`isUpgraded`](https://developer.apple.com/documentation/StoreKit/Transaction/isUpgraded) in [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) to `true` and sends a new transaction for the upgraded subscription. The system doesn’t set [`cancelDate`](sktesttransaction/canceldate.md) in this case.

## See Also

- [var purchaseDate: Date](sktesttransaction/purchasedate.md)
  The date of purchase for the transaction.
- [var expirationDate: Date?](sktesttransaction/expirationdate.md)
  The date a subscription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/canceldate)*
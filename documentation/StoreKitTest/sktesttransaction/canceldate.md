# cancelDate

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSDate * cancelDate;
```

## Discussion

The [`cancelDate`](./canceldate.md) is equivalent to the [`revocationDate`](../../StoreKit/transaction/revocationdate.md) in [`Transaction`](../../StoreKit/transaction.md). The system sets the [`cancelDate`](./canceldate.md) if it refunds or revokes the in-app purchase. Otherwise, the value is `nil`.

A subscription can have a `nil` [`cancelDate`](./canceldate.md) and be inactive if its expiration date passed.

The system doesn’t set [`cancelDate`](./canceldate.md) if the user turns off auto-renewing for the subscription. If the user upgrades the subscription, the system sets [`isUpgraded`](../../StoreKit/transaction/isupgraded.md) in [`Transaction`](../../StoreKit/transaction.md) to `true` and sends a new transaction for the upgraded subscription. The system doesn’t set [`cancelDate`](./canceldate.md) in this case.

## See Also

### Getting Dates
- [var purchaseDate: Date](./purchasedate.md)
  The date of purchase for the transaction.
- [var expirationDate: Date?](./expirationdate.md)
  The date a subscription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/canceldate)*
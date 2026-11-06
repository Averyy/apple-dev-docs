# seats(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Sets the total number of seats for a multiseat subscription purchase.

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
@backDeployed(before: iOS 27.3, macOS 27.3, tvOS 27.3, watchOS 27.3, visionOS 27.3)
static func seats(_ targetSeatQuantity: Int) -> Product.PurchaseOption
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)
- [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Return Value

An instance of [`Product.PurchaseOption`](../purchaseoption.md) to use in [`purchase(options:)`](../purchase%28options%29.md).

## Discussion

Use this option to buy a multiseat subscription, or to add seats to one. Pass the total number of seats the subscription has after the purchase, not the number of seats to add. When you add seats, the total needs to be higher than the subscription’s current number of seats. For example, to add 4 seats to a subscription that has 8, pass 12:

```swift
let result = try await product.purchase(options: [.seats(12)])
```

Use this option only for a product whose [`supportsMultiSeatPurchase`](../supportsmultiseatpurchase.md) value is `true`. To reduce the number of seats, the group purchaser uses Manage Subscriptions. Present it with [`showManageSubscriptions(in:)`](../../appstore/showmanagesubscriptions%28in%29.md) or, on macOS, [`showManageSubscriptions(from:)`](../../appstore/showmanagesubscriptions%28from%29.md), or direct the group purchaser to their subscriptions in Settings.

For more information, see [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md).

On the App Store, a customer can buy up to 100 seats in a single purchase. Customers can buy multiseat subscriptions on iOS, iPadOS, and macOS. To set the quantity of a consumable or a non-renewing subscription, use [`quantity(_:)`](./quantity%28_%29.md) instead.

## Parameters

- `targetSeatQuantity`: The total number of seats the subscription has after the purchase completes.

## See Also

### Purchasing multiseat subscriptions
- [static func multiSeatInvitationSheetSuppressed(Bool) -> Product.PurchaseOption](./multiseatinvitationsheetsuppressed%28_%29.md)
  Turns off the invitation sheet that the system presents after a multiseat subscription purchase with Apple-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/seats(_:))*
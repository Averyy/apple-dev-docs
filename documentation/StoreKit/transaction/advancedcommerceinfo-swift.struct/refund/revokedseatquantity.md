# revokedSeatQuantity

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of seats that this refund revoked.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
let revokedSeatQuantity: Int?
```

## Discussion

This value is `nil` if the refund didn’t revoke a specific number of seats. To revoke seats, set the `revokeSeatQuantity` value in a [`Revoke Subscription`](../../../../AdvancedCommerceAPI/revoke-subscription.md) request.

## See Also

### Instance Properties
- [let amount: Decimal](./amount.md)
  The amount of the refund.
- [let date: Date](./date.md)
  The date the refund was granted.
- [let reason: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.property.md)
  The reason for the refund.
- [let type: Transaction.AdvancedCommerceInfo.Refund.RefundType](./type.md)
  The type of the refund.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/revokedseatquantity)*
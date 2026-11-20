# revokeSeatQuantity

**Framework**: Advanced Commerce API  
**Kind**: typealias  
**Role**: Type

The number of unclaimed seats to revoke from a subscription that a customer buys as a multiseat purchase.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
int32 revokeSeatQuantity
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)



**Minimum**: `1`

## Discussion

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

Include `revokeSeatQuantity` in a [`SubscriptionRevokeRequest`](./subscriptionrevokerequest.md) to revoke some of a subscription’s seats rather than the entire subscription. Omit it to revoke the entire subscription, including claimed seats. When you revoke seats, the App Store sends a `REFUND` notification with a subtype of `SEATS`. For more information, see [`subtype`](../AppStoreServerNotifications/subtype.md).

You can revoke only unclaimed seats, which are seats that no member occupies. The value needs to be a positive number that doesn’t exceed the subscription’s number of unclaimed seats. The App Store revokes seats from the least expensive tier first.

The `refundType` in the [`SubscriptionRevokeRequest`](./subscriptionrevokerequest.md) describes the time period that the refund covers, independent of the number of seats you revoke.

## See Also

### Data types
- [type currency](./currency.md)
  The three-letter ISO 4217 currency code for the price of a product.
- [type description](./description.md)
  A string you provide that describes a SKU.
- [type dependentSKU](./dependentsku.md)
  The product identifier of a dependent SKU in a subscription price change.
- [type displayName](./displayname.md)
  A string with a product name that you can localize and is suitable for display to customers.
- [type effective](./effective.md)
  A string value that indicates when a requested change to an auto-renewable subscription goes into effect.
- [type finalQuantity](./finalquantity.md)
  The total number of seats for a subscription item that a customer buys as a multiseat purchase.
- [type period](./period.md)
  The duration of a single cycle of an auto-renewable subscription.
- [type price](./price.md)
  A price, in milliunits of a currency, for an Advanced Commerce API SKU.
- [type proratedPrice](./proratedprice.md)
  A prorated price, in milliunits of a currency, for an Advanced Commerce API SKU.
- [type retainBillingCycle](./retainbillingcycle.md)
  A Boolean value that determines whether to keep the existing billing cycle with the change you request.
- [type refundAmount](./refundamount.md)
  A refund amount, in milliunits of the currency.
- [type refundReason](./refundreason.md)
  A reason to request a refund.
- [type refundRiskingPreference](./refundriskingpreference.md)
  A Boolean value that indicates whether the App Store asks you for consumption data to help inform the refund decision.
- [type SKU](./sku.md)
  The product identifier of an Apple In-App Purchase product you manage in your own system.
- [type storefront](./storefront.md)
  A three-letter code that represents the country or region associated with the App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/revokeseatquantity)*
# advancedCommerceRevokedSeatQuantity

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The number of seats that a refund revoked from an Advanced Commerce subscription.

**Availability**:
- App Store Server API 1.25+

## Declaration

```
int32 advancedCommerceRevokedSeatQuantity
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

> ❗ **Important**:  Multiseat purchases with the Advanced Commerce API are only available in the sandbox environment.

The `revokedSeatQuantity` field of [`advancedCommerceRefund`](./advancedcommercerefund.md) uses this type. It’s present when a refund revokes some, but not all, of the seats of a subscription that a customer buys as a multiseat purchase.

To revoke seats, call the [`Revoke Subscription`](../AdvancedCommerceAPI/revoke-subscription.md) endpoint and specify the [`revokeSeatQuantity`](../AdvancedCommerceAPI/revokeseatquantity.md). The App Store then sends a `REFUND` notification. If the subscription remains active with its remaining seats, the notification has a subtype of `SEATS`. If the request revokes every seat, the notification has no subtype. For more information, see [`subtype`](../AppStoreServerNotifications/subtype.md).

## See Also

### Data types
- [type advancedCommerceConsistencyToken](./advancedcommerceconsistencytoken.md)
- [type advancedCommerceDescription](./advancedcommercedescription.md)
- [type advancedCommerceDisplayName](./advancedcommercedisplayname.md)
- [type advancedCommerceEstimatedTax](./advancedcommerceestimatedtax.md)
- [type advancedCommerceMaximumSeatQuantity](./advancedcommercemaximumseatquantity.md)
  The number of seats in a price tier of an Advanced Commerce subscription item.
- [type advancedCommerceOfferPeriod](./advancedcommerceofferperiod.md)
- [type advancedCommerceOfferPrice](./advancedcommerceofferprice.md)
- [type advancedCommercePartnerId](./advancedcommercepartnerid.md)
- [type advancedCommercePartnerName](./advancedcommercepartnername.md)
- [type advancedCommercePartners](./advancedcommercepartners.md)
- [type advancedCommercePeriod](./advancedcommerceperiod.md)
- [type advancedCommercePeriodCount](./advancedcommerceperiodcount.md)
- [type advancedCommercePrice](./advancedcommerceprice.md)
- [type advancedCommercePriceIncreaseInfoDependentSKU](./advancedcommercepriceincreaseinfodependentsku.md)
- [type advancedCommercePriceIncreaseInfoPrice](./advancedcommercepriceincreaseinfoprice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/advancedcommercerevokedseatquantity)*
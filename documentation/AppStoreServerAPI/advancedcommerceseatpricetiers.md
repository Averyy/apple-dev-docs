# advancedCommerceSeatPriceTiers

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The price tiers that your app provides for the seats of an Advanced Commerce subscription item.

**Availability**:
- App Store Server API 1.25+

## Declaration

```
[advancedCommerceSeatPriceTier] advancedCommerceSeatPriceTiers
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

> ❗ **Important**:  Multiseat purchases with the Advanced Commerce API are only available in the sandbox environment.

This array contains the price tiers from your app’s request for a subscription item that a customer buys as a multiseat purchase. The tiers appear in order, from the most expensive tier to the least expensive, and the array contains up to five tiers.

The `seatPriceTiers` field of [`advancedCommerceTransactionItem`](./advancedcommercetransactionitem.md) and the `seatRenewalPriceTiers` field of [`advancedCommerceRenewalItem`](./advancedcommercerenewalitem.md) use this type. To find the number of seats the transaction includes at each price, see the `priceTiers` array of [`TransactionMultiSeatInfo`](./transactionmultiseatinfo.md).

For more information about providing price tiers, see [`SeatPriceTier`](../AdvancedCommerceAPI/seatpricetier.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/advancedcommerceseatpricetiers)*
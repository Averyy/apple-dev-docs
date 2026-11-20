# advancedCommerceMaximumSeatQuantity

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The number of seats in a price tier of an Advanced Commerce subscription item.

**Availability**:
- App Store Server Notifications 2.25+

## Declaration

```
int32 advancedCommerceMaximumSeatQuantity
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)



**Minimum**: `1`

## Discussion

> ❗ **Important**:  Multiseat purchases with the Advanced Commerce API are only available in the sandbox environment.

This value is the number of seats in the tier, not the position of the tier’s last seat. For example, two tiers that each have a `maximumSeatQuantity` of `5` cover seats 1 through 5 and seats 6 through 10.

The last tier in an [`advancedCommerceSeatPriceTiers`](./advancedcommerceseatpricetiers.md) array doesn’t contain this value, because it has no upper limit.

## See Also

### Data types
- [type advancedCommerceConsistencyToken](./advancedcommerceconsistencytoken.md)
- [type advancedCommerceDescription](./advancedcommercedescription.md)
- [type advancedCommerceDisplayName](./advancedcommercedisplayname.md)
- [type advancedCommerceEstimatedTax](./advancedcommerceestimatedtax.md)
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
- [type advancedCommercePriceIncreaseInfoStatus](./advancedcommercepriceincreaseinfostatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/advancedcommercemaximumseatquantity)*
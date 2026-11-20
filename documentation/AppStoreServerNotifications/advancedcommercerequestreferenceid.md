# advancedCommerceRequestReferenceId

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The request reference identifier from the most recent Advanced Commerce API request that applies to the transaction.

**Availability**:
- App Store Server Notifications 2.14+

## Declaration

```
string advancedCommerceRequestReferenceId
```

## Discussion

For a transaction with an [`inAppOwnershipType`](./inappownershiptype.md) of `ASSIGNED`, this value is `00000000-0000-0000-0000-000000000000`, rather than the request reference identifier from the group purchaser’s request.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/advancedcommercerequestreferenceid)*
# advancedCommerceSeatPriceTier

**Framework**: App Store Server Notifications  
**Kind**: dictionary  
**Role**: Object

A price tier that your app provides for the seats of an Advanced Commerce subscription item.

**Availability**:
- App Store Server Notifications 2.25+

## Declaration

```
object advancedCommerceSeatPriceTier
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

> ❗ **Important**:  Multiseat purchases with the Advanced Commerce API are only available in the sandbox environment.

The [`advancedCommerceSeatPriceTiers`](./advancedcommerceseatpricetiers.md) array contains these tiers.

## Properties

- `maximumSeatQuantity` (advancedCommerceMaximumSeatQuantity): The number of seats in the tier. This field is absent for the last tier, which has no upper limit.

  **Minimum**: `1`
- `price` (advancedCommerceTierPrice): The price per seat, in milliunits of the currency, for the tier.

## See Also

### Objects
- [object advancedCommerceDescriptors](./advancedcommercedescriptors.md)
- [object advancedCommerceOffer](./advancedcommerceoffer.md)
- [object advancedCommercePartner](./advancedcommercepartner.md)
- [object advancedCommercePriceIncreaseInfo](./advancedcommercepriceincreaseinfo.md)
- [object advancedCommerceRefund](./advancedcommercerefund.md)
- [object advancedCommerceRenewalInfo](./advancedcommercerenewalinfo.md)
- [object advancedCommerceRenewalItem](./advancedcommercerenewalitem.md)
- [object advancedCommerceTransactionInfo](./advancedcommercetransactioninfo.md)
- [object advancedCommerceTransactionItem](./advancedcommercetransactionitem.md)
- [object advancedCommerceBundleItem](./advancedcommercebundleitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/advancedcommerceseatpricetier)*
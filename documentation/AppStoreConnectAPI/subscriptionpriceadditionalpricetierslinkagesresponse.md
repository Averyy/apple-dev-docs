# SubscriptionPriceAdditionalPriceTiersLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list the IDs of a subscription price’s additional price tiers.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceAdditionalPriceTiersLinkagesResponse
```

## Topics

### Dictionaries
- [object SubscriptionPriceAdditionalPriceTiersLinkagesResponse.Data](./subscriptionpriceadditionalpricetierslinkagesresponse/data-data.dictionary.md)

## Properties

- `data` ([SubscriptionPriceAdditionalPriceTiersLinkagesResponse.Data]) *(required)*: The object types and IDs of the related resources.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

### Objects and types
- [object SubscriptionPriceTier](./subscriptionpricetier.md)
  A volume pricing tier that sets a per-seat price from a minimum number of seats.
- [object SubscriptionPriceTierInlineCreate](./subscriptionpricetierinlinecreate.md)
  A volume pricing tier that you create inline with a subscription price.
- [object SubscriptionPriceTiersResponse](./subscriptionpricetiersresponse.md)
  The response body for endpoints that list subscription price tiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpriceadditionalpricetierslinkagesresponse)*
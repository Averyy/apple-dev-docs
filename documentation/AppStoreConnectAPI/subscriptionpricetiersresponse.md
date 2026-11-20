# SubscriptionPriceTiersResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list subscription price tiers.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTiersResponse
```

## Properties

- `data` ([SubscriptionPriceTier]) *(required)*: The resource data.
- `included` ([SubscriptionPricePoint]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

### Objects and types
- [object SubscriptionPriceTier](./subscriptionpricetier.md)
  A volume pricing tier that sets a per-seat price from a minimum number of seats.
- [object SubscriptionPriceTierInlineCreate](./subscriptionpricetierinlinecreate.md)
  A volume pricing tier that you create inline with a subscription price.
- [object SubscriptionPriceAdditionalPriceTiersLinkagesResponse](./subscriptionpriceadditionalpricetierslinkagesresponse.md)
  The response body for endpoints that list the IDs of a subscription price’s additional price tiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetiersresponse)*
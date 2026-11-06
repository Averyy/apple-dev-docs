# RetentionOfferPricesLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing the resource identifiers of prices for a retention offer.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOfferPricesLinkagesResponse
```

## Topics

### Dictionaries
- [object RetentionOfferPricesLinkagesResponse.Data](./retentionofferpriceslinkagesresponse/data-data.dictionary.md)

## Properties

- `data` ([RetentionOfferPricesLinkagesResponse.Data]) *(required)*: The object types and IDs of the related resources.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

### Objects and types
- [object RetentionOffer](./retentionoffer.md)
  A discounted offer for an auto-renewable subscription that you present to people who start to cancel it.
- [object RetentionOfferCreateRequest](./retentionoffercreaterequest.md)
  The request body you use to create a retention offer.
- [object RetentionOfferUpdateRequest](./retentionofferupdaterequest.md)
  The request body you use to update a retention offer.
- [object RetentionOfferResponse](./retentionofferresponse.md)
  The response body for endpoints that create, read, or modify a single retention offer.
- [object RetentionOffersResponse](./retentionoffersresponse.md)
  The response body for endpoints that list retention offers.
- [object RetentionOfferPrice](./retentionofferprice.md)
  The territory-specific price point for a retention offer.
- [object RetentionOfferPriceInlineCreate](./retentionofferpriceinlinecreate.md)
  An inline object for specifying territory pricing when creating a retention offer.
- [object RetentionOfferPricesResponse](./retentionofferpricesresponse.md)
  The response body for endpoints that list retention offer prices.
- [object SubscriptionRetentionOffersLinkagesResponse](./subscriptionretentionofferslinkagesresponse.md)
  A response containing the resource identifiers of all retention offers for a subscription.
- [object SubscriptionRetentionMessageOffersLinkagesRequest](./subscriptionretentionmessageofferslinkagesrequest.md)
  The request body you use to add or remove retention offers from a subscription’s retention message.
- [object SubscriptionRetentionMessageOffersLinkagesResponse](./subscriptionretentionmessageofferslinkagesresponse.md)
  A response containing the resource identifiers of retention offers that appear with a subscription’s retention message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionofferpriceslinkagesresponse)*
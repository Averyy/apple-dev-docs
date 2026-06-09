# WinBackOfferPrice

**Framework**: App Store Connect API  
**Kind**: dictionary

The territory-specific customer price and duration for a win-back subscription offer.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object WinBackOfferPrice
```

## Topics

### Objects
- [object WinBackOfferPrice.Relationships](winbackofferprice/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (WinBackOfferPrice.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object WinBackOffer](winbackoffer.md)
  A promotional offer targeting lapsed subscribers, providing a discount or free trial to encourage them to resubscribe.
- [object WinBackOfferCreateRequest](winbackoffercreaterequest.md)
  The request body you use to create a winback offer.
- [object WinBackOfferPriceInlineCreate](winbackofferpriceinlinecreate.md)
  An inline object for specifying territory-specific pricing when creating or updating a win-back offer.
- [object WinBackOfferPricesResponse](winbackofferpricesresponse.md)
  The response body for endpoints that list prices for a win-back offer.
- [object WinBackOfferResponse](winbackofferresponse.md)
  The response body for endpoints that create, read, or modify a single win-back offer for a subscription.
- [object WinBackOfferUpdateRequest](winbackofferupdaterequest.md)
  The request body you use to update a win-back offer.
- [object WinBackOffersResponse](winbackoffersresponse.md)
  The response body for endpoints that list win-back offers for a subscription.
- [object IntegerRange](integerrange.md)
  Describe the upper and lower integer bound of the attribute.
- [object WinBackOfferPricesLinkagesResponse](winbackofferpriceslinkagesresponse.md)
- [object SubscriptionWinBackOffersLinkagesResponse](subscriptionwinbackofferslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/winbackofferprice)*
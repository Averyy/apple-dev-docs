# WinBackOfferResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a single win-back offer for a subscription.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object WinBackOfferResponse
```

## Properties

- `data` (WinBackOffer) *(required)*
- `included` ([WinBackOfferPrice])
- `links` (DocumentLinks) *(required)*

## See Also

- [object WinBackOffer](winbackoffer.md)
  A promotional offer targeting lapsed subscribers, providing a discount or free trial to encourage them to resubscribe.
- [object WinBackOfferCreateRequest](winbackoffercreaterequest.md)
  The request body you use to create a winback offer.
- [object WinBackOfferPrice](winbackofferprice.md)
  The territory-specific customer price and duration for a win-back subscription offer.
- [object WinBackOfferPriceInlineCreate](winbackofferpriceinlinecreate.md)
  An inline object for specifying territory-specific pricing when creating or updating a win-back offer.
- [object WinBackOfferPricesResponse](winbackofferpricesresponse.md)
  The response body for endpoints that list prices for a win-back offer.
- [object WinBackOfferUpdateRequest](winbackofferupdaterequest.md)
  The request body you use to update a win-back offer.
- [object WinBackOffersResponse](winbackoffersresponse.md)
  The response body for endpoints that list win-back offers for a subscription.
- [object IntegerRange](integerrange.md)
  Describe the upper and lower integer bound of the attribute.
- [object WinBackOfferPricesLinkagesResponse](winbackofferpriceslinkagesresponse.md)
- [object SubscriptionWinBackOffersLinkagesResponse](subscriptionwinbackofferslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/winbackofferresponse)*
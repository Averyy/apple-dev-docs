# WinBackOfferCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object WinBackOfferCreateRequest.Data
```

## Topics

### Objects
- [object WinBackOfferCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a winback offer resource.
- [object WinBackOfferCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (WinBackOfferCreateRequest.Data.Attributes) *(required)*: The attributes that describes the request that creates a win-back offer resource.
- `relationships` (WinBackOfferCreateRequest.Data.Relationships) *(required)*: The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `winBackOffers`

## See Also

### Objects
- [object WinBackOfferPriceInlineCreate](../winbackofferpriceinlinecreate.md)
  An inline object for specifying territory-specific pricing when creating or updating a win-back offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/winbackoffercreaterequest/data-data.dictionary)*
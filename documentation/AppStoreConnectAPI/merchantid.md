# MerchantId

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a merchant ID resource.

**Availability**:
- App Store Connect API 3.8+

## Declaration

```swift
object MerchantId
```

## Topics

### Dictionaries
- [object MerchantId.Attributes](merchantid/attributes-data.dictionary.md)
  Attributes that describe a merchant ID resource.
- [object MerchantId.Relationships](merchantid/relationships-data.dictionary.md)
  The relationship you include in the request and those on which you can operate.

## Properties

- `attributes` (MerchantId.Attributes): Attributes that describe a merchant ID resource.
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the merchant ID resource ID from the [`List Merchant IDs`](get-v1-merchantids.md) response.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (MerchantId.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object MerchantIdResponse](merchantidresponse.md)
  A response that contains a single merchant ID resource.
- [object MerchantIdsResponse](merchantidsresponse.md)
  A response that contains a list of merchant ID resources.
- [object MerchantIdCreateRequest](merchantidcreaterequest.md)
  The request body you use to create a merchant ID.
- [object MerchantIdUpdateRequest](merchantidupdaterequest.md)
  The request body you use to update a merchant ID.
- [object MerchantIdCertificatesLinkagesResponse](merchantidcertificateslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/merchantid)*
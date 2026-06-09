# PassTypeId

**Framework**: App Store Connect API  
**Kind**: dictionary

A pass type identifier used to create and manage Wallet passes such as boarding passes, coupons, or loyalty cards.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object PassTypeId
```

## Topics

### Dictionaries
- [object PassTypeId.Attributes](passtypeid/attributes-data.dictionary.md)
  The configurable attributes of a pass type identifier, including its identifier string and description.
- [object PassTypeId.Relationships](passtypeid/relationships-data.dictionary.md)
  The relationships for a pass type identifier, linking it to its associated signing certificates.

## Properties

- `attributes` (PassTypeId.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (PassTypeId.Relationships)
- `type` (string) *(required)*

## See Also

- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object PassTypeIdCertificatesLinkagesResponse](passtypeidcertificateslinkagesresponse.md)
  A response containing the resource identifiers of signing certificates associated with a pass type identifier.
- [object PassTypeIdCreateRequest](passtypeidcreaterequest.md)
  The request body for registering a new pass type identifier for Wallet pass signing.
- [object PassTypeIdResponse](passtypeidresponse.md)
  A response containing a single Wallet pass type identifier.
- [object PassTypeIdUpdateRequest](passtypeidupdaterequest.md)
  The request body you use to update a pass type id update request.
- [object PassTypeIdsResponse](passtypeidsresponse.md)
  A response containing a list of Wallet pass type identifiers registered in your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/passtypeid)*
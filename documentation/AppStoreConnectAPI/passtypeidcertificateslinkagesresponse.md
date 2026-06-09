# PassTypeIdCertificatesLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the resource identifiers of signing certificates associated with a pass type identifier.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object PassTypeIdCertificatesLinkagesResponse
```

## Topics

### Dictionaries
- [object PassTypeIdCertificatesLinkagesResponse.Data](passtypeidcertificateslinkagesresponse/data-data.dictionary.md)
  The resource linkage data identifying a certificate linked to a pass type identifier.

## Properties

- `data` ([PassTypeIdCertificatesLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object PassTypeId](passtypeid.md)
  A pass type identifier used to create and manage Wallet passes such as boarding passes, coupons, or loyalty cards.
- [object PassTypeIdCreateRequest](passtypeidcreaterequest.md)
  The request body for registering a new pass type identifier for Wallet pass signing.
- [object PassTypeIdResponse](passtypeidresponse.md)
  A response containing a single Wallet pass type identifier.
- [object PassTypeIdUpdateRequest](passtypeidupdaterequest.md)
  The request body you use to update a pass type id update request.
- [object PassTypeIdsResponse](passtypeidsresponse.md)
  A response containing a list of Wallet pass type identifiers registered in your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/passtypeidcertificateslinkagesresponse)*
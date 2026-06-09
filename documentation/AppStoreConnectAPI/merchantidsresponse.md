# MerchantIdsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of Apple Pay merchant identifiers registered to your account.

**Availability**:
- App Store Connect API 3.8+

## Declaration

```swift
object MerchantIdsResponse
```

## Properties

- `data` ([MerchantId]) *(required)*
- `included` ([Certificate])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object MerchantId](merchantid.md)
  An Apple Pay merchant identifier registered to your account, used to associate payment capabilities with your app’s bundle ID.
- [object MerchantIdResponse](merchantidresponse.md)
  A response containing a single Apple Pay merchant identifier.
- [object MerchantIdCreateRequest](merchantidcreaterequest.md)
  The request body you use to create a merchant ID.
- [object MerchantIdUpdateRequest](merchantidupdaterequest.md)
  The request body you use to update a merchant ID.
- [object MerchantIdCertificatesLinkagesResponse](merchantidcertificateslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/merchantidsresponse)*
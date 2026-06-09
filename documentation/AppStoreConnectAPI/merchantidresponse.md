# MerchantIdResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single Apple Pay merchant identifier.

**Availability**:
- App Store Connect API 3.8+

## Declaration

```swift
object MerchantIdResponse
```

## Properties

- `data` (MerchantId) *(required)*
- `included` ([Certificate])
- `links` (DocumentLinks) *(required)*

## See Also

- [object MerchantId](merchantid.md)
  An Apple Pay merchant identifier registered to your account, used to associate payment capabilities with your app’s bundle ID.
- [object MerchantIdsResponse](merchantidsresponse.md)
  A response containing a list of Apple Pay merchant identifiers registered to your account.
- [object MerchantIdCreateRequest](merchantidcreaterequest.md)
  The request body you use to create a merchant ID.
- [object MerchantIdUpdateRequest](merchantidupdaterequest.md)
  The request body you use to update a merchant ID.
- [object MerchantIdCertificatesLinkagesResponse](merchantidcertificateslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/merchantidresponse)*
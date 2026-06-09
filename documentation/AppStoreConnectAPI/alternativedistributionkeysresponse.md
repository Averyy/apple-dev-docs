# AlternativeDistributionKeysResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list alternative distribution keys.

**Availability**:
- App Store Connect API 3.4.2+

## Declaration

```swift
object AlternativeDistributionKeysResponse
```

#### Discussion

For more information about the response that includes this alternative distribution key object, see [`AlternativeDistributionKeyResponse`](alternativedistributionkeyresponse.md).

## Properties

- `data` ([AlternativeDistributionKey]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AlternativeDistributionKey](alternativedistributionkey.md)
  A public key used to authorize an alternative marketplace or web distribution to offer your app outside the App Store.
- [object AlternativeDistributionKeyResponse](alternativedistributionkeyresponse.md)
  The response body for endpoints that create or read a single alternative distribution key.
- [object AlternativeDistributionKeyCreateRequest](alternativedistributionkeycreaterequest.md)
  The request body you use to create an alternative distribution key.
- [object AppAlternativeDistributionKeyLinkageResponse](appalternativedistributionkeylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionkeysresponse)*
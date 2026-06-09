# AlternativeDistributionKeyResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create or read a single alternative distribution key.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionKeyResponse
```

#### Discussion

This object is the response from the alternative distribution key endpoints. For more information about alternative distribution keys, see Creating and reading keys.

```javascript
{
  "data": {
     "type": "alternativeDistributionKeys",
     "id": "string",
     "attributes": {
       "publicKey": "string"
     },
     "links": {
       "self": "string"
     }
  },
  "links": {
    "self": "string"
  }
}
```

## Properties

- `data` (AlternativeDistributionKey) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

- [object AlternativeDistributionKey](alternativedistributionkey.md)
  A public key used to authorize an alternative marketplace or web distribution to offer your app outside the App Store.
- [object AlternativeDistributionKeysResponse](alternativedistributionkeysresponse.md)
  The response body for endpoints that list alternative distribution keys.
- [object AlternativeDistributionKeyCreateRequest](alternativedistributionkeycreaterequest.md)
  The request body you use to create an alternative distribution key.
- [object AppAlternativeDistributionKeyLinkageResponse](appalternativedistributionkeylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionkeyresponse)*
# AlternativeDistributionKeyResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a single alternative distribution key resource.

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

## See Also

- [object AlternativeDistributionKey](alternativedistributionkey.md)
  The data structure that represents an alternative distribution key resource.
- [object AlternativeDistributionKeysResponse](alternativedistributionkeysresponse.md)
  A response that contains a list of alternative distribution keys.
- [object AlternativeDistributionKeyCreateRequest](alternativedistributionkeycreaterequest.md)
  The request body you use to create an alternative distribution key.
- [object AppAlternativeDistributionKeyLinkageResponse](appalternativedistributionkeylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionkeyresponse)*
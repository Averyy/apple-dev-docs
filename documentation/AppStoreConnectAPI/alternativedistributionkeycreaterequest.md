# AlternativeDistributionKeyCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create an alternative distribution key.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionKeyCreateRequest
```

#### Discussion

Use this object to create a new alternative distribution key association in App Store Connect. For more infomation about the request that includes this request body, see [`Add an Alternative Distribution Key`](post-v1-alternativedistributionkeys.md).

## Topics

### Objects
- [object AlternativeDistributionKeyCreateRequest.Data](alternativedistributionkeycreaterequest/data-data.dictionary.md)
  The request body you use to create an alternative distribution key.

## Properties

- `data` (AlternativeDistributionKeyCreateRequest.Data) *(required)*

## See Also

- [object AlternativeDistributionKey](alternativedistributionkey.md)
  A public key used to authorize an alternative marketplace or web distribution to offer your app outside the App Store.
- [object AlternativeDistributionKeyResponse](alternativedistributionkeyresponse.md)
  The response body for endpoints that create or read a single alternative distribution key.
- [object AlternativeDistributionKeysResponse](alternativedistributionkeysresponse.md)
  The response body for endpoints that list alternative distribution keys.
- [object AppAlternativeDistributionKeyLinkageResponse](appalternativedistributionkeylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionkeycreaterequest)*
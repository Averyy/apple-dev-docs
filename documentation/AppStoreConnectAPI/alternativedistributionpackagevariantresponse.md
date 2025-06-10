# AlternativeDistributionPackageVariantResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a single alternative distribution package variant resource.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionPackageVariantResponse
```

#### Discussion

This object is the response that contains a single alternative distribution package variant. For more information, see [`Read information for an alternative distribution package variants`](get-v1-alternativedistributionpackagevariants-_id_.md). The schema of the response body is below.

```javascript
{
  "data": {
    "type": "alternativeDistributionPackageVariants",
    "id": "string",
    "attributes": {
      "url": "string",
      "urlExpirationDate": "2025-02-23T06:53:07.520Z",
      "alternativeDistributionKeyBlob": "string"
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

- [object AlternativeDistributionPackage](alternativedistributionpackage.md)
  The data structure that represents an alternative distribution package resource.
- [object AlternativeDistributionPackageCreateRequest](alternativedistributionpackagecreaterequest.md)
  The request body you use to create an alternative distribution package.
- [object AlternativeDistributionPackageResponse](alternativedistributionpackageresponse.md)
  A response that contains a single alternative distribution package resource.
- [object AlternativeDistributionPackageVersion](alternativedistributionpackageversion.md)
  The data structure that represents an alternative distribution package version resource.
- [object AlternativeDistributionPackageVersionResponse](alternativedistributionpackageversionresponse.md)
  A response that contains a single alternative distribution package version resource.
- [object AlternativeDistributionPackageVersionsResponse](alternativedistributionpackageversionsresponse.md)
  A response that contains a list of alternative distribution package version resources.
- [object AlternativeDistributionPackageDelta](alternativedistributionpackagedelta.md)
  The data structure that represents an alternative distribution package delta resource.
- [object AlternativeDistributionPackageDeltaResponse](alternativedistributionpackagedeltaresponse.md)
  A response that contains a single alternative distribution package delta resource.
- [object AlternativeDistributionPackageDeltasResponse](alternativedistributionpackagedeltasresponse.md)
  A response that contains a list of alternative distribution package delta resources.
- [object AlternativeDistributionPackageVariant](alternativedistributionpackagevariant.md)
  The data structure that represents an alternative distribution package variant resource.
- [object AlternativeDistributionPackageVariantsResponse](alternativedistributionpackagevariantsresponse.md)
  A response that contains a list of alternative distribution package variant resources.
- [object AlternativeDistributionPackageVersionDeltasLinkagesResponse](alternativedistributionpackageversiondeltaslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionVariantsLinkagesResponse](alternativedistributionpackageversionvariantslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackagevariantresponse)*
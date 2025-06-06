# AlternativeDistributionPackageVariantsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of alternative distribution package variant resources.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionPackageVariantsResponse
```

#### Discussion

This object is the response that contains a list of alternative distribution package variants. For more information, see [`List variants information`](get-v1-alternativedistributionpackageversions-_id_-variants.md). The schema of the response body is below.

```javascript
{
  "data": [
    {
      "type": "alternativeDistributionPackageVariants",
      "id": "string",
      "attributes": {
        "url": "string",
        "urlExpirationDate": "2024-02-27T00:58:50.105Z",
        "alternativeDistributionKeyBlob": "string"
      },
      "links": {
        "self": "string"
      }
    }
  ],
  "links": {
    "self": "string",
    "first": "string",
    "next": "string"
  },
  "meta": {
    "paging": {
      "total": 0,
      "limit": 0
    }
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
- [object AlternativeDistributionPackageVariantResponse](alternativedistributionpackagevariantresponse.md)
  A response that contains a single alternative distribution package variant resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackagevariantsresponse)*
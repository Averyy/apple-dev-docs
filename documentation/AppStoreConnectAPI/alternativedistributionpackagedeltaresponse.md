# AlternativeDistributionPackageDeltaResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single delta update for an alternative distribution package.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionPackageDeltaResponse
```

#### Discussion

This object is the response that contains a single alternative distribution package delta. For more information about alternative distribution package deltas see [`Read Information for Alternative Distribution Package Deltas`](get-v1-alternativedistributionpackagedeltas-_id_.md). The schema of the response body is below.

```javascript
{
  "data": {
    "type": "alternativeDistributionPackageDeltas",
    "id": "string",
    "attributes": {
      "url": "string",
      "urlExpirationDate": "2024-02-23T06:50:07.723Z",
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

## Properties

- `data` (AlternativeDistributionPackageDelta) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

- [object AlternativeDistributionPackage](alternativedistributionpackage.md)
  The distributable package for an app on an alternative marketplace or web distribution, containing versioned variants and delta updates.
- [object AlternativeDistributionPackageCreateRequest](alternativedistributionpackagecreaterequest.md)
  The request body you use to create an alternative distribution package.
- [object AlternativeDistributionPackageResponse](alternativedistributionpackageresponse.md)
  The response body for endpoints that read a single alternative distribution package.
- [object AlternativeDistributionPackageVersion](alternativedistributionpackageversion.md)
  A versioned snapshot of an alternative distribution package, containing its variants and delta updates.
- [object AlternativeDistributionPackageVersionResponse](alternativedistributionpackageversionresponse.md)
  The response body for endpoints that read a single alternative distribution package version.
- [object AlternativeDistributionPackageVersionsResponse](alternativedistributionpackageversionsresponse.md)
  The response body for endpoints that list versions of an alternative distribution package.
- [object AlternativeDistributionPackageDelta](alternativedistributionpackagedelta.md)
  An incremental update package for an alternative distribution app, containing only the changes between two versions to reduce download size.
- [object AlternativeDistributionPackageDeltasResponse](alternativedistributionpackagedeltasresponse.md)
  A response containing a list of delta updates available for an alternative distribution package.
- [object AlternativeDistributionPackageVariant](alternativedistributionpackagevariant.md)
  A device-specific file package within an alternative distribution app, targeting a particular device family.
- [object AlternativeDistributionPackageVariantResponse](alternativedistributionpackagevariantresponse.md)
  A response containing a single variant of an alternative distribution package.
- [object AlternativeDistributionPackageVariantsResponse](alternativedistributionpackagevariantsresponse.md)
  A response containing a list of device-specific variants within an alternative distribution package.
- [object AlternativeDistributionPackageVersionDeltasLinkagesResponse](alternativedistributionpackageversiondeltaslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionVariantsLinkagesResponse](alternativedistributionpackageversionvariantslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackagedeltaresponse)*
# AlternativeDistributionPackageVersionsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object AlternativeDistributionPackageVersionsLinkagesResponse
```

## Topics

### Dictionaries
- [object AlternativeDistributionPackageVersionsLinkagesResponse.Data](alternativedistributionpackageversionslinkagesresponse/data-data.dictionary.md)

## Properties

- `data` ([AlternativeDistributionPackageVersionsLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

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
- [object AlternativeDistributionPackageDeltaResponse](alternativedistributionpackagedeltaresponse.md)
  A response containing a single delta update for an alternative distribution package.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackageversionslinkagesresponse)*
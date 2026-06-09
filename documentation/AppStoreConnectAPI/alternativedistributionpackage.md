# AlternativeDistributionPackage

**Framework**: App Store Connect API  
**Kind**: dictionary

The distributable package for an app on an alternative marketplace or web distribution, containing versioned variants and delta updates.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionPackage
```

#### Discussion

To learn more about the response that includes this alternative distribution package object, see [`AlternativeDistributionPackageResponse`](alternativedistributionpackageresponse.md).

## Topics

### Objects
- [object AlternativeDistributionPackage.Relationships](alternativedistributionpackage/relationships-data.dictionary.md)
  The relationships for an alternative distribution package, linking it to its versions.
### Dictionaries
- [object AlternativeDistributionPackage.Attributes](alternativedistributionpackage/attributes-data.dictionary.md)
  Attributes that describe an alternative distribution package resource.

## Properties

- `attributes` (AlternativeDistributionPackage.Attributes)
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the alternative distribution package.
- `links` (ResourceLinks)
- `relationships` (AlternativeDistributionPackage.Relationships)
- `type` (string) *(required)*

## See Also

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
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackage)*
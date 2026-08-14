# Alternative Distribution Packages

**Framework**: App Store Connect API

Create and read distribution packages for an alternative app distribution.

#### Overview

App developers can get alternative distribution package IDs through the App Store Connect API by using [`Read an app store version’s alternative distribution package`](get-v1-appstoreversions-_id_-alternativedistributionpackage.md). You can also get the IDs in App Store Connect, to learn more, see [`Get an alternative distribution package ID`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/get-an-alternative-distribution-package-id).

The alternative distribution package ID is valid for distributing a marketplace app, an app on an alternative marketplace, or through web distribution. To learn more about creating alternative distribution packages, see [`Creating alternative distribution packages`](creating-alternative-distribution-packages.md).

To learn more about ingesting alternative distribution packages as a marketplace, see [`Processing alternative app marketplace notifications`](https://developer.apple.com/documentation/marketplacekit/processing-alternative-marketplace-notifications).

## Topics

### Creating and reading distribution packages
- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read Alternative Distribution Package Information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Create an Alternative Distribution Package](post-v1-alternativedistributionpackages.md)
  Create an alternative distribution package for an App Store version.
- [Read an app store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.
- [Read Version Information for an Alternative Distribution Package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.
### Getting version information
- [Read Information for an Alternative Distribution Package Version](get-v1-alternativedistributionpackageversions-_id_.md)
  Get detail information about a specific alternative distribution package version.
- [Read Version Information for an Alternative Distribution Package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.
- [List Deltas Information](get-v1-alternativedistributionpackageversions-_id_-deltas.md)
  List deltas for a specific alternative distribution package version.
- [List Variants Information](get-v1-alternativedistributionpackageversions-_id_-variants.md)
  List variants for specific alternative distribution package version.
- [List delta ids](get-v1-alternativedistributionpackageversions-_id_-relationships-deltas.md)
  List all delta Ids for a specific alternative distribution package version.
- [List variant ids information](get-v1-alternativedistributionpackageversions-_id_-relationships-variants.md)
  List variant Ids for specific alternative distribution package version.
- [Read version ids for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-relationships-versions.md)
  Get version IDs about a specific alternative distribution package.
### Getting delta information
- [Read Information for Alternative Distribution Package Deltas](get-v1-alternativedistributionpackagedeltas-_id_.md)
  Get detail information about specific alternative distribution package deltas.
- [List Deltas Information](get-v1-alternativedistributionpackageversions-_id_-deltas.md)
  List deltas for a specific alternative distribution package version.
### Getting variant information
- [Read variant information for an alternative distribution package](get-v1-alternativedistributionpackagevariants-_id_.md)
  Get detail information about specific alternative distribution package variants.
- [List Variants Information](get-v1-alternativedistributionpackageversions-_id_-variants.md)
  List variants for specific alternative distribution package version.
### Objects
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
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)

## See Also

- [Notifications](notifications.md)
  Add and read information for alternative distribution package notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternative-distribution-packages)*
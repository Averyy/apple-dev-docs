# Alternative Distribution Packages

**Framework**: App Store Connect API

Create and read distribution packages for an alternative app distribution.

#### Overview

App developers can get alternative distribution package IDs through the App Store Connect API by using [`Read an App Store version’s alternative distribution package`](get-v1-appstoreversions-_id_-alternativedistributionpackage.md). You can also get the IDs in App Store Connect, to learn more, see [`Get an alternative distribution package ID`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/get-an-alternative-distribution-package-id).

The alternative distribution package ID is valid for distributing a marketplace app, an app on an alternative marketplace, or through web distribution. To learn more about creating alternative distribution packages, see [`Creating alternative distribution packages`](creating-alternative-distribution-packages.md).

To learn more about ingesting alternative distribution packages as a marketplace, see [`Processing alternative app marketplace notifications`](https://developer.apple.com/documentation/appdistribution/processing-alternative-marketplace-notifications).

## Topics

### Creating and reading distribution packages
- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read alternative distribution package information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Create an alternative distribution package](post-v1-alternativedistributionpackages.md)
  Create an alternative distribution package for an app store version.
- [Read an App Store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.
- [Read version information for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.
### Getting version information
- [Read information for an alternative distribution package version](get-v1-alternativedistributionpackageversions-_id_.md)
  Get detail information about a specific alternative distribution package version.
- [Read version information for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.
- [List deltas information](get-v1-alternativedistributionpackageversions-_id_-deltas.md)
  List deltas for a specific alternative distribution package version.
- [List variants information](get-v1-alternativedistributionpackageversions-_id_-variants.md)
  List variants for specific alternative distribution package version.
- [List delta Ids](get-v1-alternativedistributionpackageversions-_id_-relationships-deltas.md)
  List all delta Ids for a specific alternative distribution package version.
- [List variant Ids information](get-v1-alternativedistributionpackageversions-_id_-relationships-variants.md)
  List variant Ids for specific alternative distribution package version.
- [Read version Ids for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-relationships-versions.md)
  Get version IDs about a specific alternative distribution package.
### Getting delta information
- [Read information for alternative distribution package deltas](get-v1-alternativedistributionpackagedeltas-_id_.md)
  Get detail information about specific alternative distribution package deltas.
- [List deltas information](get-v1-alternativedistributionpackageversions-_id_-deltas.md)
  List deltas for a specific alternative distribution package version.
### Getting variant information
- [Read information for an alternative distribution package variants](get-v1-alternativedistributionpackagevariants-_id_.md)
  Get detail information about specific alternative distribution package variants.
- [List variants information](get-v1-alternativedistributionpackageversions-_id_-variants.md)
  List variants for specific alternative distribution package version.
### Objects
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
- [object AlternativeDistributionPackageVariantsResponse](alternativedistributionpackagevariantsresponse.md)
  A response that contains a list of alternative distribution package variant resources.
- [object AlternativeDistributionPackageVersionDeltasLinkagesResponse](alternativedistributionpackageversiondeltaslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionVariantsLinkagesResponse](alternativedistributionpackageversionvariantslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)

## See Also

- [Notifications](notifications.md)
  Add and read information for alternative distribution package notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternative-distribution-packages)*
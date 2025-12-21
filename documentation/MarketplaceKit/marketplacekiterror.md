# MarketplaceKitError

**Framework**: MarketplaceKit  
**Kind**: enum

Errors that the MarketplaceKit framework can throw.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
enum MarketplaceKitError
```

#### Overview

The [`AppLibrary`](applibrary.md) class `requestAppInstallation()` functions can throw an error of this type.

## Topics

### Device and platform compatibility errors
- [MarketplaceKitError.minimumPlatformVersionNotSatisfied(_:)](marketplacekiterror/minimumplatformversionnotsatisfied(_:).md)
  An error that indicates the device has a lower platform version than that required by the requested app.
- [MarketplaceKitError.missingCapabilities(_:)](marketplacekiterror/missingcapabilities(_:).md)
  An error that indicates the device lacks capabilities that requested app requires.
- [MarketplaceKitError.noSupportedVariant](marketplacekiterror/nosupportedvariant.md)
  An error that indicates the requested app doesn’t have a supported variant for this device.
- [MarketplaceKitError.unsupportedPlatform](marketplacekiterror/unsupportedplatform.md)
  An error that indicates that the requested app doesn’t support the platform.
- [case insufficientStorageSpace(Measurement<UnitInformationStorage>)](marketplacekiterror/insufficientstoragespace(_:).md)
  An error that indicates that the device lacks the required disk space to install the app.
### Installation and permission errors
- [MarketplaceKitError.appNotInstalled](marketplacekiterror/appnotinstalled.md)
  An error that indicates that a requested operation requires that the app first exists on the device.
- [MarketplaceKitError.installationOfMarketplaceDenied](marketplacekiterror/installationofmarketplacedenied.md)
  An error that indicates that the device disallows the installation of marketplaces.
- [MarketplaceKitError.installationRestricted](marketplacekiterror/installationrestricted.md)
  An error that indicates that app installation is restricted on this device.
- [MarketplaceKitError.mismatchedInstallType](marketplacekiterror/mismatchedinstalltype.md)
  An error that indicates the provided install type (install, update, restore) doesn’t match the install that results.
- [MarketplaceKitError.missingInstallVerificationToken](marketplacekiterror/missinginstallverificationtoken.md)
  An error that indicates the required install verification token is missing.
### Content validation and security errors
- [MarketplaceKitError.invalidAlternativeDistributionPackageSignature](marketplacekiterror/invalidalternativedistributionpackagesignature.md)
  An error that indicates the alternative-distribution-package signature is invalid.
- [MarketplaceKitError.invalidAlternativeDistributionPackageURL](marketplacekiterror/invalidalternativedistributionpackageurl.md)
  An error that indicates the alternative-distribution-package URL is invalid.
- [MarketplaceKitError.invalidLicense](marketplacekiterror/invalidlicense.md)
  An error that indicates that a license your server provides is invalid.
- [MarketplaceKitError.invalidManifest](marketplacekiterror/invalidmanifest.md)
  An error that indicates that the app manifest provided by your server is invalid.
- [MarketplaceKitError.invalidURL](marketplacekiterror/invalidurl.md)
  An error that indicates that a URL your server or app provides is invalid.
### Age-rating errors
- [MarketplaceKitError.ageRatingExceptionNotNeeded](marketplacekiterror/ageratingexceptionnotneeded.md)
  An error that indicates the app requests an unnecessary age-rating exception.
- [MarketplaceKitError.missingAgeRatingExceptionRequest](marketplacekiterror/missingageratingexceptionrequest.md)
  An error that indicates the app needs to request an age-rating exception.
- [MarketplaceKitError.ratingRestricted](marketplacekiterror/ratingrestricted.md)
  An error that indicates the requested app’s age rating is beyond that allowed for the device.
### System and network errors
- [MarketplaceKitError.cancelled](marketplacekiterror/cancelled.md)
  An error that indicates the app isn’t eligible for installation.
- [MarketplaceKitError.featureUnavailable](marketplacekiterror/featureunavailable.md)
  An error that indicates that the requested feature is unavailable.
- [MarketplaceKitError.networkError](marketplacekiterror/networkerror.md)
  An error that indicates a network error occurs during a request.
- [MarketplaceKitError.oauthTokenError](marketplacekiterror/oauthtokenerror.md)
  An error that indicates that the framework failed to retrieve an authorization token.
- [MarketplaceKitError.unknown](marketplacekiterror/unknown.md)
  An error that indicates failure due to an unknown error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror)*
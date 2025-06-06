# MarketplaceKitError

**Framework**: MarketplaceKit  
**Kind**: enum

Errors that can occur in the marketplace workflow.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum MarketplaceKitError
```

#### Overview

The [`AppLibrary`](applibrary.md) variety of functions `requestAppInstallation(...)` can throw an error of this type.

## Topics

### Enumeration Cases
- [MarketplaceKitError.appNotInstalled](marketplacekiterror/appnotinstalled.md)
  The requested operation cannot be completed because the app isn’t installed
- [MarketplaceKitError.cancelled](marketplacekiterror/cancelled.md)
  The app isn’t eligible to be installed
- [MarketplaceKitError.featureUnavailable](marketplacekiterror/featureunavailable.md)
  The requested feature is unavailable
- [MarketplaceKitError.installationOfMarketplaceDenied](marketplacekiterror/installationofmarketplacedenied.md)
  Installations of marketplaces are denied on this device.
- [MarketplaceKitError.installationRestricted](marketplacekiterror/installationrestricted.md)
  Installations are restricted on this device.
- [case insufficientStorageSpace(Measurement<UnitInformationStorage>)](marketplacekiterror/insufficientstoragespace(_:).md)
  The requested install requires more storage space than the device has available.
- [MarketplaceKitError.invalidAlternativeDistributionPackageSignature](marketplacekiterror/invalidalternativedistributionpackagesignature.md)
  The signature of the Alternative Distribution Package wasn’t available or was invalid
- [MarketplaceKitError.invalidAlternativeDistributionPackageURL](marketplacekiterror/invalidalternativedistributionpackageurl.md)
  Invalid URL for an Alternative Distribution Package
- [MarketplaceKitError.invalidLicense](marketplacekiterror/invalidlicense.md)
  No valid license provided
- [MarketplaceKitError.invalidManifest](marketplacekiterror/invalidmanifest.md)
  The manifest is invalid, or cannot be read
- [MarketplaceKitError.invalidURL](marketplacekiterror/invalidurl.md)
  An invalid URL was provided
- [MarketplaceKitError.minimumPlatformVersionNotSatisfied(_:)](marketplacekiterror/minimumplatformversionnotsatisfied(_:).md)
  The requested install requires a minimum platform version that is greater than this device.
- [MarketplaceKitError.mismatchedInstallType](marketplacekiterror/mismatchedinstalltype.md)
  The provided install type doesn’t match the install that would occur
- [MarketplaceKitError.missingCapabilities(_:)](marketplacekiterror/missingcapabilities(_:).md)
  The requested install requires capabilities not available on this device.
- [MarketplaceKitError.missingInstallVerificationToken](marketplacekiterror/missinginstallverificationtoken.md)
  The required install verification token is missing
- [MarketplaceKitError.networkError](marketplacekiterror/networkerror.md)
  A network error occurred during the request
- [MarketplaceKitError.noSupportedVariant](marketplacekiterror/nosupportedvariant.md)
  The requested install has no supported variant for this device.
- [MarketplaceKitError.oauthTokenError](marketplacekiterror/oauthtokenerror.md)
  An error fetching an OAuth Token
- [MarketplaceKitError.ratingRestricted](marketplacekiterror/ratingrestricted.md)
  The requested install has a rating that exceeds this device’s restrictions.
- [MarketplaceKitError.unknown](marketplacekiterror/unknown.md)
  Failure due to an unknown error.
- [MarketplaceKitError.unsupportedPlatform](marketplacekiterror/unsupportedplatform.md)
  The requested install does not run on this device’s platform.
### Initializers
- [init(from: any Decoder) throws](marketplacekiterror/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var description: String](marketplacekiterror/description.md)
  A textual representation of this instance.
### Instance Methods
- [func encode(to: any Encoder) throws](marketplacekiterror/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Error Implementations](marketplacekiterror/error-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror)*
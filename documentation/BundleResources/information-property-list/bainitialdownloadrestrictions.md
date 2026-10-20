# BAInitialDownloadRestrictions

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The restrictions that apply to the set of assets that download immediately after app installation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Details

- **Name**: `BAInitialDownloadRestrictions`
- **Type**: dictionary

#### Discussion

This key is required to use Background Assets.

## Topics

### Initial download restrictions
- [BADownloadAllowance](./bainitialdownloadrestrictions/badownloadallowance.md)
  The combined, maximum size of the initial, non-essential asset download files.
- [BADownloadDomainAllowList](./bainitialdownloadrestrictions/badownloaddomainallowlist.md)
  The permitted list of domains the extension can use when scheduling the initial set of asset downloads.
- [BAEssentialDownloadAllowance](./bainitialdownloadrestrictions/baessentialdownloadallowance.md)
  The combined, maximum size of the essential asset download files.

## See Also

### Background downloads
- [BAUsesAppleHosting](./bausesapplehosting.md)
  A Boolean value that indicates whether you use Apple’s service to host your asset packs.
- [BAHasManagedAssetPacks](./bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.
- [BAAppGroupID](./baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAMaxInstallSize](./bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [BAManifestURL](./bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAEssentialMaxInstallSize](./baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bainitialdownloadrestrictions)*
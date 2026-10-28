# BAHasManagedAssetPacks

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether you let the system automatically manage your asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 16.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Details

- **Name**: `BAHasManagedAssetPacks`
- **Type**: boolean

## Discussion

Set this key to `YES` if you want the system to automatically download your asset packs and keep them up to date in the background.

Then, in your app’s code, manage asset-pack downloads using the `AssetPackManager` actor. In your extension code, use the StoreKit `StoreDownloaderExtension` protocol if you set the [`BAUsesAppleHosting`](./bausesapplehosting.md) key to `YES`; otherwise, use the Background Assets `ManagedDownloaderExtension` protocol.

## See Also

### Background downloads
- [BAUsesAppleHosting](./bausesapplehosting.md)
  A Boolean value that indicates whether you use Apple’s service to host your asset packs.
- [BAAppGroupID](./baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAInitialDownloadRestrictions](./bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAMaxInstallSize](./bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [BAManifestURL](./bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAEssentialMaxInstallSize](./baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bahasmanagedassetpacks)*
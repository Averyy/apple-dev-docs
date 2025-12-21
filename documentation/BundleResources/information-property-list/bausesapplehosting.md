# BAUsesAppleHosting

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether you use Apple’s service to host your asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 16.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

#### Discussion

Use this key if you set the [`BAHasManagedAssetPacks`](information-property-list/bahasmanagedassetpacks.md) key to  `YES`. Then, if you set this key to `YES`, use the StoreKit `StoreDownloaderExtension` protocol in your extension; otherwise, use the Background Assets `ManagedDownloaderExtension` protocol.

## See Also

- [BAHasManagedAssetPacks](information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.
- [BAAppGroupID](information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAInitialDownloadRestrictions](information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAMaxInstallSize](information-property-list/bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [BAManifestURL](information-property-list/bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAEssentialMaxInstallSize](information-property-list/baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bausesapplehosting)*
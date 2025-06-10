# BAMaxInstallSize

**Framework**: Bundle Resources  
**Kind**: typealias

The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

#### Discussion

> ❗ **Important**:  The App Store uses this key to show the size of your app on the product page, so provide an accurate value. If you compress the assets, use the uncompressed size of the files for this value. Don’t overstate the disk space you require.

This key is required to use Background Assets.

## See Also

- [BAUsesAppleHosting](information-property-list/bausesapplehosting.md)
  A Boolean value that indicates whether you use Apple’s service to host your asset packs.
- [BAHasManagedAssetPacks](information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.
- [BAAppGroupID](information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAInitialDownloadRestrictions](information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAManifestURL](information-property-list/bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAEssentialMaxInstallSize](information-property-list/baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bamaxinstallsize)*
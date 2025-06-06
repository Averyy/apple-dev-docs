# BAEssentialMaxInstallSize

**Framework**: Bundle Resources  
**Kind**: typealias

The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 18.4+
- visionOS 2.4+

#### Discussion

> ❗ **Important**:  The App Store uses this key to show the size of your app on the product page, so provide an accurate value. If you compress the assets, use the uncompressed size of the files for this value. Don’t overstate the disk space you require.

 The App Store uses this key to show the size of your app on the product page, so provide an accurate value. If you compress the assets, use the uncompressed size of the files for this value. Don’t overstate the disk space you require.

This key is required to use Background Assets.

## See Also

- [BAInitialDownloadRestrictions](information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAMaxInstallSize](information-property-list/bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [BAManifestURL](information-property-list/bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/baessentialmaxinstallsize)*
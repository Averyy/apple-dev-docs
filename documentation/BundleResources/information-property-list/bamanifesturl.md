# BAManifestURL

**Framework**: Bundle Resources  
**Kind**: typealias

The location URL of the app’s manifest file that contains the names and sizes of assets.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

#### Discussion

The manifest file contains information that your extension needs to schedule asset downloads, such as the names, URLs, and sizes of the assets. The format and content of the manifest file is your responsibility. The system uses this key to download the manifest file and pass it to your extension. This key is required to use Background Assets.

## See Also

- [BAUsesAppleHosting](information-property-list/bausesapplehosting.md)
  A Boolean value that indicates whether you use Apple’s service to host your asset packs.
- [BAHasManagedAssetPacks](information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.
- [BAAppGroupID](information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAInitialDownloadRestrictions](information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAMaxInstallSize](information-property-list/bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [BAEssentialMaxInstallSize](information-property-list/baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bamanifesturl)*
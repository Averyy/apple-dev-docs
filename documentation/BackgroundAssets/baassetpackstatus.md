# BAAssetPackStatus

**Framework**: Background Assets  
**Kind**: enum  
**Role**: Enumeration

The status of an asset pack.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
enum BAAssetPackStatus : NSUInteger;
```

## Topics

### Enumeration Cases
- [BAAssetPackStatusDownloadAvailable](./baassetpackstatus/baassetpackstatusdownloadavailable.md)
  A status value that indicates that the asset pack is available to download.
- [BAAssetPackStatusDownloaded](./baassetpackstatus/baassetpackstatusdownloaded.md)
  A status value that indicates that the system finished downloading the asset pack.
- [BAAssetPackStatusDownloading](./baassetpackstatus/baassetpackstatusdownloading.md)
  A status value that indicates that the system is currently downloading the asset pack.
- [BAAssetPackStatusObsolete](./baassetpackstatus/baassetpackstatusobsolete.md)
  A status value that indicates that the asset pack is no longer available to download.
- [BAAssetPackStatusOutOfDate](./baassetpackstatus/baassetpackstatusoutofdate.md)
  A status value that indicates that the downloaded asset pack is out of date.
- [BAAssetPackStatusUpToDate](./baassetpackstatus/baassetpackstatusuptodate.md)
  A status value that indicates that the downloaded asset pack is up to date.
- [BAAssetPackStatusUpdateAvailable](./baassetpackstatus/baassetpackstatusupdateavailable.md)
  A status value that indicates that an update to the asset pack is available to download.

## See Also

### Managed asset packs
- [BAAssetPack](./baassetpack.md)
  An archive of assets that the system downloads together.
- [BAAssetPackManager](./baassetpackmanager.md)
  A class that manages asset packs.
- [BAAssetPackManifest](./baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [BAManagedDownloaderExtension](./bamanageddownloaderextension.md)
  An application extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAManagedAssetPackDownloadDelegate](./bamanagedassetpackdownloaddelegate.md)
  An object that handles status updates when downloading an asset pack.
- [BAAppGroupID](../BundleResources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackstatus)*
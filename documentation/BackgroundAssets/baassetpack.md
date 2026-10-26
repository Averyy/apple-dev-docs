# BAAssetPack

**Framework**: Background Assets  
**Kind**: class  
**Role**: Class

An archive of assets that the system downloads together.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface BAAssetPack : NSObject
```

#### Overview

An instance of this class can be invalidated when the asset pack that it represents is updated on the server.

## Topics

### Identifying assets
- [identifier](./baassetpack/identifier.md)
  A unique identifier for the asset pack.
- [version](./baassetpack/version.md)
  The asset pack’s version number
### Accessing asset details
- [userInfo](./baassetpack/userinfo.md)
  JSON-encoded custom information that’s associated with the asset pack.
### Accessing asset language
- [language](./baassetpack/language.md)
  The language, represented as a BCP-47 identifier, for which this asset pack is localized.
### Downloading assets
- [- download](./baassetpack/download.md)
  Creates a download object for the asset pack that you schedule using a download manager.
- [- downloadForContentRequest:](./baassetpack/downloadforcontentrequest_.md)
  Creates a download object for the asset pack that you schedule using a download manager.
- [downloadSize](./baassetpack/downloadsize.md)
  The size of the download file containing the asset pack in bytes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Managed asset packs
- [BAAssetPackStatus](./baassetpackstatus.md)
  The status of an asset pack.
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

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpack)*
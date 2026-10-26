# BAManagedAssetPackDownloadDelegate

**Framework**: Background Assets  
**Kind**: protocol  
**Role**: Protocol

An object that handles status updates when downloading an asset pack.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@protocol BAManagedAssetPackDownloadDelegate <NSObject>
```

## Mentions

- [Downloading Apple-hosted asset packs](./downloading-apple-hosted-asset-packs.md)

## Topics

### Tracking downloads
- [- downloadOfAssetPackBegan:](./bamanagedassetpackdownloaddelegate/downloadofassetpackbegan_.md)
  Notifies the receiver that the download began or resumed after being paused.
- [- downloadOfAssetPack:hasProgress:](./bamanagedassetpackdownloaddelegate/downloadofassetpack_hasprogress_.md)
  Notifies the receiver that the download is in progress.
- [- downloadOfAssetPackPaused:](./bamanagedassetpackdownloaddelegate/downloadofassetpackpaused_.md)
  Notifies the receiver that the download paused.
- [- downloadOfAssetPackFinished:](./bamanagedassetpackdownloaddelegate/downloadofassetpackfinished_.md)
  Notifies the receiver that the download completed and that the asset pack is available locally.
- [- downloadOfAssetPack:failedWithError:](./bamanagedassetpackdownloaddelegate/downloadofassetpack_failedwitherror_.md)
  Notifies the receiver that the download failed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managed asset packs
- [BAAssetPack](./baassetpack.md)
  An archive of assets that the system downloads together.
- [BAAssetPackStatus](./baassetpackstatus.md)
  The status of an asset pack.
- [BAAssetPackManager](./baassetpackmanager.md)
  A class that manages asset packs.
- [BAAssetPackManifest](./baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [BAManagedDownloaderExtension](./bamanageddownloaderextension.md)
  An application extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAAppGroupID](../BundleResources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bamanagedassetpackdownloaddelegate)*
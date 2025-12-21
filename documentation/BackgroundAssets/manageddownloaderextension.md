# ManagedDownloaderExtension

**Framework**: Background Assets  
**Kind**: protocol

An app extension that uses the system implementation to schedule asset-pack downloads automatically.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol ManagedDownloaderExtension : BADownloaderExtension where Self.Configuration : ManagedDownloaderExtensionConfiguration
```

#### Overview

The protocol provides default implementations for all of the inherited `BADownloaderExtension` requirements.

> ⚠️ **Warning**: Don’t implement any of the inherited `BADownloaderExtension` requirements aside from, optionally, [`backgroundDownload(_:didReceive:)`](badownloaderextension-qwaw/backgrounddownload(_:didreceive:).md).

## Topics

### Downloading assets
- [func shouldDownload(AssetPack) -> Bool](manageddownloaderextension/shoulddownload(_:).md)
  Determines whether to download an asset pack.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [BADownloaderExtension](badownloaderextension-qwaw.md)

## See Also

- [struct AssetPack](assetpack.md)
  An archive of assets that the system downloads together.
- [actor AssetPackManager](assetpackmanager.md)
  An actor that manages asset packs.
- [BAAppGroupID](../BundleResources/Information-Property-List/BAAppGroupID.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/Information-Property-List/BAHasManagedAssetPacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextension)*
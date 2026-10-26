# BAAssetPackManifest

**Framework**: Background Assets  
**Kind**: class  
**Role**: Class

A manifest of asset packs that are available to download.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface BAAssetPackManifest : NSObject
```

## Mentions

- [Reducing download and storage demands with localized asset packs](./reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Topics

### Creating an asset pack manifest
- [- initWithContentsOfURL:applicationGroupIdentifier:error:](./baassetpackmanifest/initwithcontentsofurl_applicationgroupidentifier_error_.md)
  Initializes a representation of a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.
- [- initFromData:applicationGroupIdentifier:error:](./baassetpackmanifest/initfromdata_applicationgroupidentifier_error_.md)
  Initializes a representation of a manifest in memory from JSON-encoded data.
### Accessing downloads
- [- allDownloads](./baassetpackmanifest/alldownloads.md)
  Creates download objects for every asset pack in this manifest.
- [- allDownloadsForContentRequest:](./baassetpackmanifest/alldownloadsforcontentrequest_.md)
  Creates download objects for every asset pack in this manifest.
### Getting asset packs
- [assetPacks](./baassetpackmanifest/assetpacks.md)
  The asset packs in this manifest that are available to download.
- [- assetPackWithIdentifier:](./baassetpackmanifest/assetpackwithidentifier_.md)
  Returns the asset pack in this manifest with the given identifier.
### Getting localized asset packs
- [localizedAssetPacks](./baassetpackmanifest/localizedassetpacks.md)
  The subset of asset packs in this manifest that best match the current preferred languages.
- [- localizedAssetPacksForLanguage:](./baassetpackmanifest/localizedassetpacksforlanguage_.md)
  Returns the subset of asset packs in this manifest that are available to download and that best match the specified language.
### Inspecting asset pack localization
- [primaryLanguage](./baassetpackmanifest/primarylanguage.md)
  The application’s primary language, represented as a BCP-47 identifier, as configured in App Store Connect.
- [availableLanguages](./baassetpackmanifest/availablelanguages.md)
  The languages, represented as their respective BCP-47 identifiers, for which asset packs in this manifest are localized.
- [resolvedLanguage](./baassetpackmanifest/resolvedlanguage.md)
  The language, represented as a BCP-47 identifier, asset packs in this manifest that are localized for which the system automatically makes available locally.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Managed asset packs
- [BAAssetPack](./baassetpack.md)
  An archive of assets that the system downloads together.
- [BAAssetPackStatus](./baassetpackstatus.md)
  The status of an asset pack.
- [BAAssetPackManager](./baassetpackmanager.md)
  A class that manages asset packs.
- [BAManagedDownloaderExtension](./bamanageddownloaderextension.md)
  An application extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAManagedAssetPackDownloadDelegate](./bamanagedassetpackdownloaddelegate.md)
  An object that handles status updates when downloading an asset pack.
- [BAAppGroupID](../BundleResources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest)*
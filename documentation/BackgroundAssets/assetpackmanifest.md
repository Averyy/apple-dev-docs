# AssetPackManifest

**Framework**: Background Assets  
**Kind**: struct

A manifest of asset packs that are available to download.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AssetPackManifest
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Topics

### Creating an asset pack manifest
- [init(contentsOf: URL, appGroupID: String) throws](assetpackmanifest/init(contentsof:appgroupid:).md)
  Creates a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.
- [init(from: Data, appGroupID: String) throws](assetpackmanifest/init(from:appgroupid:).md)
  Creates a manifest in memory given JSON-encoded data.
### Accessing downloads
- [func allDownloads(for: BAContentRequest?) -> Set<BADownload>](assetpackmanifest/alldownloads(for:).md)
  Creates download objects for every applicable asset pack in this manifest, which can be scheduled with the download manager.
### Getting asset packs
- [let assetPacks: Set<AssetPack>](assetpackmanifest/assetpacks.md)
  The asset packs in this manifest that are available to download.
- [func assetPack(withID: String) -> AssetPack?](assetpackmanifest/assetpack(withid:).md)
  Returns the asset pack in this manifest with the given ID.
### Getting localized asset packs
- [var localizedAssetPacks: Set<AssetPack>](assetpackmanifest/localizedassetpacks.md)
  The subset of asset packs in this manifest that best match the current preferred languages.
- [func localizedAssetPacks(for: Locale.Language) -> Set<AssetPack>](assetpackmanifest/localizedassetpacks(for:).md)
  Returns the subset of asset packs in this manifest that are available to download and that best match the specified language.
### Inspecting asset pack localization
- [var primaryLanguage: Locale.Language?](assetpackmanifest/primarylanguage.md)
  The app’s primary language as configured in App Store Connect.
- [var availableLanguages: [Locale.Language]](assetpackmanifest/availablelanguages.md)
  The languages for which asset packs in this manifest are localized.
- [var resolvedLanguage: Locale.Language?](assetpackmanifest/resolvedlanguage.md)
  The language that best matches current preferences and for which a localized asset pack is available locally.
### Supporting types
- [AssetPackManifest.DecodingConfiguration](assetpackmanifest/decodingconfiguration.md)
  A structure that includes information for decoding an asset-pack manifest.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DecodableWithConfiguration](../Foundation/DecodableWithConfiguration.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AssetPack](assetpack.md)
  An archive of assets that the system downloads together.
- [actor AssetPackManager](assetpackmanager.md)
  An actor that manages asset packs.
- [protocol ManagedDownloaderExtension](manageddownloaderextension.md)
  An app extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAAppGroupID](../BundleResources/Information-Property-List/BAAppGroupID.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/Information-Property-List/BAHasManagedAssetPacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest)*
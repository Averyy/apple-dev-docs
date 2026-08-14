# AssetPack

**Framework**: Background Assets  
**Kind**: struct

An archive of assets that the system downloads together.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AssetPack
```

## Mentions

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)

#### Overview

An instance of this structure can be invalidated when the asset pack that it represents is updated on the server.

## Topics

### Identifying assets
- [let id: String](assetpack/id.md)
  A unique ID for the asset pack.
- [let version: Int](assetpack/version.md)
  The asset pack’s version number.
### Accessing asset details
- [AssetPack.Status](assetpack/status.md)
  The status of an asset pack.
- [let userInfo: Data?](assetpack/userinfo.md)
  JSON-encoded custom information that’s associated with the asset pack.
### Accessing asset language
- [let language: Locale.Language?](assetpack/language.md)
  The language for which this asset pack is localized.
- [Locale.Language](../foundation/locale/language-swift.struct.md)
  A type that represents a language, as used in a locale.
### Downloading assets
- [func download(for: BAContentRequest?) -> BADownload](assetpack/download(for:).md)
  Creates a download object for the asset pack that you schedule using a download manager.
- [let downloadSize: Int](assetpack/downloadsize.md)
  The size of the download file containing the asset pack in bytes.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [DecodableWithConfiguration](../foundation/decodablewithconfiguration.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [actor AssetPackManager](assetpackmanager.md)
  An actor that manages asset packs.
- [struct AssetPackManifest](assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [protocol ManagedDownloaderExtension](manageddownloaderextension.md)
  An app extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAAppGroupID](../bundleresources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../bundleresources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack)*
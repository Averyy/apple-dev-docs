# AssetPackManifest

**Framework**: Background Assets  
**Kind**: struct

A representation of a manifest that lists asset packs that are available to download.

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

#### Overview

This structure applies only when you want to manage your asset packs manually. Don’t use this structure if you want to opt in to automatic management of asset packs.

## Topics

### Creating an asset pack manifest
- [init(contentsOf: URL, appGroupID: String) throws](assetpackmanifest/init(contentsof:appgroupid:).md)
  Creates a representation of a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.
- [init(from: Data, appGroupID: String) throws](assetpackmanifest/init(from:appgroupid:).md)
  Creates a representation of a manifest in memory given JSON-encoded data.
### Accessing downloads
- [func allDownloads(for: BAContentRequest?) -> Set<BADownload>](assetpackmanifest/alldownloads(for:).md)
  Creates download objects for every applicable asset pack, which can be scheduled with the download manager.
### Getting asset packs
- [let assetPacks: Set<AssetPack>](assetpackmanifest/assetpacks.md)
  The asset packs that are available to download.
### Structures
- [AssetPackManifest.DecodingConfiguration](assetpackmanifest/decodingconfiguration.md)
  A structure that includes information for decoding an asset-pack manifest.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DecodableWithConfiguration](../Foundation/DecodableWithConfiguration.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest)*
# AssetPackManifest

**Framework**: Background Assets  
**Kind**: struct

A representation of a manifest that lists asset packs that are available to download.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AssetPackManifest
```

#### Overview

This structure applies only when you want to manage your asset packs manually. Don’t use this structure if you want to opt in to automatic management of asset packs.

## Topics

### Structures
- [AssetPackManifest.DecodingConfiguration](assetpackmanifest/decodingconfiguration.md)
  A configuration that informs how a manifest is decoded.
### Initializers
- [init(contentsOf: URL, appGroupID: String) throws](assetpackmanifest/init(contentsof:appgroupid:).md)
  Creates a representation of a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.
- [init(from: Data, appGroupID: String) throws](assetpackmanifest/init(from:appgroupid:).md)
  Creates a representation of a manifest in memory given JSON-encoded data.
### Instance Properties
- [let assetPacks: Set<AssetPack>](assetpackmanifest/assetpacks.md)
  The asset packs that are available to download.
### Instance Methods
- [func allDownloads(for: BAContentRequest?) -> Set<BADownload>](assetpackmanifest/alldownloads(for:).md)
  Creates download objects for every asset pack, which can be scheduled with the download manager.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DecodableWithConfiguration](../Foundation/DecodableWithConfiguration.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest)*
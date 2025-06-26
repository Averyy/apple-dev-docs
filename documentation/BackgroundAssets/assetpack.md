# AssetPack

**Framework**: Background Assets  
**Kind**: struct

An archive of assets that the system downloads together.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AssetPack
```

## Mentions

- [Downloading asset packs hosted by Apple](downloading-asset-packs-hosted-by-apple.md)

#### Overview

An instance of this structure can be invalidated when the asset pack that it represents is updated on the server.

## Topics

### Structures
- [AssetPack.Status](assetpack/status.md)
  The status of an asset pack.
### Instance Properties
- [let downloadSize: Int](assetpack/downloadsize.md)
  The size of the download file containing the asset pack in bytes.
- [let id: String](assetpack/id.md)
  A unique ID for the asset pack.
- [let userInfo: Data?](assetpack/userinfo.md)
  JSON-encoded custom information that’s associated with the asset pack.
- [let version: Int](assetpack/version.md)
  The asset pack’s version number
### Instance Methods
- [func download(for: BAContentRequest?) -> BADownload](assetpack/download(for:).md)
  Creates a download object for the asset pack that you schedule using a download manager.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DecodableWithConfiguration](../Foundation/DecodableWithConfiguration.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack)*
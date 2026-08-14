# CKAsset.ExportedAssetID

**Framework**: CloudKit  
**Kind**: struct

An identifier that can be used for creating a server-side copy of a [`CKAsset`](ckasset.md) that already exists in iCloud, potentially in a different container.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ExportedAssetID
```

#### Overview

An [`CKAsset.ExportedAssetID`](ckasset/exportedassetid.md) is valid only on the same device where it was created, and it expires after a few days.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckasset/exportedassetid)*
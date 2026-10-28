# CKAsset.ExportedAssetID

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

An identifier that can be used for creating a server-side copy of a [`CKAsset`](../ckasset.md) that already exists in iCloud, potentially in a different container.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ExportedAssetID
```

## Overview

An [`CKAsset.ExportedAssetID`](./exportedassetid.md) is valid only on the same device where it was created, and it expires after a few days.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckasset/exportedassetid)*
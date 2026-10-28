# PHAssetExtendedMetadata

**Framework**: Photos  
**Kind**: class  
**Role**: Class

Represents other asset attributes that are not included when fetching `PHAsset` directly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class PHAssetExtendedMetadata
```

```objc
@interface PHAssetExtendedMetadata : NSObject
```

## Overview

When [`extendedMetadata`](./phasset/extendedmetadata.md) is called, these properties are fetched. They can be prefetched by toggling [`prefetchAssetExtendedMetadata`](./phfetchoptions/prefetchassetextendedmetadata.md) when fetching [`PHAsset`](./phasset.md).

## Topics

### Reading metadata
- [var caption: String?](./phassetextendedmetadata/caption.md)
  The compact description for this asset.
- [var keywords: [String]](./phassetextendedmetadata/keywords.md)
  The keywords associated with this asset
### Instance Properties
- [var originalFilename: String?](./phassetextendedmetadata/originalfilename.md)
  The original file name of this asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetextendedmetadata)*
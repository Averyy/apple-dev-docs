# MediaIntelligenceImageAsset.Kind

**Framework**: Media Intelligence  
**Kind**: enum  
**Role**: Enumeration

A value that describes the source of an image asset’s data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Kind
```

## Mentions

- [Detecting and grouping faces in images](../detecting-and-grouping-faces-in-images.md)

## Overview

[`MediaIntelligenceImageAsset.Kind`](./kind-swift.enum.md) describes how the framework reads an image.

## Topics

### Kinds
- [MediaIntelligenceImageAsset.Kind.url(_:)](./kind-swift.enum/url%28_%29.md)
  An image located at the specified URL.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an asset
- [init(id: MediaIntelligenceImageAsset.ID, kind: MediaIntelligenceImageAsset.Kind)](./init%28id,kind%29.md)
  Creates an image asset with the specified identifier and kind.
- [MediaIntelligenceImageAsset.ID](./id-swift.struct.md)
  A unique identifier for an image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceimageasset/kind-swift.enum)*
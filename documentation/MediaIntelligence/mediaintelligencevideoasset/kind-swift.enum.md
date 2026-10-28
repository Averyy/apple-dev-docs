# MediaIntelligenceVideoAsset.Kind

**Framework**: Media Intelligence  
**Kind**: enum  
**Role**: Enumeration

A value that describes the source of a video asset’s data.

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

- [Finding the best moments in a video](../finding-the-best-moments-in-a-video.md)

## Overview

[`MediaIntelligenceVideoAsset.Kind`](./kind-swift.enum.md) describes how the framework reads a video.

## Topics

### Kinds
- [MediaIntelligenceVideoAsset.Kind.url(_:)](./kind-swift.enum/url%28_%29.md)
  A video located at the specified URL.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an asset
- [init(id: MediaIntelligenceVideoAsset.ID, kind: MediaIntelligenceVideoAsset.Kind)](./init%28id,kind%29.md)
  Creates a video asset with the specified identifier and kind.
- [MediaIntelligenceVideoAsset.ID](./id-swift.struct.md)
  A unique identifier for a video asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligencevideoasset/kind-swift.enum)*
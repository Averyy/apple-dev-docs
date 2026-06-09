# MediaIntelligenceVideoAsset

**Framework**: Media Intelligence  
**Kind**: struct

A video asset to analyze.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MediaIntelligenceVideoAsset
```

## Mentions

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)

#### Overview

Create an instance of this type to identify a video for [`VideoAnalyzer`](videoanalyzer.md) to process. Each asset has a unique identifier you assign, and a [`MediaIntelligenceVideoAsset.Kind`](mediaintelligencevideoasset/kind-swift.enum.md) value that describes how the framework accesses the video data.

## Topics

### Creating an asset
- [init(id: MediaIntelligenceVideoAsset.ID, kind: MediaIntelligenceVideoAsset.Kind)](mediaintelligencevideoasset/init(id:kind:).md)
  Creates a video asset with the specified identifier and kind.
- [MediaIntelligenceVideoAsset.ID](mediaintelligencevideoasset/id-swift.struct.md)
  A unique identifier for a video asset.
- [MediaIntelligenceVideoAsset.Kind](mediaintelligencevideoasset/kind-swift.enum.md)
  A value that describes the source of a video asset’s data.
### Inspecting an asset
- [let id: MediaIntelligenceVideoAsset.ID](mediaintelligencevideoasset/id-swift.property.md)
  A unique identifier for the asset.
- [let kind: MediaIntelligenceVideoAsset.Kind](mediaintelligencevideoasset/kind-swift.property.md)
  A value that describes how the framework accesses the video data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)
  Identify keyframes and highlight segments using on-device analysis.
- [class VideoAnalyzer](videoanalyzer.md)
  An object that analyzes video assets for highlights and key frames.
- [class HighlightAnalysisRequest](highlightanalysisrequest.md)
  A request that identifies the most engaging segments of a video.
- [class KeyFrameAnalysisRequest](keyframeanalysisrequest.md)
  A request that identifies the best representative frame of a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligencevideoasset)*
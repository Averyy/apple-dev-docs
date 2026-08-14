# MediaIntelligenceImageAsset

**Framework**: Media Intelligence  
**Kind**: struct

An image asset to analyze.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MediaIntelligenceImageAsset
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Overview

Create a [`MediaIntelligenceImageAsset`](mediaintelligenceimageasset.md) to identify an image you want [`FaceGroupAnalyzer`](facegroupanalyzer.md) to process. Each asset has a unique identifier you assign, and a [`MediaIntelligenceImageAsset.Kind`](mediaintelligenceimageasset/kind-swift.enum.md) value that describes how the framework accesses the image data.

Use the same [`MediaIntelligenceImageAsset.ID`](mediaintelligenceimageasset/id-swift.struct.md) value consistently for a specified image. The framework uses this identifier to match new submissions against existing data, so changing the identifier causes the framework to treat the image as a new asset.

## Topics

### Creating an asset
- [init(id: MediaIntelligenceImageAsset.ID, kind: MediaIntelligenceImageAsset.Kind)](mediaintelligenceimageasset/init(id:kind:).md)
  Creates an image asset with the specified identifier and kind.
- [MediaIntelligenceImageAsset.ID](mediaintelligenceimageasset/id-swift.struct.md)
  A unique identifier for an image asset.
- [MediaIntelligenceImageAsset.Kind](mediaintelligenceimageasset/kind-swift.enum.md)
  A value that describes the source of an image asset’s data.
### Inspecting an asset
- [let id: MediaIntelligenceImageAsset.ID](mediaintelligenceimageasset/id-swift.property.md)
  A unique identifier for the asset.
- [let kind: MediaIntelligenceImageAsset.Kind](mediaintelligenceimageasset/kind-swift.property.md)
  A value that describes how the framework accesses the image data.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)
  Organize photos by person using on-device face detection.
- [class FaceGroupAnalyzer](facegroupanalyzer.md)
  An object that detects faces in images and groups them by person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceimageasset)*
# identifyFaces(in:)

**Framework**: Media Intelligence  
**Kind**: method  
**Role**: Instance Method

Detects and identifies faces without modifying the analyzer’s data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final nonisolated(nonsending) func identifyFaces(in assets: [MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
```

## Mentions

- [Detecting and grouping faces in images](../detecting-and-grouping-faces-in-images.md)

#### Return Value

An async sequence of `(assetID, faces)` pairs.

#### Discussion

Use this method to recognize people in new images against the existing gallery without storing any face data. Each returned face has an [`entityID`](./face/entityid.md) if the framework matched it to a known entity, or `nil` if no match was found.

## Parameters

- `assets`: The image assets to analyze.

## See Also

### Fetching and identifying faces
- [func fetchFaces([FaceGroupAnalyzer.Face.ID]) throws -> some AsyncSequence<FaceGroupAnalyzer.Face, any Error>
](./fetchfaces%28_%29.md)
  Returns the faces with the specified identifiers.
- [func fetchFaces(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](./fetchfaces%28for%29.md)
  Returns the faces belonging to the specified entities.
- [func fetchFaces(in: [MediaIntelligenceImageAsset.ID]) throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](./fetchfaces%28in%29.md)
  Returns the faces from the specified assets.
- [func fetchAssetIDs(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>
](./fetchassetids%28for%29.md)
  Returns the asset identifiers for the specified entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/identifyfaces(in:))*
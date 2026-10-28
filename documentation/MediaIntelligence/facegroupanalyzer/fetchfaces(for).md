# fetchFaces(for:)

**Framework**: Media Intelligence  
**Kind**: method  
**Role**: Instance Method

Returns the faces belonging to the specified entities.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func fetchFaces(for entityIDs: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
```

## Mentions

- [Detecting and grouping faces in images](../detecting-and-grouping-faces-in-images.md)

## Return Value

An async sequence of `(entityID, faces)` pairs.

## Parameters

- `entityIDs`: The entity identifiers to look up.

## See Also

### Fetching and identifying faces
- [func fetchFaces([FaceGroupAnalyzer.Face.ID]) throws -> some AsyncSequence<FaceGroupAnalyzer.Face, any Error>
](./fetchfaces%28_%29.md)
  Returns the faces with the specified identifiers.
- [func fetchFaces(in: [MediaIntelligenceImageAsset.ID]) throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](./fetchfaces%28in%29.md)
  Returns the faces from the specified assets.
- [func fetchAssetIDs(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>
](./fetchassetids%28for%29.md)
  Returns the asset identifiers for the specified entities.
- [func identifyFaces(in: [MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](./identifyfaces%28in%29.md)
  Detects and identifies faces without modifying the analyzer’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/fetchfaces(for:))*
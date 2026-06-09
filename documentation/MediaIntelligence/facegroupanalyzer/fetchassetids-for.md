# fetchAssetIDs(for:)

**Framework**: Media Intelligence  
**Kind**: method

Returns the asset identifiers for the specified entities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func fetchAssetIDs(for entityIDs: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Return Value

An async sequence of `(entityID, assetIDs)` pairs.

## Parameters

- `entityIDs`: The entity identifiers to look up.

## See Also

- [func fetchFaces([FaceGroupAnalyzer.Face.ID]) throws -> some AsyncSequence<FaceGroupAnalyzer.Face, any Error>
](facegroupanalyzer/fetchfaces(_:).md)
  Returns the faces with the specified identifiers.
- [func fetchFaces(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/fetchfaces(for:).md)
  Returns the faces belonging to the specified entities.
- [func fetchFaces(in: [MediaIntelligenceImageAsset.ID]) throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/fetchfaces(in:).md)
  Returns the faces from the specified assets.
- [func identifyFaces(in: [MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/identifyfaces(in:).md)
  Detects and identifies faces without modifying the analyzer’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/fetchassetids(for:))*
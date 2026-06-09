# fetchFaces(in:)

**Framework**: Media Intelligence  
**Kind**: method

Returns the faces from the specified assets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func fetchFaces(in assetIDs: [MediaIntelligenceImageAsset.ID]) throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
```

#### Return Value

An async sequence of `(assetID, faces)` pairs.

## Parameters

- `assetIDs`: The asset identifiers to look up.

## See Also

- [func fetchFaces([FaceGroupAnalyzer.Face.ID]) throws -> some AsyncSequence<FaceGroupAnalyzer.Face, any Error>
](facegroupanalyzer/fetchfaces(_:).md)
  Returns the faces with the specified identifiers.
- [func fetchFaces(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/fetchfaces(for:).md)
  Returns the faces belonging to the specified entities.
- [func fetchAssetIDs(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>
](facegroupanalyzer/fetchassetids(for:).md)
  Returns the asset identifiers for the specified entities.
- [func identifyFaces(in: [MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/identifyfaces(in:).md)
  Detects and identifies faces without modifying the analyzer’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/fetchfaces(in:))*
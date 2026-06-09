# allFacesByEntityID

**Framework**: Media Intelligence  
**Kind**: property

An async sequence of all faces, grouped by entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var allFacesByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error> { get }
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

## See Also

- [var allFaces: some AsyncSequence<FaceGroupAnalyzer.Face, any Error>](facegroupanalyzer/allfaces.md)
  An async sequence of all faces in the analyzer.
- [var allEntities: some AsyncSequence<FaceGroupAnalyzer.Entity, any Error>](facegroupanalyzer/allentities.md)
  An async sequence of all entities in the analyzer.
- [var allAssetIDs: some AsyncSequence<MediaIntelligenceImageAsset.ID, any Error>](facegroupanalyzer/allassetids.md)
  An async sequence of all asset identifiers in the analyzer.
- [var allAssetIDsByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>](facegroupanalyzer/allassetidsbyentityid.md)
  An async sequence of all asset identifiers, grouped by entity.
- [FaceGroupAnalyzer.Face](facegroupanalyzer/face.md)
  A face detected in an image asset.
- [FaceGroupAnalyzer.Entity](facegroupanalyzer/entity.md)
  A cluster of faces that belong to the same person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/allfacesbyentityid)*
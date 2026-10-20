# allFacesByEntityID

**Framework**: Media Intelligence  
**Kind**: property  
**Role**: Instance Property

An async sequence of all faces, grouped by entity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var allFacesByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error> { get }
```

## Mentions

- [Detecting and grouping faces in images](../detecting-and-grouping-faces-in-images.md)

## See Also

### Retrieving faces and entities
- [var allFaces: some AsyncSequence<FaceGroupAnalyzer.Face, any Error>](./allfaces.md)
  An async sequence of all faces in the analyzer.
- [var allEntities: some AsyncSequence<FaceGroupAnalyzer.Entity, any Error>](./allentities.md)
  An async sequence of all entities in the analyzer.
- [var allAssetIDs: some AsyncSequence<MediaIntelligenceImageAsset.ID, any Error>](./allassetids.md)
  An async sequence of all asset identifiers in the analyzer.
- [var allAssetIDsByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>](./allassetidsbyentityid.md)
  An async sequence of all asset identifiers, grouped by entity.
- [FaceGroupAnalyzer.Face](./face.md)
  A face detected in an image asset.
- [FaceGroupAnalyzer.Entity](./entity.md)
  A cluster of faces that belong to the same person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/allfacesbyentityid)*
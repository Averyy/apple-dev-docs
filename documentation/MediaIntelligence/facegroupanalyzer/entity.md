# FaceGroupAnalyzer.Entity

**Framework**: Media Intelligence  
**Kind**: struct  
**Role**: Structure

A cluster of faces that belong to the same person.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Entity
```

#### Overview

This type represents a distinct person as identified by the framework’s clustering algorithm. After you call [`update(subprogress:)`](./update%28subprogress%29.md), each detected face receives a [`entityID`](./face/entityid.md) that associates it with an entity.

Use [`fetchFaces(for:)`](./fetchfaces%28for%29.md) to retrieve all faces that belong to a particular entity, or [`fetchAssetIDs(for:)`](./fetchassetids%28for%29.md) to find the images in which a person appears.

## Topics

### Identifying an entity
- [let id: FaceGroupAnalyzer.Entity.ID](./entity/id-swift.property.md)
  A unique identifier for the entity.
- [FaceGroupAnalyzer.Entity.ID](./entity/id-swift.struct.md)
  A type that uniquely identifies an entity.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving faces and entities
- [var allFaces: some AsyncSequence<FaceGroupAnalyzer.Face, any Error>](./allfaces.md)
  An async sequence of all faces in the analyzer.
- [var allFacesByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>](./allfacesbyentityid.md)
  An async sequence of all faces, grouped by entity.
- [var allEntities: some AsyncSequence<FaceGroupAnalyzer.Entity, any Error>](./allentities.md)
  An async sequence of all entities in the analyzer.
- [var allAssetIDs: some AsyncSequence<MediaIntelligenceImageAsset.ID, any Error>](./allassetids.md)
  An async sequence of all asset identifiers in the analyzer.
- [var allAssetIDsByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>](./allassetidsbyentityid.md)
  An async sequence of all asset identifiers, grouped by entity.
- [FaceGroupAnalyzer.Face](./face.md)
  A face detected in an image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/entity)*
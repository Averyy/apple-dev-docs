# FaceGroupAnalyzer.Entity

**Framework**: Media Intelligence  
**Kind**: struct

A cluster of faces that belong to the same person.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Entity
```

#### Overview

This type represents a distinct person as identified by the framework’s clustering algorithm. After you call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md), each detected face receives a [`entityID`](facegroupanalyzer/face/entityid.md) that associates it with an entity.

Use [`fetchFaces(for:)`](facegroupanalyzer/fetchfaces(for:).md) to retrieve all faces that belong to a particular entity, or [`fetchAssetIDs(for:)`](facegroupanalyzer/fetchassetids(for:).md) to find the images in which a person appears.

## Topics

### Identifying an entity
- [let id: FaceGroupAnalyzer.Entity.ID](facegroupanalyzer/entity/id-swift.property.md)
  A unique identifier for the entity.
- [FaceGroupAnalyzer.Entity.ID](facegroupanalyzer/entity/id-swift.struct.md)
  A type that uniquely identifies an entity.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var allFaces: some AsyncSequence<FaceGroupAnalyzer.Face, any Error>](facegroupanalyzer/allfaces.md)
  An async sequence of all faces in the analyzer.
- [var allFacesByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>](facegroupanalyzer/allfacesbyentityid.md)
  An async sequence of all faces, grouped by entity.
- [var allEntities: some AsyncSequence<FaceGroupAnalyzer.Entity, any Error>](facegroupanalyzer/allentities.md)
  An async sequence of all entities in the analyzer.
- [var allAssetIDs: some AsyncSequence<MediaIntelligenceImageAsset.ID, any Error>](facegroupanalyzer/allassetids.md)
  An async sequence of all asset identifiers in the analyzer.
- [var allAssetIDsByEntityID: some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>](facegroupanalyzer/allassetidsbyentityid.md)
  An async sequence of all asset identifiers, grouped by entity.
- [FaceGroupAnalyzer.Face](facegroupanalyzer/face.md)
  A face detected in an image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/entity)*
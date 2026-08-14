# FaceGroupAnalyzer.Face

**Framework**: Media Intelligence  
**Kind**: struct

A face detected in an image asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Face
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Overview

This type represents a single face that [`FaceGroupAnalyzer`](facegroupanalyzer.md) detects in an image. It records the face’s location within the image, the identifier of the image it came from, and after [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) runs, the entity the face belongs to.

The [`bounds`](facegroupanalyzer/face/bounds.md) rectangle uses normalized coordinates in the range `0.0` to `1.0` along both axes, with the origin at the top-left corner of the image.

## Topics

### Identifying a face
- [let id: FaceGroupAnalyzer.Face.ID](facegroupanalyzer/face/id-swift.property.md)
  A unique identifier for the face.
- [let entityID: FaceGroupAnalyzer.Entity.ID?](facegroupanalyzer/face/entityid.md)
  An identifier for the entity this face belongs to.
- [let assetID: MediaIntelligenceImageAsset.ID](facegroupanalyzer/face/assetid.md)
  An identifier for the image asset that contains this face.
- [FaceGroupAnalyzer.Face.ID](facegroupanalyzer/face/id-swift.struct.md)
  A unique identifier for a detected face.
### Locating a face
- [let bounds: CGRect](facegroupanalyzer/face/bounds.md)
  A normalized rectangle describing the location of the face within its source image.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
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
- [FaceGroupAnalyzer.Entity](facegroupanalyzer/entity.md)
  A cluster of faces that belong to the same person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/face)*
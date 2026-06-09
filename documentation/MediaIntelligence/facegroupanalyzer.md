# FaceGroupAnalyzer

**Framework**: Media Intelligence  
**Kind**: class

An object that detects faces in images and groups them by person.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class FaceGroupAnalyzer
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Overview

[`FaceGroupAnalyzer`](facegroupanalyzer.md) is the central object in the face analysis pipeline. It detects faces in images, stores their data persistently in a working directory you choose, and clusters the faces into groups called *entities*, where each entity represents a distinct person.

The analyzer stores all face data and cluster assignments in the directory you pass to [`init(workingDirectory:)`](facegroupanalyzer/init(workingdirectory:).md). This directory persists between app launches, so subsequent runs resume from where the previous session ended. Call [`purge(workingDirectory:)`](facegroupanalyzer/purge(workingdirectory:).md) to remove all data from the directory.

Use [`identifyFaces(in:)`](facegroupanalyzer/identifyfaces(in:).md) to detect and match faces in images without storing anything. This is useful for recognizing people in new images against an existing gallery without modifying the analyzer’s data.

## Topics

### Creating an analyzer
- [init(workingDirectory: URL) throws](facegroupanalyzer/init(workingdirectory:).md)
  Creates a face group analyzer at the specified directory.
### Managing assets
- [let workingDirectory: URL](facegroupanalyzer/workingdirectory.md)
  A directory where the analyzer stores its face data and metadata.
- [func insertOrUpdateAssets([MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/insertorupdateassets(_:).md)
  Adds or replaces image assets in the analyzer.
- [func deleteAssets([MediaIntelligenceImageAsset.ID]) async throws](facegroupanalyzer/deleteassets(_:).md)
  Removes the specified assets and their associated face data.
- [func deleteAllAssets() async throws](facegroupanalyzer/deleteallassets.md)
  Removes all assets and their associated face data from the analyzer.
- [static func purge(workingDirectory: URL) async throws](facegroupanalyzer/purge(workingdirectory:).md)
  Removes all analyzer data from the specified directory.
### Updating the gallery
- [var state: FaceGroupAnalyzer.State](facegroupanalyzer/state-swift.property.md)
  A value describing the current processing state of the analyzer.
- [FaceGroupAnalyzer.State](facegroupanalyzer/state-swift.enum.md)
  The current processing state of a face group analyzer.
- [func update(subprogress: consuming Subprogress?) async throws](facegroupanalyzer/update(subprogress:).md)
  Clusters faces into entities and updates their assignments.
### Retrieving faces and entities
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
- [FaceGroupAnalyzer.Entity](facegroupanalyzer/entity.md)
  A cluster of faces that belong to the same person.
### Fetching and identifying faces
- [func fetchFaces([FaceGroupAnalyzer.Face.ID]) throws -> some AsyncSequence<FaceGroupAnalyzer.Face, any Error>
](facegroupanalyzer/fetchfaces(_:).md)
  Returns the faces with the specified identifiers.
- [func fetchFaces(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/fetchfaces(for:).md)
  Returns the faces belonging to the specified entities.
- [func fetchFaces(in: [MediaIntelligenceImageAsset.ID]) throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/fetchfaces(in:).md)
  Returns the faces from the specified assets.
- [func fetchAssetIDs(for: [FaceGroupAnalyzer.Entity.ID]) throws -> some AsyncSequence<(entityID: FaceGroupAnalyzer.Entity.ID, assetIDs: Array<MediaIntelligenceImageAsset.ID>), any Error>
](facegroupanalyzer/fetchassetids(for:).md)
  Returns the asset identifiers for the specified entities.
- [func identifyFaces(in: [MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/identifyfaces(in:).md)
  Detects and identifies faces without modifying the analyzer’s data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)
  Organize photos by person using on-device face detection.
- [struct MediaIntelligenceImageAsset](mediaintelligenceimageasset.md)
  An image asset to analyze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer)*
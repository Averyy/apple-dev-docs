# insertOrUpdateAssets(_:)

**Framework**: Media Intelligence  
**Kind**: method

Adds or replaces image assets in the analyzer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final nonisolated(nonsending) func insertOrUpdateAssets(_ assets: [MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Return Value

An async sequence of `(assetID, faces)` pairs — one per asset — reporting the faces detected in each image.

#### Discussion

For each asset, the method detects faces and extracts facial data, then persists the results to the working directory. If an asset with the same identifier already exists, the method replaces its face data.

After this call, [`state`](facegroupanalyzer/state-swift.property.md) becomes [`FaceGroupAnalyzer.State.stale`](facegroupanalyzer/state-swift.enum/stale.md) until you call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md). Faces detected in this call have a `nil` [`entityID`](facegroupanalyzer/face/entityid.md) until clustering runs.

## Parameters

- `assets`: The image assets to ingest.

## See Also

- [let workingDirectory: URL](facegroupanalyzer/workingdirectory.md)
  A directory where the analyzer stores its face data and metadata.
- [func deleteAssets([MediaIntelligenceImageAsset.ID]) async throws](facegroupanalyzer/deleteassets(_:).md)
  Removes the specified assets and their associated face data.
- [func deleteAllAssets() async throws](facegroupanalyzer/deleteallassets.md)
  Removes all assets and their associated face data from the analyzer.
- [static func purge(workingDirectory: URL) async throws](facegroupanalyzer/purge(workingdirectory:).md)
  Removes all analyzer data from the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/insertorupdateassets(_:))*
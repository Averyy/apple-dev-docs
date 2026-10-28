# purge(workingDirectory:)

**Framework**: Media Intelligence  
**Kind**: method  
**Role**: Type Method

Removes all analyzer data from the specified directory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated(nonsending)
static func purge(workingDirectory: URL) async throws
```

## Mentions

- [Detecting and grouping faces in images](../detecting-and-grouping-faces-in-images.md)

## Discussion

Call this method to permanently delete all face data, cluster assignments, and metadata from `workingDirectory`. This operation is irreversible.

## Parameters

- `workingDirectory`: The directory to purge.

## See Also

### Managing assets
- [let workingDirectory: URL](./workingdirectory.md)
  A directory where the analyzer stores its face data and metadata.
- [func insertOrUpdateAssets([MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](./insertorupdateassets%28_%29.md)
  Adds or replaces image assets in the analyzer.
- [func deleteAssets([MediaIntelligenceImageAsset.ID]) async throws](./deleteassets%28_%29.md)
  Removes the specified assets and their associated face data.
- [func deleteAllAssets() async throws](./deleteallassets%28%29.md)
  Removes all assets and their associated face data from the analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/purge(workingdirectory:))*
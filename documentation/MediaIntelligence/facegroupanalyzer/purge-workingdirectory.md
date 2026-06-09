# purge(workingDirectory:)

**Framework**: Media Intelligence  
**Kind**: method

Removes all analyzer data from the specified directory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) static func purge(workingDirectory: URL) async throws
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Discussion

Call this method to permanently delete all face data, cluster assignments, and metadata from `workingDirectory`. This operation is irreversible.

## Parameters

- `workingDirectory`: The directory to purge.

## See Also

- [let workingDirectory: URL](facegroupanalyzer/workingdirectory.md)
  A directory where the analyzer stores its face data and metadata.
- [func insertOrUpdateAssets([MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/insertorupdateassets(_:).md)
  Adds or replaces image assets in the analyzer.
- [func deleteAssets([MediaIntelligenceImageAsset.ID]) async throws](facegroupanalyzer/deleteassets(_:).md)
  Removes the specified assets and their associated face data.
- [func deleteAllAssets() async throws](facegroupanalyzer/deleteallassets.md)
  Removes all assets and their associated face data from the analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/purge(workingdirectory:))*
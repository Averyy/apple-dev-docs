# deleteAllAssets()

**Framework**: Media Intelligence  
**Kind**: method

Removes all assets and their associated face data from the analyzer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final nonisolated(nonsending) func deleteAllAssets() async throws
```

## See Also

- [let workingDirectory: URL](facegroupanalyzer/workingdirectory.md)
  A directory where the analyzer stores its face data and metadata.
- [func insertOrUpdateAssets([MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](facegroupanalyzer/insertorupdateassets(_:).md)
  Adds or replaces image assets in the analyzer.
- [func deleteAssets([MediaIntelligenceImageAsset.ID]) async throws](facegroupanalyzer/deleteassets(_:).md)
  Removes the specified assets and their associated face data.
- [static func purge(workingDirectory: URL) async throws](facegroupanalyzer/purge(workingdirectory:).md)
  Removes all analyzer data from the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/deleteallassets())*
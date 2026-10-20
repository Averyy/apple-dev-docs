# workingDirectory

**Framework**: Media Intelligence  
**Kind**: property  
**Role**: Instance Property

A directory where the analyzer stores its face data and metadata.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final let workingDirectory: URL
```

## See Also

### Managing assets
- [func insertOrUpdateAssets([MediaIntelligenceImageAsset]) async throws -> some AsyncSequence<(assetID: MediaIntelligenceImageAsset.ID, faces: Array<FaceGroupAnalyzer.Face>), any Error>
](./insertorupdateassets%28_%29.md)
  Adds or replaces image assets in the analyzer.
- [func deleteAssets([MediaIntelligenceImageAsset.ID]) async throws](./deleteassets%28_%29.md)
  Removes the specified assets and their associated face data.
- [func deleteAllAssets() async throws](./deleteallassets%28%29.md)
  Removes all assets and their associated face data from the analyzer.
- [static func purge(workingDirectory: URL) async throws](./purge%28workingdirectory%29.md)
  Removes all analyzer data from the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/workingdirectory)*
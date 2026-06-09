# MediaIntelligenceError.faceGroupProcessing

**Framework**: Media Intelligence  
**Kind**: case

The framework can’t complete a face grouping operation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case faceGroupProcessing
```

#### Discussion

This error occurs when the framework fails to detect faces, insert or delete face data, or update face cluster assignments. If this error occurs during [`insertOrUpdateAssets(_:)`](facegroupanalyzer/insertorupdateassets(_:).md) or [`deleteAssets(_:)`](facegroupanalyzer/deleteassets(_:).md), the framework automatically rolls back any partial changes.

## See Also

- [MediaIntelligenceError.mediaProcessing](mediaintelligenceerror/mediaprocessing.md)
  The framework can’t process a media asset.
- [MediaIntelligenceError.resultFetching](mediaintelligenceerror/resultfetching.md)
  The framework can’t retrieve analysis results.
- [MediaIntelligenceError.workingDirectory](mediaintelligenceerror/workingdirectory.md)
  The framework can’t access the working directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceerror/facegroupprocessing)*
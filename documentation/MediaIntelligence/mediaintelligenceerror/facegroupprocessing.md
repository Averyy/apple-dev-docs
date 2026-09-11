# MediaIntelligenceError.faceGroupProcessing

**Framework**: Media Intelligence  
**Kind**: case

The framework can’t complete a face grouping operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
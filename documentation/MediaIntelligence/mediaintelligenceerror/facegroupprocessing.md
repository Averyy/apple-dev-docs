# MediaIntelligenceError.faceGroupProcessing

**Framework**: Media Intelligence  
**Kind**: case  
**Role**: Case

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

## Discussion

This error occurs when the framework fails to detect faces, insert or delete face data, or update face cluster assignments. If this error occurs during [`insertOrUpdateAssets(_:)`](../facegroupanalyzer/insertorupdateassets%28_%29.md) or [`deleteAssets(_:)`](../facegroupanalyzer/deleteassets%28_%29.md), the framework automatically rolls back any partial changes.

## See Also

### Errors
- [MediaIntelligenceError.mediaProcessing](./mediaprocessing.md)
  The framework can’t process a media asset.
- [MediaIntelligenceError.resultFetching](./resultfetching.md)
  The framework can’t retrieve analysis results.
- [MediaIntelligenceError.workingDirectory](./workingdirectory.md)
  The framework can’t access the working directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceerror/facegroupprocessing)*
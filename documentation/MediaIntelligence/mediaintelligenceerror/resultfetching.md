# MediaIntelligenceError.resultFetching

**Framework**: Media Intelligence  
**Kind**: case

The framework can’t retrieve analysis results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case resultFetching
```

#### Discussion

This error occurs when the framework can’t find a result that matches the type expected by a [`VideoAnalyzer.Request`](videoanalyzer/request.md). Confirm that you’re passing the correct request type to [`analyze(_:for:)`](videoanalyzer/analyze(_:for:).md).

## See Also

- [MediaIntelligenceError.faceGroupProcessing](mediaintelligenceerror/facegroupprocessing.md)
  The framework can’t complete a face grouping operation.
- [MediaIntelligenceError.mediaProcessing](mediaintelligenceerror/mediaprocessing.md)
  The framework can’t process a media asset.
- [MediaIntelligenceError.workingDirectory](mediaintelligenceerror/workingdirectory.md)
  The framework can’t access the working directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceerror/resultfetching)*
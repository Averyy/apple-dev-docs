# MediaIntelligenceError.workingDirectory

**Framework**: Media Intelligence  
**Kind**: case

The framework can’t access the working directory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case workingDirectory
```

#### Discussion

This error occurs when the working directory you provide to [`init(workingDirectory:)`](facegroupanalyzer/init(workingdirectory:).md) or [`purge(workingDirectory:)`](facegroupanalyzer/purge(workingdirectory:).md) doesn’t exist or isn’t accessible. Verify that the URL points to a valid, writable directory before creating an analyzer.

## See Also

- [MediaIntelligenceError.faceGroupProcessing](mediaintelligenceerror/facegroupprocessing.md)
  The framework can’t complete a face grouping operation.
- [MediaIntelligenceError.mediaProcessing](mediaintelligenceerror/mediaprocessing.md)
  The framework can’t process a media asset.
- [MediaIntelligenceError.resultFetching](mediaintelligenceerror/resultfetching.md)
  The framework can’t retrieve analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceerror/workingdirectory)*
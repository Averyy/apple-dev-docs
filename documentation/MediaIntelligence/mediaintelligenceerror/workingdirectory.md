# MediaIntelligenceError.workingDirectory

**Framework**: Media Intelligence  
**Kind**: case  
**Role**: Case

The framework can’t access the working directory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case workingDirectory
```

## Discussion

This error occurs when the working directory you provide to [`init(workingDirectory:)`](../facegroupanalyzer/init%28workingdirectory%29.md) or [`purge(workingDirectory:)`](../facegroupanalyzer/purge%28workingdirectory%29.md) doesn’t exist or isn’t accessible. Verify that the URL points to a valid, writable directory before creating an analyzer.

## See Also

### Errors
- [MediaIntelligenceError.faceGroupProcessing](./facegroupprocessing.md)
  The framework can’t complete a face grouping operation.
- [MediaIntelligenceError.mediaProcessing](./mediaprocessing.md)
  The framework can’t process a media asset.
- [MediaIntelligenceError.resultFetching](./resultfetching.md)
  The framework can’t retrieve analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceerror/workingdirectory)*
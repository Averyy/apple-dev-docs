# videoAnalysis(forFileAt:)

**Framework**: Sensitive Content Analysis  
**Kind**: method

Analyzes a video file on disk at a URL for sensitive content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 2.0+

## Declaration

```swift
func videoAnalysis(forFileAt fileURL: URL) -> SCSensitivityAnalyzer.VideoAnalysisHandler
```

#### Return Value

An object that checks if a video contains sensitive content and provides the app with status updates as the analysis progresses.

## Parameters

- `fileURL`: The URL for a video file on disk.

## See Also

- [SCSensitivityAnalyzer.VideoAnalysisHandler](scsensitivityanalyzer/videoanalysishandler.md)
  An object that checks if a video contains sensitive content and provides status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer/videoanalysis(forfileat:))*
# SCVideoStreamAnalysisChangeHandler

**Framework**: Sensitive Content Analysis  
**Kind**: typealias  
**Role**: Type Alias

A handler your app provides to receive video-stream analysis results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```c
typedef void (^)(SCSensitivityAnalysis *, NSError *) SCVideoStreamAnalysisChangeHandler;
```

#### Discussion

Your app implements this handler and the framework calls it when the analyzer’s video stream detects sensitive content, or when the analyzer encounters an error providing analysis or an error in input parameters.

This handler receives an instance of [`SCSensitivityAnalysis`](./scsensitivityanalysis.md), and an [`Error`](../Swift/error.md), as in the following example:

```swift
analyzer.analysisChangedHandler = { analysis, error in
    self.analysis = analysis
    if analysis.shouldInterruptVideo {
        // ...
    }
    if analysis.shouldIndicateSensitivity {
        // ...
    }
    if analysis.shouldMuteAudio {
        // ...
    }
}
```

## See Also

### Responding to sensitive content
- [var analysis: SCSensitivityAnalysis?](./scvideostreamanalyzer/analysis.md)
  The results of the first detected sensitive video frame.
- [analysisChangedHandler](./scvideostreamanalyzer/analysischangedhandler.md)
  A handler that your app provides to react to sensitive content detection.
- [func continueStream()](./scvideostreamanalyzer/continuestream%28%29.md)
  Indicates that your app is ready to resume video stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalysischangehandler)*
# continueStream()

**Framework**: Sensitive Content Analysis  
**Kind**: method  
**Role**: Instance Method

Indicates that your app is ready to resume video stream analysis.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func continueStream()
```

```objc
- (void) continueStream;
```

## Discussion

When the framework detects sensitive content in the video stream, it pauses analysis and begins censoring the stream’s video frames. Call this method to resume analysis and stop censoring video frames when your app is ready to show the stream again.

## See Also

### Responding to sensitive content
- [var analysis: SCSensitivityAnalysis?](./analysis.md)
  The results of the first detected sensitive video frame.
- [analysisChangedHandler](./analysischangedhandler.md)
  A handler that your app provides to react to sensitive content detection.
- [SCVideoStreamAnalysisChangeHandler](../scvideostreamanalysischangehandler.md)
  A handler your app provides to receive video-stream analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/continuestream())*
# analysisChangedHandler

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Instance Property

A handler that your app provides to react to sensitive content detection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```objc
@property (copy, readwrite, nullable) SCVideoStreamAnalysisChangeHandler analysisChangedHandler;
```

#### Discussion

The system invokes all analyzer handlers on the same conference call with the updated analysis or error.

## See Also

### Responding to sensitive content
- [var analysis: SCSensitivityAnalysis?](./analysis.md)
  The results of the first detected sensitive video frame.
- [SCVideoStreamAnalysisChangeHandler](../scvideostreamanalysischangehandler.md)
  A handler your app provides to receive video-stream analysis results.
- [func continueStream()](./continuestream%28%29.md)
  Indicates that your app is ready to resume video stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analysischangedhandler)*
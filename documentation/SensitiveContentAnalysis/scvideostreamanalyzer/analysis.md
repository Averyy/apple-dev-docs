# analysis

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Instance Property

The results of the first detected sensitive video frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var analysis: SCSensitivityAnalysis? { get }
```

```objc
@property (readonly, nullable) SCSensitivityAnalysis * analysis;
```

#### Discussion

The analysis also includes suggestions for the app based on the nature of the sensitive content, including: [`shouldInterruptVideo`](../scsensitivityanalysis/shouldinterruptvideo.md), [`shouldIndicateSensitivity`](../scsensitivityanalysis/shouldindicatesensitivity.md) and [`shouldMuteAudio`](../scsensitivityanalysis/shouldmuteaudio.md).

## See Also

### Responding to sensitive content
- [func continueStream()](./continuestream%28%29.md)
  Indicates that your app is ready to resume video stream analysis.
- [analysisChangedHandler](./analysischangedhandler.md)
  A handler that your app provides to react to sensitive content detection.
- [SCVideoStreamAnalysisChangeHandler](../scvideostreamanalysischangehandler.md)
  A handler your app provides to receive video-stream analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analysis)*
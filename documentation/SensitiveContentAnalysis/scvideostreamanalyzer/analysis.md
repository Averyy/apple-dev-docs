# analysis

**Framework**: SensitiveContentAnalysis  
**Kind**: property

The results of the first detected sensitive video frame.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var analysis: SCSensitivityAnalysis? { get }
```

#### Discussion

The analysis also includes suggestions for the app based on the nature of the sensitive content, including: [`shouldInterruptVideo`](scsensitivityanalysis/shouldinterruptvideo.md), [`shouldIndicateSensitivity`](scsensitivityanalysis/shouldindicatesensitivity.md) and [`shouldMuteAudio`](scsensitivityanalysis/shouldmuteaudio.md).

## See Also

- [func continueStream()](scvideostreamanalyzer/continuestream.md)
  Indicates that your app is ready to resume video stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analysis)*
# continueStream()

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Indicates that your app is ready to resume video stream analysis.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func continueStream()
```

#### Discussion

When the framework detects sensitive content in the video stream, it pauses analysis and begins censoring the stream’s video frames. Call this method to resume analysis and stop censoring video frames when your app is ready to show the stream again.

## See Also

- [var analysis: SCSensitivityAnalysis?](scvideostreamanalyzer/analysis.md)
  The results of the first detected sensitive video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/continuestream())*
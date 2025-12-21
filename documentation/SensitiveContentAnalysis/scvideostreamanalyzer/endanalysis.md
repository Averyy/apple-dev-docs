# endAnalysis()

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Stops stream analysis.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func endAnalysis()
```

#### Discussion

This method stops analyzing the video stream in reference to the most recent call to `beginAnalysis`.

## See Also

- [func analyze(CVPixelBuffer)](scvideostreamanalyzer/analyze(_:).md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](scvideostreamanalyzer/beginanalysis(of:)-78qm.md)
  Analyzes video frames for the given capture device input.
- [func beginAnalysis(of: VTDecompressionSession) throws](scvideostreamanalyzer/beginanalysis(of:)-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](scvideostreamanalyzer/analysischanges.md)
  A stream your app uses to receive video-stream analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/endanalysis())*
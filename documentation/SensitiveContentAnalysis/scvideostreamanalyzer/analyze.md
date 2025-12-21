# analyze(_:)

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Analyzes individual video-stream frames for sensitive content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func analyze(_ pixelBuffer: CVPixelBuffer)
```

#### Discussion

This method analyzes a specific video frame and updates [`analysis`](scvideostreamanalyzer/analysis.md) according to the results. If your app implements a custom stream decoder, you can call this method for each video frame.

## See Also

- [func beginAnalysis(of: AVCaptureDeviceInput) throws](scvideostreamanalyzer/beginanalysis(of:)-78qm.md)
  Analyzes video frames for the given capture device input.
- [func beginAnalysis(of: VTDecompressionSession) throws](scvideostreamanalyzer/beginanalysis(of:)-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](scvideostreamanalyzer/analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](scvideostreamanalyzer/endanalysis.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analyze(_:))*
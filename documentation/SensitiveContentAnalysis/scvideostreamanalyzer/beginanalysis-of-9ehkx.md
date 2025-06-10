# beginAnalysis(of:)

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Analyzes video frames for the given decompression session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func beginAnalysis(of decompressionSession: VTDecompressionSession) throws
```

#### Discussion

If the framework detects sensitive content in the video stream, the [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession) produces blank frames to effectively censor the video stream on the person’s behalf. When your app is ready to show the video stream again, resume analysis by calling [`continueStream()`](scvideostreamanalyzer/continuestream().md).

## Parameters

- `decompressionSession`: An object that provides video frames for your app to analyze for sensitive content.

## See Also

- [func analyze(CVPixelBuffer)](scvideostreamanalyzer/analyze(_:).md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](scvideostreamanalyzer/beginanalysis(of:)-78qm.md)
  Analyzes video frames for the given capture device input.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](scvideostreamanalyzer/analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](scvideostreamanalyzer/endanalysis.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/beginanalysis(of:)-9ehkx)*
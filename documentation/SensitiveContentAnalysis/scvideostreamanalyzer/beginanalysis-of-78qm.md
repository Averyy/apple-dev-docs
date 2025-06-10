# beginAnalysis(of:)

**Framework**: SensitiveContentAnalysis  
**Kind**: method

Analyzes video frames for the given capture device input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func beginAnalysis(of captureDeviceInput: AVCaptureDeviceInput) throws
```

#### Discussion

Call this method to begin analyzing a video stream from the given [`AVCaptureDeviceInput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDeviceInput). If the framework detects sensitive content in the video stream, the `AVCaptureDeviceInput` interrupts subsequent frames with the `AVCaptureSessionInterruptionReasonSensitiveContentMitigationActivated` interruption reason to effectively censor the video stream on the person’s behalf. When your app is ready to show the video stream again, resume analysis by calling [`continueStream()`](scvideostreamanalyzer/continuestream().md).

## Parameters

- `captureDeviceInput`: An object that contains information about the specific camera and its captured content in the video stream.

## See Also

- [func analyze(CVPixelBuffer)](scvideostreamanalyzer/analyze(_:).md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: VTDecompressionSession) throws](scvideostreamanalyzer/beginanalysis(of:)-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](scvideostreamanalyzer/analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](scvideostreamanalyzer/endanalysis.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/beginanalysis(of:)-78qm)*
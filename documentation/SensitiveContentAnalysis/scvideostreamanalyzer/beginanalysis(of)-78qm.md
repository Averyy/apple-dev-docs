# beginAnalysis(of:)

**Framework**: Sensitive Content Analysis  
**Kind**: method  
**Role**: Instance Method

Analyzes video frames for the given capture device input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func beginAnalysis(of captureDeviceInput: AVCaptureDeviceInput) throws
```

```objc
- (BOOL) beginAnalysisOfCaptureDeviceInput:(AVCaptureDeviceInput *) captureDeviceInput error:(NSError **) error;
```

## Discussion

Call this method to begin analyzing a video stream from the given [`AVCaptureDeviceInput`](../../AVFoundation/avcapturedeviceinput.md). If the framework detects sensitive content in the video stream, the `AVCaptureDeviceInput` interrupts subsequent frames with the `AVCaptureSessionInterruptionReasonSensitiveContentMitigationActivated` interruption reason to effectively censor the video stream on the person’s behalf. When your app is ready to show the video stream again, resume analysis by calling [`continueStream()`](./continuestream%28%29.md).

## Parameters

- `captureDeviceInput`: An object that contains information about the specific camera and its captured content in the video stream.

## See Also

### Analyzing a video stream
- [func analyze(CVPixelBuffer)](./analyze%28_%29.md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: VTDecompressionSession) throws](./beginanalysis%28of%29-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](./analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](./endanalysis%28%29.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/beginanalysis(of:)-78qm)*
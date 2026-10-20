# beginAnalysis(of:)

**Framework**: Sensitive Content Analysis  
**Kind**: method  
**Role**: Instance Method

Analyzes video frames for the given decompression session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func beginAnalysis(of decompressionSession: VTDecompressionSession) throws
```

```objc
- (BOOL) beginAnalysisOfDecompressionSession:(VTDecompressionSessionRef) decompressionSession error:(NSError **) error;
```

#### Discussion

If the framework detects sensitive content in the video stream, the [`VTDecompressionSession`](../../VideoToolbox/vtdecompressionsession.md) produces blank frames to effectively censor the video stream on the person’s behalf. When your app is ready to show the video stream again, resume analysis by calling [`continueStream()`](./continuestream%28%29.md).

## Parameters

- `decompressionSession`: An object that provides video frames for your app to analyze for sensitive content.

## See Also

### Analyzing a video stream
- [func analyze(CVPixelBuffer)](./analyze%28_%29.md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](./beginanalysis%28of%29-78qm.md)
  Analyzes video frames for the given capture device input.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](./analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](./endanalysis%28%29.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/beginanalysis(of:)-9ehkx)*
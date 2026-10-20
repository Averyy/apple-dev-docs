# analyze(_:)

**Framework**: Sensitive Content Analysis  
**Kind**: method  
**Role**: Instance Method

Analyzes individual video-stream frames for sensitive content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func analyze(_ pixelBuffer: CVPixelBuffer)
```

```objc
- (void) analyzePixelBuffer:(CVPixelBufferRef) pixelBuffer;
```

#### Discussion

This method analyzes a specific video frame and updates [`analysis`](./analysis.md) according to the results. If your app implements a custom stream decoder, you can call this method for each video frame.

## See Also

### Analyzing a video stream
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](./beginanalysis%28of%29-78qm.md)
  Analyzes video frames for the given capture device input.
- [func beginAnalysis(of: VTDecompressionSession) throws](./beginanalysis%28of%29-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error>](./analysischanges.md)
  A stream your app uses to receive video-stream analysis results.
- [func endAnalysis()](./endanalysis%28%29.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analyze(_:))*
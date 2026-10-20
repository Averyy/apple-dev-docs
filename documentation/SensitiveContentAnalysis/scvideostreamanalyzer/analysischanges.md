# analysisChanges

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Instance Property

A stream your app uses to receive video-stream analysis results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error> { get }
```

## See Also

### Analyzing a video stream
- [func analyze(CVPixelBuffer)](./analyze%28_%29.md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](./beginanalysis%28of%29-78qm.md)
  Analyzes video frames for the given capture device input.
- [func beginAnalysis(of: VTDecompressionSession) throws](./beginanalysis%28of%29-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [func endAnalysis()](./endanalysis%28%29.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analysischanges)*
# analysisChanges

**Framework**: SensitiveContentAnalysis  
**Kind**: property

A stream your app uses to receive video-stream analysis results.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var analysisChanges: some AsyncSequence<SCSensitivityAnalysis, any Error> { get }
```

## See Also

- [func analyze(CVPixelBuffer)](scvideostreamanalyzer/analyze(_:).md)
  Analyzes individual video-stream frames for sensitive content.
- [func beginAnalysis(of: AVCaptureDeviceInput) throws](scvideostreamanalyzer/beginanalysis(of:)-78qm.md)
  Analyzes video frames for the given capture device input.
- [func beginAnalysis(of: VTDecompressionSession) throws](scvideostreamanalyzer/beginanalysis(of:)-9ehkx.md)
  Analyzes video frames for the given decompression session.
- [func endAnalysis()](scvideostreamanalyzer/endanalysis.md)
  Stops stream analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/analysischanges)*
# AVCaptureVideoStabilizationMode.lowLatency

**Framework**: AVFoundation  
**Kind**: case

Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case lowLatency
```

## See Also

- [AVCaptureVideoStabilizationMode.off](avcapturevideostabilizationmode/off.md)
  A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationMode.standard](avcapturevideostabilizationmode/standard.md)
  A mode that uses the standard algorithm.
- [AVCaptureVideoStabilizationMode.cinematic](avcapturevideostabilizationmode/cinematic.md)
  A mode that uses the cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.cinematicExtended](avcapturevideostabilizationmode/cinematicextended.md)
  A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.previewOptimized](avcapturevideostabilizationmode/previewoptimized.md)
  A mode that uses the preview optimized stabilization algorithm.
- [AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced](avcapturevideostabilizationmode/cinematicextendedenhanced.md)
  A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.auto](avcapturevideostabilizationmode/auto.md)
  A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/lowlatency)*
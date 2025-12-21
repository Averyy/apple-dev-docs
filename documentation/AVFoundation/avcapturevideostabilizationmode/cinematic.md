# AVCaptureVideoStabilizationMode.cinematic

**Framework**: AVFoundation  
**Kind**: case

A mode that uses the cinematic stabilization algorithm.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
case cinematic
```

#### Discussion

Cinematic video stabilization has a reduced field of view compared to standard video stabilization. Enabling cinematic video stabilization introduces considerably more latency into the video capture pipeline than standard video stabilization and consumes significantly more system memory.

Specify identical or similar minimum and maximum frame durations when using this mode.

## See Also

- [AVCaptureVideoStabilizationMode.off](avcapturevideostabilizationmode/off.md)
  A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationMode.standard](avcapturevideostabilizationmode/standard.md)
  A mode that uses the standard algorithm.
- [AVCaptureVideoStabilizationMode.cinematicExtended](avcapturevideostabilizationmode/cinematicextended.md)
  A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.previewOptimized](avcapturevideostabilizationmode/previewoptimized.md)
  A mode that uses the preview optimized stabilization algorithm.
- [AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced](avcapturevideostabilizationmode/cinematicextendedenhanced.md)
  A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.auto](avcapturevideostabilizationmode/auto.md)
  A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.
- [AVCaptureVideoStabilizationMode.lowLatency](avcapturevideostabilizationmode/lowlatency.md)
  Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/cinematic)*
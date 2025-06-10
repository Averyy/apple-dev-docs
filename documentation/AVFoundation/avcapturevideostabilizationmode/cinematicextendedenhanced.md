# AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced

**Framework**: AVFoundation  
**Kind**: case

A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+

## Declaration

```swift
case cinematicExtendedEnhanced
```

#### Discussion

Enhanced extended cinematic has a reduced field of view compared to extended cinematic, without any noticeable increase in latency, and it yields improved stability.

> **Note**:  It’s recommended to use identical or similar minimum and maximum frame durations in conjunction with this mode.

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
- [AVCaptureVideoStabilizationMode.auto](avcapturevideostabilizationmode/auto.md)
  A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/cinematicextendedenhanced)*
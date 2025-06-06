# AVCaptureVideoStabilizationMode.previewOptimized

**Framework**: AVFoundation  
**Kind**: case

A mode that uses the preview optimized stabilization algorithm.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+

## Declaration

```swift
case previewOptimized
```

#### Discussion

Preview stabilization is a low-latency and low-power algorithm which the system supports only on connections that have either an associated preview layer or a preview-sized [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md).

## See Also

- [AVCaptureVideoStabilizationMode.off](avcapturevideostabilizationmode/off.md)
  A mode that doesn’t stabilize video capture.
- [AVCaptureVideoStabilizationMode.standard](avcapturevideostabilizationmode/standard.md)
  A mode that uses the standard algorithm.
- [AVCaptureVideoStabilizationMode.cinematic](avcapturevideostabilizationmode/cinematic.md)
  A mode that uses the cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.cinematicExtended](avcapturevideostabilizationmode/cinematicextended.md)
  A mode that uses the extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced](avcapturevideostabilizationmode/cinematicextendedenhanced.md)
  A mode that stabilizes video using the enhanced extended cinematic stabilization algorithm.
- [AVCaptureVideoStabilizationMode.auto](avcapturevideostabilizationmode/auto.md)
  A mode that indicates the system chooses the most appropriate video stabilization mode for the device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/previewoptimized)*
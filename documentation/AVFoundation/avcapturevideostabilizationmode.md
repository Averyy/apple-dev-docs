# AVCaptureVideoStabilizationMode

**Framework**: AVFoundation  
**Kind**: enum

An enumeration of video stabilization modes that capture devices and formats support.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
enum AVCaptureVideoStabilizationMode
```

## Topics

### Stabilization modes
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
- [AVCaptureVideoStabilizationMode.lowLatency](avcapturevideostabilizationmode/lowlatency.md)
  Indicates that video should be stabilized using the low latency stabilization algorithm. Low Latency stabilization has a reduced field of view. Enabling low latency stabilization introduces no additional latency into the video capture pipeline.
### Initializers
- [init?(rawValue: Int)](avcapturevideostabilizationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isVideoStabilizationModeSupported(AVCaptureVideoStabilizationMode) -> Bool](avcapturedevice/format/isvideostabilizationmodesupported(_:).md)
  A Boolean value that indicates whether the format supports a given video stabilization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode)*
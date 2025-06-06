# videoFrameRateRangeForCenterStage

**Framework**: AVFoundation  
**Kind**: property

The range of frame rates available when Center Stage is active.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
var videoFrameRateRangeForCenterStage: AVFrameRateRange? { get }
```

#### Discussion

Devices may support a limited frame rate range when Center Stage is active. The value is `nil` if the device doesn’t support Center Stage.

## See Also

- [var isCenterStageSupported: Bool](avcapturedevice/format/iscenterstagesupported.md)
  A Boolean value that indicates whether the format supports Center Stage.
- [var videoMinZoomFactorForCenterStage: CGFloat](avcapturedevice/format/videominzoomfactorforcenterstage.md)
  The minimum zoom factor available when Center Stage is active.
- [var videoMaxZoomFactorForCenterStage: CGFloat](avcapturedevice/format/videomaxzoomfactorforcenterstage.md)
  The maximum zoom factor available when Center Stage is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcenterstage)*
# videoMaxZoomFactorForCenterStage

**Framework**: AVFoundation  
**Kind**: property

The maximum zoom factor available when Center Stage is active.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
var videoMaxZoomFactorForCenterStage: CGFloat { get }
```

#### Discussion

Devices support a limited zoom range when Center Stage is active. If the device doesn’t support Center Stage, the value is [`videoMaxZoomFactor`](avcapturedevice/format/videomaxzoomfactor.md).

## See Also

- [var isCenterStageSupported: Bool](avcapturedevice/format/iscenterstagesupported.md)
  A Boolean value that indicates whether the format supports Center Stage.
- [var videoFrameRateRangeForCenterStage: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforcenterstage.md)
  The range of frame rates available when Center Stage is active.
- [var videoMinZoomFactorForCenterStage: CGFloat](avcapturedevice/format/videominzoomfactorforcenterstage.md)
  The minimum zoom factor available when Center Stage is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcenterstage)*
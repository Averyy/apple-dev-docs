# videoMinZoomFactorForCenterStage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The minimum zoom factor available when Center Stage is active.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
var videoMinZoomFactorForCenterStage: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat videoMinZoomFactorForCenterStage;
```

#### Discussion

Devices support a limited zoom range when Center Stage is active. If the device doesn’t support Center Stage, the value is 1.0.

## See Also

### Determining Center Stage support
- [var isCenterStageSupported: Bool](./iscenterstagesupported.md)
  A Boolean value that indicates whether the format supports Center Stage.
- [var videoFrameRateRangeForCenterStage: AVFrameRateRange?](./videoframeraterangeforcenterstage.md)
  The range of frame rates available when Center Stage is active.
- [var videoMaxZoomFactorForCenterStage: CGFloat](./videomaxzoomfactorforcenterstage.md)
  The maximum zoom factor available when Center Stage is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videominzoomfactorforcenterstage)*
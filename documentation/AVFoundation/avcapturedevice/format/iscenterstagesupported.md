# isCenterStageSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format supports Center Stage.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
var isCenterStageSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCenterStageSupported) BOOL centerStageSupported;
```

## Discussion

See [`AVCaptureDevice`](../../avcapturedevice.md) for more information on using Center Stage.

## See Also

### Determining Center Stage support
- [var videoFrameRateRangeForCenterStage: AVFrameRateRange?](./videoframeraterangeforcenterstage.md)
  The range of frame rates available when Center Stage is active.
- [var videoMinZoomFactorForCenterStage: CGFloat](./videominzoomfactorforcenterstage.md)
  The minimum zoom factor available when Center Stage is active.
- [var videoMaxZoomFactorForCenterStage: CGFloat](./videomaxzoomfactorforcenterstage.md)
  The maximum zoom factor available when Center Stage is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscenterstagesupported)*
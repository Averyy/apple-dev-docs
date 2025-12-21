# shouldMatchFrameRate

**Framework**: AVFoundation  
**Kind**: property

A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var shouldMatchFrameRate: Bool { get set }
```

#### Discussion

If you want to configure your [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) to match its source [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md), set [`shouldMatchFrameRate`](avcaptureexternaldisplayconfiguration/shouldmatchframerate.md) to `true`. The default value is `false`.

## See Also

- [var bypassColorSpaceConversion: Bool](avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion.md)
  A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.
- [var preferredResolution: CMVideoDimensions](avcaptureexternaldisplayconfiguration/preferredresolution.md)
  Your preferred external display resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration/shouldmatchframerate)*
# bypassColorSpaceConversion

**Framework**: AVFoundation  
**Kind**: property

A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var bypassColorSpaceConversion: Bool { get set }
```

#### Discussion

Set [`bypassColorSpaceConversion`](avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion.md) to `true` if you would like the configurator’s  [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) color space preserved on the output display. This is accomplished by setting the working color space to match the color space of the external display. The color properties of the `CALayer` remain untouched. The default value is `false`.

## See Also

- [var preferredResolution: CMVideoDimensions](avcaptureexternaldisplayconfiguration/preferredresolution.md)
  Your preferred external display resolution.
- [var shouldMatchFrameRate: Bool](avcaptureexternaldisplayconfiguration/shouldmatchframerate.md)
  A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion)*
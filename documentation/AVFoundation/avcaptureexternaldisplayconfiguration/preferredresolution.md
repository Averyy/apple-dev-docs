# preferredResolution

**Framework**: AVFoundation  
**Kind**: property

Your preferred external display resolution.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var preferredResolution: CMVideoDimensions { get set }
```

#### Discussion

Use [`preferredResolution`](avcaptureexternaldisplayconfiguration/preferredresolution.md) to set your desired resolution of the external display. When left at the default value of { 0, 0 },  the native resolution of the external display is used.

## See Also

- [var bypassColorSpaceConversion: Bool](avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion.md)
  A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.
- [var shouldMatchFrameRate: Bool](avcaptureexternaldisplayconfiguration/shouldmatchframerate.md)
  A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration/preferredresolution)*
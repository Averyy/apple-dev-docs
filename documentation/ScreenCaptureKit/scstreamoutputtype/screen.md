# SCStreamOutputType.screen

**Framework**: ScreenCaptureKit  
**Kind**: case

An output type that represents a screen capture sample buffer.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
case screen
```

#### Discussion

This output represents a sample buffer that wraps a [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) backed by an [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface).

The width, height, and pixel format of the sample buffer reflect what you define in [`SCStreamConfiguration`](scstreamconfiguration.md). When capturing multiple windows, the system bases the width and height on the display you pass in through [`SCContentFilter`](sccontentfilter.md). You can set a background color for multi-window sample buffers by setting [`backgroundColor`](scstreamconfiguration/backgroundcolor.md); otherwise the default color is black.

## See Also

- [SCStreamOutputType.audio](scstreamoutputtype/audio.md)
  An output type that represents an audio capture sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype/screen)*
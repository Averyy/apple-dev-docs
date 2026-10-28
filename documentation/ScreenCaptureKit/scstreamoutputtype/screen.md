# SCStreamOutputType.screen

**Framework**: ScreenCaptureKit  
**Kind**: case  
**Role**: Case

An output type that represents a screen capture sample buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case screen
```

```c
SCStreamOutputTypeScreen
```

## Discussion

This output represents a sample buffer that wraps a [CVPixelBuffer](../../CoreVideo/cvpixelbuffer-q2e.md) backed by an [`IOSurface`](../../IOSurface/iosurface-page.md).

The width, height, and pixel format of the sample buffer reflect what you define in [`SCStreamConfiguration`](../scstreamconfiguration.md). When capturing multiple windows, the system bases the width and height on the display you pass in through [`SCContentFilter`](../sccontentfilter.md). You can set a background color for multi-window sample buffers by setting [`backgroundColor`](../scstreamconfiguration/backgroundcolor.md); otherwise the default color is black.

## See Also

### Output types
- [SCStreamOutputType.audio](./audio.md)
  An output type that represents an audio capture sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype/screen)*
# sessionPreset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A preset value that indicates the quality level or bit rate of the output.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var sessionPreset: AVCaptureSession.Preset { get set }
```

```objc
@property (nonatomic, copy) AVCaptureSessionPreset sessionPreset;
```

## Discussion

Specify a preset value to configure a capture session’s format and settings. The default preset is [`high`](./preset/high.md), which produces high-quality video and audio output, but you can specify any preset value that returns [`true`](../../Swift/true.md) for a call to [`canSetSessionPreset(_:)`](./cansetsessionpreset%28_%29.md).

You can set this value while the session is running.

## See Also

### Setting a session preset
- [AVCaptureSession.Preset](./preset.md)
  Presets that define standard configurations for a capture session.
- [func canSetSessionPreset(AVCaptureSession.Preset) -> Bool](./cansetsessionpreset%28_%29.md)
  Determines whether you can configure a capture session with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/sessionpreset)*
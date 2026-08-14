# sessionPreset

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

Specify a preset value to configure a capture session’s format and settings. The default preset is [`high`](avcapturesession/preset/high.md), which produces high-quality video and audio output, but you can specify any preset value that returns [`true`](https://developer.apple.com/documentation/swift/true) for a call to [`canSetSessionPreset(_:)`](avcapturesession/cansetsessionpreset(_:).md).

You can set this value while the session is running.

## See Also

- [AVCaptureSession.Preset](avcapturesession/preset.md)
  Presets that define standard configurations for a capture session.
- [func canSetSessionPreset(AVCaptureSession.Preset) -> Bool](avcapturesession/cansetsessionpreset(_:).md)
  Determines whether you can configure a capture session with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/sessionpreset)*
# canSetSessionPreset(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether you can configure a capture session with the specified preset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func canSetSessionPreset(_ preset: AVCaptureSession.Preset) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the capture session supports the preset; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Use this method to determine whether the capture session, in its current I/O configuration, supports a particular preset. You can only set a preset that returns [`true`](https://developer.apple.com/documentation/swift/true) as the capture session’s [`sessionPreset`](avcapturesession/sessionpreset.md) property value.

## Parameters

- `preset`: A preset value to test.

## See Also

- [AVCaptureSession.Preset](avcapturesession/preset.md)
  Presets that define standard configurations for a capture session.
- [var sessionPreset: AVCaptureSession.Preset](avcapturesession/sessionpreset.md)
  A preset value that indicates the quality level or bit rate of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/cansetsessionpreset(_:))*
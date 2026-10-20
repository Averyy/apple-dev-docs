# AVCaptureSession.Preset

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Presets that define standard configurations for a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
struct Preset
```

```c
typedef NSString * AVCaptureSessionPreset;
```

#### Discussion

Setting a [`sessionPreset`](./sessionpreset.md) value provides a convenient way to configure a capture session for common use cases.

## Topics

### Quality levels
- [static let high: AVCaptureSession.Preset](./preset/high.md)
  A preset suitable for capturing high-quality output.
- [static let medium: AVCaptureSession.Preset](./preset/medium.md)
  A preset suitable for capturing medium-quality output.
- [static let low: AVCaptureSession.Preset](./preset/low.md)
  A preset suitable for capturing low-quality output.
### Photo
- [static let photo: AVCaptureSession.Preset](./preset/photo.md)
  A preset suitable for capturing high-resolution photo quality output.
### Manual configuration
- [static let inputPriority: AVCaptureSession.Preset](./preset/inputpriority.md)
  A preset that doesn’t specify audio and video output settings for a capture session.
### High definition
- [static let qHD960x540: AVCaptureSession.Preset](./preset/qhd960x540.md)
  A preset suitable for capturing quarter HD quality (960 x 540 pixel) video output.
- [static let hd1280x720: AVCaptureSession.Preset](./preset/hd1280x720.md)
  A preset suitable for capturing 720p quality (1280 x 720 pixel) video output.
- [static let hd1920x1080: AVCaptureSession.Preset](./preset/hd1920x1080.md)
  A preset suitable for capturing 1080p-quality (1920 x 1080 pixels) video output.
- [static let hd4K3840x2160: AVCaptureSession.Preset](./preset/hd4k3840x2160.md)
  A preset suitable for capturing 2160p-quality (3840 x 2160 pixels) video output.
### VGA
- [static let qvga320x240: AVCaptureSession.Preset](./preset/qvga320x240.md)
  A preset suitable for capturing 320 x 240 pixel video output.
- [static let vga640x480: AVCaptureSession.Preset](./preset/vga640x480.md)
  A preset suitable for capturing VGA quality (640 x 480 pixel) video output.
### iFrame
- [static let iFrame960x540: AVCaptureSession.Preset](./preset/iframe960x540.md)
  A preset suitable for capturing 960 x 540 quality iFrame H.264 video at about 30 Mbits/sec with AAC audio.
- [static let iFrame1280x720: AVCaptureSession.Preset](./preset/iframe1280x720.md)
  A preset suitable for capturing 1280 x 720 quality iFrame H.264 video at about 40 Mbits/sec with AAC audio.
### CIF
- [static let cif352x288: AVCaptureSession.Preset](./preset/cif352x288.md)
  A preset suitable for capturing CIF quality (352 x 288 pixel) video output.
### Initializers
- [init(rawValue: String)](./preset/init%28rawvalue%29.md)
  Creates a preset with a string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting a session preset
- [func canSetSessionPreset(AVCaptureSession.Preset) -> Bool](./cansetsessionpreset%28_%29.md)
  Determines whether you can configure a capture session with the specified preset.
- [var sessionPreset: AVCaptureSession.Preset](./sessionpreset.md)
  A preset value that indicates the quality level or bit rate of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset)*
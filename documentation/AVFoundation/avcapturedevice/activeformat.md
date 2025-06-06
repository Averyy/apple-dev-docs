# activeFormat

**Framework**: AVFoundation  
**Kind**: property

The capture format in use by the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var activeFormat: AVCaptureDevice.Format { get set }
```

#### Discussion

In iOS, a device’s active format and a capture session’s [`sessionPreset`](avcapturesession/sessionpreset.md) are mutually exclusive. If you set a device’s active format, the session to which it’s attached changes its preset to [`inputPriority`](avcapturesession/preset/inputpriority.md). Likewise if you set a preset on a capture session, the session assumes control of its input devices, and configures their active format appropriately.

> **Note**:  Audio devices don’t expose any user-configurable formats in iOS. To configure audio input on iOS, use [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) and its related APIs instead.

 Audio devices don’t expose any user-configurable formats in iOS. To configure audio input on iOS, use [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) and its related APIs instead.

Set the [`activeFormat`](avcapturedevice/activeformat.md), [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md), and [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md) properties simultaneously by performing the configuration between calls to the session’s [`beginConfiguration()`](avcapturesession/beginconfiguration().md) and [`commitConfiguration()`](avcapturesession/commitconfiguration().md) methods.

```swift
// Configure capture session.
captureSession.beginConfiguration()

do {
    try device.lockForConfiguration()
    
    // Set the device's active format.
    device.activeFormat = // a supported format.
    
    // Set the device's min/max frame duration.
    device.activeVideoMinFrameDuration = // a supported minimum duration.
    device.activeVideoMaxFrameDuration = // a supported maximum duration.
    
    device.unlockForConfiguration()
} catch {
    // Handle error.
}

// Apply the changes to the session.
captureSession.commitConfiguration()
```

If you configure a session to use an active format intended for high resolution still photography, and you apply zoom, orientation, or format changes to an [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md), the system may not meet the target framerate.

This property is key-value observable.

## See Also

- [var formats: [AVCaptureDevice.Format]](avcapturedevice/formats.md)
  The capture formats a device supports.
- [var activeDepthDataFormat: AVCaptureDevice.Format?](avcapturedevice/activedepthdataformat.md)
  The currently active depth data format of the capture device.
- [AVCaptureDevice.Format](avcapturedevice/format.md)
  A class that defines media formats and capture settings that capture devices support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeformat)*